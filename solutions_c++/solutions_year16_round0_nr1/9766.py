#include<bits/stdc++.h>
#include<iostream>
#include <cstdlib> 

using namespace std;

int main(){
long long int n,t,i,j,k,str,mani,mani1;
  int* a = (int*)std::malloc(sizeof(int));

cin>>t;k=1;
while(k<=t){
 cin>>n;
  if(n==0)cout<<"Case #"<<k<<": INSOMNIA"<<endl;
  else{
  for(i=0;i<10;i++)
  {
 a[i]=0;i=1;str=1;mani=0;mani1=0;
  }
   while(str && mani1<=LLONG_MAX){
   mani=n*i;
   mani1=mani;
   while(mani){
   a[mani%10]=1;
   mani=mani/10;
   }str=0;
   for(j=0;j<10;j++){if(a[j])continue;else {str=1;break;}}
   i++;
   }
   if(str==0)
  cout<<"Case #"<<k<<": "<<mani<<endl;
   else cout<<"Case #"<<k<<": INSOMNIA"<<endl;
  }
 k++;

}




}
