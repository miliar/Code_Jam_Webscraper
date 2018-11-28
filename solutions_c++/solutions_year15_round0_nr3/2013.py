#include <vector>
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;
int main(){
int T;
cin>>T;

for(int i=0;i<T;++i){
int L,X;
cin>>L>>X;
string s;
cin>>s;
int c=1;

int pos=0;
for(int k=0; k<X && k<X%16+16;++k){
for(int j=0;j<L;++j)
{
if((c==1 && s[j]=='i') || (c==3 && s[j]=='k') || (c==-4 && s[j]=='j')) c=2;
else if((c==-1 && s[j]=='i') || (c==-3 && s[j]=='k') || (c==4 && s[j]=='j')) c=-2;
else if((c==-2 && s[j]=='i') || (c==-4 && s[j]=='k') || (c==-3 && s[j]=='j')) c=1;
else if((c==2 && s[j]=='i') || (c==4 && s[j]=='k') || (c==3 && s[j]=='j')) c=-1;
else if((c==1 && s[j]=='j') || (c==-2 && s[j]=='k') || (c==4 && s[j]=='i')) c=3;
else if((c==-1 && s[j]=='j') || (c==2 && s[j]=='k') || (c==-4 && s[j]=='i')) c=-3;
else if((c==1 && s[j]=='k') || (c==-3 && s[j]=='i') || (c==2 && s[j]=='j')) c=4;
else if((c==-1 && s[j]=='k') || (c==3 && s[j]=='i') || (c==-2 && s[j]=='j')) c=-4;

if(c==2 && pos==0) { pos=1; c=1;}
if(c==3 && pos==1) {pos=2; c=1;}
if(c==4 && pos==2) { pos=3; c=1;}
}
}
if(c==1 && pos==3) cout<<"Case #"<<i+1<<": "<<"YES"<<endl;
else cout<<"Case #"<<i+1<<": "<<"NO"<<endl;
}


}
