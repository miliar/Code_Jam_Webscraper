#include<bits/stdc++.h>
using namespace std;

int main(){
long long int n,t,i,j,k,tog,new1,new2;int a[10];
cin>>t;k=1;
while(k<=t){
 cin>>n;
  if(n==0)cout<<"Case #"<<k<<": INSOMNIA"<<endl;
  else{
  for(i=0;i<10;i++)a[i]=0;i=1;tog=1;new1=0;new2=0;
   while(tog && new2<=LLONG_MAX){
   new1=n*i;new2=new1;
   while(new1){
   a[new1%10]=1;
   new1=new1/10;
   }tog=0;
   for(j=0;j<10;j++){if(a[j])continue;else {tog=1;break;}}
   i++;
   }
   if(tog==0)
  cout<<"Case #"<<k<<": "<<new2<<endl;
   else cout<<"Case #"<<k<<": INSOMNIA"<<endl;
  }
 k++;

}




}

