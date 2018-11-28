#include <iostream>
#include <vector>
#include <utility>
#include <sstream>
using namespace std;

int main(){
    int t; cin>>t;
    for(int tt=0;tt<t;tt++){
        string s; cin>>s;
        int b=1;

        char p=s[0];
        for(int i=0;i<s.size();i++){
            if(s[i]!=p){
                b++;
                p=s[i];
            }
        }

        if(s[s.size()-1]=='+'){
            b--;
        }

        cout << "Case #" << tt+1 << ": " << b << endl;
    }
}
