#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;
#define S(a) scanf("%d",&(a))
int main(){
int t,ct=1,result,n,c;
string str;
freopen("A-small-attempt0.in","r",stdin);
freopen("output.txt","w",stdout);
cin>>t;
while(t--){
result=0;
cin>>str;
S(n);
for(int i=0;i<str.length();i++)
for(int j=i+n;j<=str.length();j++){
c=0;
for(int k=i;k<j;k++){

if(str[k]=='a' || str[k]=='e' || str[k]=='i'|| str[k]=='o' || str[k]=='u')
c=0;
else
c++;
if(c>=n){
result++;
break;
}
}
}
printf("Case #%d: %d\n",ct++,result);
}
}
