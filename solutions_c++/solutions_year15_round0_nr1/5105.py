#include <bits/stdc++.h>
using namespace std;

int main(){
    ifstream cin("input.txt");
    ofstream cout("output.txt");
    int T;
    cin>>T;
    for(int c=1;c<=T;c++){
        int sm;
        string s;
        cin>>sm>>s;
        int standing=0;
        int res = 0;
        for(int sh=0;sh<s.size();sh++){
            if(sh<=standing){
                standing+=(s[sh]-'0');
                continue;
            }
            res+=(sh-standing);
            standing+=(s[sh]-'0')+sh-standing;
        }
        cout<<"Case #"<<c<<": "<<res<<endl;
        }
}
