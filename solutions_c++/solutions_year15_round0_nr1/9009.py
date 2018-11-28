/*
ID: mah.tg.1
PROG: beads
LANG: C++
*/
#include<bits/stdc++.h>
using namespace std;
int main(){
freopen("A-large.in", "rt", stdin);
freopen("A large.txt", "wt", stdout);
long t,l,n,i,c=0,sum=0;
string s;
cin>>t;
for(l=0;l<t;l++){
    cin>>n>>s;
    for(i=0;i<s.size();i++){
        if(s[i]!='0'){
            if(i>sum){
                c+=i-sum;
                sum+=i-sum;
            }
        }
        sum+=s[i]-'0';
    }
    cout<<"Case #"<<l+1<<": "<<c<<endl;
    c=0;
    sum=0;
}
return 0;
}
