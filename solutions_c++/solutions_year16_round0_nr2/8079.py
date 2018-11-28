#include<iostream>
#include<stack>
#include<fstream>
#include<string>
#include<algorithm>
#include<stdio.h>
using namespace std;
stack <char> s,s1;
int main(){
    freopen("Bl.in","r",stdin);
    freopen("o6.out","w",stdout);
    int t,i,l,j;
    string s;
    cin>>t;
    for(i=1;i<=t;i++){
    cin>>s;
    if(s.length()==1){
    if(s[0]=='-')
    cout<<"Case #"<<i<<": 1"<<endl;
    else
    cout<<"Case #"<<i<<": 0"<<endl;
 }
else{
        bool flag=true;
        int op=0;
        while(flag==true){
            if(s[s.length()-1]=='+')
                {s.erase(s.end()-1);
                if(s.length()==0)
                    flag=false;
                }
            else{
                    op++;
            replace(s.begin(),s.end(),'-','a');        //cout<<s<<endl;
            replace(s.begin(),s.end(),'+','b');        //cout<<s<<endl;
            replace(s.begin(),s.end(),'a','+');        //cout<<s<<endl;
            replace(s.begin(),s.end(),'b','-');        //cout<<s<<endl;
            for(j=0;j<s.length();j++)
                if(s[j]=='-') break;
            if(j==s.length()) flag=false;
            }
        }
    cout<<"Case #"<<i<<": "<<op<<endl;
 }
    }
return 0;
}
