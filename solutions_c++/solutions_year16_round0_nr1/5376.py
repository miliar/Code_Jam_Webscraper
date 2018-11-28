#include<bits/stdc++.h>
using namespace std;
long long x,a[101],ch[10],y,cnt=1,z;
bool flag;
int main(){
  /*ifstream m;
  m.open ("A-small-attempt4.in");
  ofstream f;
  f.open("output.txt");*/
 cin>>x;
 //m>>x;
 for(int i=0;i<x;i++){
  cin>>a[i];
  //m>>a[i];
 }
 for(int i=0;i<x;i++){
    for(int j=0;j<=9;j++){ch[j]=0;}

  if(a[i]){
  flag=true;
  cnt=1;
  while(flag){
   flag=false;
   y=a[i]*cnt;
     while(y>0){
      z=y%10;
      ch[z]=1;
      y/=10;
   }
   for(int k=0;k<=9;k++){
   // cout<<ch[i]<<" ";
    if(ch[k]!=1){
     flag=true;
     break;
    }
   }
  // cout<<endl;
   cnt++;
  }
  a[i]*=(cnt-1);
 }
 else a[i]=-1;
 }
 for(int i=0;i<x;i++){
  if(a[i]!=-1)cout<<"Case #"<<i+1<<": "<<a[i]<<endl;
  else cout<<"Case #"<<i+1<<": INSOMNIA"<<endl;
 }
}
