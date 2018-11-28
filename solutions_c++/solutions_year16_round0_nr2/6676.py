#include <iostream>
#include<cstring>
#include<stdio.h>
#define loop(i,a) for(int i=a;i>0;i--)
using namespace std;
int main(){
int t,i=1;
cin>>t;
while(t--){
char s[102];
cin>>s;
int count=0,k=1;
loop(i,strlen(s)-1){
if(k==1&&s[i]=='-') k=0;
if(k==0)
  if(s[i]!=s[i-1])count++;  
}
if(k==1&&s[0]=='-') count=0;
else if(s[0]=='-'&&count==0) count=0;
else if(count==0) count=-1;
printf("Case #%d: %d\n",i,count+1);
i++;    
}
return 0;
} 