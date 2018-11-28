#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
int T;
void solve(int,string);
int main(){
    cin >> T;
    for(int i=1;i<=T;++i){
        string s;
        cin >> s;
        solve(i,s);
    }
}

void solve(int i,string s){
    string res(1,s[0]);
    for(int j=1;j<s.size();++j){
        string r1 = res + s[j];
        string r2 = s[j] + res;
        res = max(r1,r2);
    }
    cout<<"Case #"<<i<<": "<<res<<endl;

}
