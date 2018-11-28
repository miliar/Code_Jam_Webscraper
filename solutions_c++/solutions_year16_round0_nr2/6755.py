#include<iostream>
#include<cstring>
using namespace std;

char s[123];
int main(){
int t;cin>>t;
for(int i=1;i<=t;i++){
cin>>s;
int n=strlen(s);
int nn=1;
for(int i=1;i<n;i++){
if(s[i]!=s[i-1])nn++;
}
if(s[0]=='+')cout<<"Case #"<<i<<": "<<(nn/2)*2<<endl;
else cout<<"Case #"<<i<<": "<<((nn+1)/2)*2-1<<endl;
}
return 0;
}
