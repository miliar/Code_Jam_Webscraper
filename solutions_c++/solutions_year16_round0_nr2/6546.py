#include <iostream>
#include <fstream>

using namespace std;

bool allPlus(string seq){
    int i=0;
    while(i<seq.length()){
        if(seq[i]=='-'){
            return false;
        }
        i++;
    }
    return true;
}

string flip(string seq){
    string ans="";
    char type;
    if(seq[0]=='+'){
        type = '-';
    }
    else{
        type = '+';
    }
    for(int i=0;i<seq.length();i++){
        ans=ans+type;
    }
    return ans;
}

int main(){
    ifstream in("B-large.in");
    ofstream out("B-large.out");
    int numCases;
    if (!in.is_open())
    {
        //handle
        cout << "not open" << endl;
        return 1;
    }
    in >> numCases;
    for (int j = 0; j < numCases; ++j) {
        string seq="";
        in >> seq;
        int flipTimes=0;
        char type;

        while(!allPlus(seq)) {
            type = seq[0];
            int i = 0;
            while (i < seq.length() && seq[i] == type) {
                i++;
            }
            string temp = seq.substr(0, i);
            seq = seq.substr(i);
            temp = flip(temp);
            seq = temp + seq;
            flipTimes++;
        }
        out << "Case #" << j + 1 << ": " << flipTimes << endl;
    }

    in.close();
    out.close();

    return 0;
}
