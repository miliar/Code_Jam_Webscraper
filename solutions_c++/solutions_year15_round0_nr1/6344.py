#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int main(){
char c,str[1100];
int T,Sm,arr[1100];
cin>>T;
for(int i=0;i<T;i++){
int ava=0,ans=0;
cin>>Sm;
cin>>str;
for(int j=0;j<=Sm;j++){
arr[j]=(str[j]-'0');
}
for(int j=0;j<=Sm;j++){
if(ava<j){
ans=ans+j-ava;
ava=j;

}
ava=ava+arr[j];
}
cout<<"Case #"<<i+1<<": "<<ans<<endl;
}
return 0;
}