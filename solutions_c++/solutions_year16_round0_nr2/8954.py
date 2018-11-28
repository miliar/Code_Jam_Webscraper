#include <bits/stdc++.h>
using namespace std;
string s;
void flip(int n){
    for(int i=0;i<=n;i++)
        {
        if(s[i]=='+')s[i]='-';
        else
            s[i]='+';
    }
}
int main(){
    int t;cin>>t;
    for(int i=1;i<=t;i++){int f=0;
     cin>>s;
     for(int j=1;j<s.length();j++){
         if(s[j]!=s[j-1]){flip(j-1);f++;}
         }
                          if(s[0]=='-')f++;
     cout<<"Case #"<<i<<": "<<f<<"\n";
 }
    return 0;
}
