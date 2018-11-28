/*By Hitesh Kalwani (India)*/
#include<bits/stdc++.h>
using namespace std;
int main(){
  //freopen("A-large.in","r",stdin);
  //freopen("output.out","w",stdout);
  long long i,t,n;
  cin>>t;
  for(long long cas=1;cas<=t;cas++){
    long long c=0,sum=0;
    cin>>n;
    string s;
    cin>>s;
    sum=sum+(s[0]-48);
    for(i=1;i<s.size();i++){
         if(sum<i){
         c+=(i-sum);
         sum+=(s[i]-48)+(i-sum);}
         else
         sum+=(s[i]-48);}
    cout<<"Case #"<<cas<<": "<<c<<endl;}
return 0;}
