#include<bits/stdc++.h>
using namespace std;
bool check(string s){
bool flag=false;
int counter=0;
for(int i=0;i<s.size();i++){
    if(s[i]=='+'){counter++;}
}
if(counter==s.size()){flag=true;}
return flag;}
int main(){
    freopen("B-large.in","r",stdin);
    freopen("out6.out","w",stdout);
    int T;cin>>T;
    int C=0;
    while(T--){
    C++;
    string s;
    cin>>s;
    cout<<"Case #"<<C<<": ";
    int coun=0;
    while(check(s)==false){
        coun++;
        bool counter=0;
        for(int i=0;i<s.size();i++){
            if(s[i]=='-'){coun+=counter;break;}
            else{s[i]='-';counter++;}
        }
        for(int i=0;i<s.size();i++){
            if(s[i]=='+'){
                break;
            }
            else{s[i]='+';}
        }
    }
    cout<<coun<<endl;
    }

return 0;}
