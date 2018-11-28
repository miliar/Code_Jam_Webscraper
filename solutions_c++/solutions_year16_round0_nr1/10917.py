#include<iostream>
#include<fstream>
#include<sstream>
#include<vector>
#include<algorithm>

using namespace std;

int main(){
    int T=0;
    long int N;
    vector<string> lines;
    ifstream in("A-large-practice.in");
    ofstream out("out.txt");
    if (!in) {
        //cout << "File A-small-practice.in not found." << endl;
        return -1;
    }
    string line;
    getline(in, line);
    istringstream iss1(line);
    iss1 >> T;
    for(int i = 1; i <= T; i++){
        getline(in, line);
        istringstream iss(line);
        iss >> N;
        if(N == 0){
            out<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
            continue;
        }
        int j = 1,k,digits[10] = {0}, allVisited = 0;
        long int temp;
        for(; allVisited == 0; j++){
            temp = N;
            temp = temp * j;
            stringstream ss;
            ss <<temp;
            std::string str = ss.str();
            for(std::string::iterator it = str.begin(); it != str.end(); ++it){
                k = *it - '0';
                if(digits[k] == 0)
                    digits[k] = 1;
            }
            int flag = 1;
            for(int x = 0; x < 10 ; x++)
                if(digits[x] == 0){
                    flag = 0;
                    break;
            }

            if(flag){
                allVisited = 1;
                out<<"Case #"<<i<<": "<<temp<<endl;
            }

        }
    }

    return 0;
}
