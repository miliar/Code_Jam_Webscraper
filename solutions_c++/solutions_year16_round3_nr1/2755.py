#include <iostream>
#include <string>
#include <stdexcept>
#include <sstream>
#include <queue>
#include <vector>

using namespace std;

class Party {
    friend bool operator>(const Party& lhs, const Party& rhs);
public:
    int member;
    char brand;
};

bool operator > (const Party& lhs, const Party& rhs){
    return lhs.member < rhs.member;
}

int main(){
    int num, count = 0;
    string line;
    
    if(getline(cin, line)){
        try{
            num = stoi(line);
        }
        catch(const invalid_argument& ia){
            cerr << "Invalid argument: " << ia.what() << '\n';
            return -1;
        }
        catch(const out_of_range& oor){
            cerr << "Out of Range error: " << oor.what() << '\n';
            return -1;
        }
    }
    // cout << "Num of test: " << num << endl; 

    while(getline(cin, line)){
        stringstream ss(line);
        int parties;
        int remain = 0;
        priority_queue<Party, vector<Party>, greater<Party> > senate;
        ss >> parties;

        getline(cin, line);
        ss.clear();
        ss.str(line);

        for(int i = 0; i < parties; i++){
            int member;
            ss >> member;
            remain += member;
            Party party;
            party.member = member;
            party.brand = ('A' + i);

            senate.push(party);
        }
        
        /*
        cout << "++++++" << endl;
        while(senate.size()){
            Party top = senate.top();
            senate.pop(); 
            cout << "DEBUG:" << top.brand << "," << top.member << endl;
        }
        cout << "++++++" << endl;
        continue;
        */

        string answer = "";
        while(true){
            char ch1, ch2;
            Party top1 = senate.top();
            ch1 = top1.brand;
            // cout << "~" << ch1 << "-" << top1.member << ",";
            if(top1.member == 0)
                break;

            senate.pop();
            top1.member--;
            senate.push(top1);

            Party top2 = senate.top();
            ch2 = top2.brand;
            // cout << ch2 << "-" << top2.member << endl;
            if( remain-1 >= 2*top2.member ){
                answer += ch1;
                answer += " ";
                remain--;
                continue;
            }

            senate.pop();
            top2.member--;
            senate.push(top2);
            
            answer += ch1;
            answer += ch2;
            answer += " ";
            remain -= 2;
        }
        
        cout << "Case #" << ++count << ": " << answer << endl;
    }

    return 0;
}
