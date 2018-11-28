#include<bits/stdc++.h>
using namespace std;
long long n,aux;


int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
int t;
cin>>t;
for(int cc=1;cc<=t;++cc){

    string s;
    cin>>s;
    int groups=0;
    char c=s[0];
    for(int i=1;i<s.size();++i){
        if(s[i]!=c)groups++,c=s[i];
    }
    if(s[s.size()-1]=='-'){
     groups++;
    }
    //cout<<groups<<endl;
   cout<<"Case #"<<cc<<": "<<groups<<endl;
}

return 0;
}
