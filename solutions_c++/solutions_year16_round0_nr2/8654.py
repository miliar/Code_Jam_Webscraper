#include<iostream>
#include<string.h>
using namespace std;
int main(){
int test,k=1;
cin>>test;
while(test--){
char string[1000],current,prev;
cin>>string;
int j=strlen(string);
if(j==1){
if(string[0]=='-') cout<<"Case #"<<k<<": "<<1<<'\n';
else cout<<"Case #"<<k<<": "<<0<<'\n';
}
else{
int i=1,count=0;
while(string[i]!='\0'){
current=string[i];
prev=string[i-1];
if(current!=prev){
count++;
for(int j=0;j<i;j++){
string[j]=current;
}
}
i++;
}
if(string[0]=='-') cout<<"Case #"<<k<<": "<<count+1<<'\n';
else cout<<"Case #"<<k<<": "<<count<<'\n';
}
k++;
}
return 0;
}
