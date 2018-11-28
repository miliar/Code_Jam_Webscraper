#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
string re[1005];
int main(){
    int t,ip;
    cin>>t;
    ip=1;
    while(t--){
        string s;
        cin>>s;
        re[1]=s[0];
        for(int i=1;i<s.size();++i){
            string f=re[i];
            string g=f;
            g=s[i]+re[i];
            f=re[i]+s[i];
            re[i+1]=max(f,g);
        }
        cout << "Case #" << ip++ << ": " << re[(int)s.size()] << endl;
    }
    return 0;
}