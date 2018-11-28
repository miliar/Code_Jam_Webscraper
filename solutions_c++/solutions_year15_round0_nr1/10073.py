#include<bits/stdc++.h>
using namespace std;
int main(){
freopen("a.in","rt",stdin);
freopen("a.out","wt",stdout);
   int t;
   cin>>t;
   int n;
   string s;
   for(int g=1;g<=t;g++){
     cin>>n;
     cin>>s;
     vector<int>v;
    for(int i=0;i<s.length();i++){
          v.push_back(s[i]-'0');
    }
    int p=0;
    int ans=0;
    p+=v[0];
    for(int i=1;i<v.size();i++){
       if(p<i){
       ans+=i-p;
        p+=i-p;
       }
       p+=v[i];

    }
    cout<<"Case #"<<g<<": "<<ans<<endl;
   }
}
