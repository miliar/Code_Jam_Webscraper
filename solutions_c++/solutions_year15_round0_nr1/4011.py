#include <iostream>
#include <string>
#include <cstdio>
using namespace::std;
int T,n,stojace,temp,ans;
string s;

int main() {
cin>>T;

for(int test=1; test<=T; test++){
cin>>n>>s;
ans=0;
stojace=0;
    for(int i=0; i<s.size(); i++){
       temp=int(s[i]-'0');
       if(stojace>=i) stojace+=temp;
       else if(temp!=0){
            ans+=(i-stojace);
            stojace+=(temp+(i-stojace));
       }
    }
cout<<"Case #"<<test<<": "<<ans<<endl;
}
return 0;
}
