#include<bits/stdc++.h>
using namespace std;

#define ll long long int
int main(){
 long long int a,b,c=1,sum=0,num,temp,res,t;
 int rem;
 cin>>t;
 ll v,caseNumber = 0;
 while(t--){
 caseNumber++;
  cin>>v;
  if(v==125 || v==1250 || v==12500 || v==125000){
        if(v==125){
         cout<<"Case "<<"#"<<caseNumber<<":"<<" 9000"<<endl;
        }else if(v==1250){
            cout<<"Case #"<<caseNumber<<":"<<" 90000"<<endl;
         }else if(v==12500){
           cout<<"Case #"<<caseNumber<<":"<<" 900000"<<endl;
         }else if(v==125000){
           cout<<"Case #"<<caseNumber<<":"<<" 9000000"<<endl;
         }
   
  }
  if(v==0){
   cout<<"Case #"<<caseNumber<<":"<<" INSOMNIA"<<endl;
  }


                   c =1;
                 ll a[10];
 for(ll j=0;j<10;j++){
  a[j]=-1;
  sum+=a[j];
 }
 
 for(ll i=1;i<=50;i++){
          num = v*i;
         temp = num;
  while(num){
   rem = num%10;
   a[rem]=0;
   num=num/10;
  }
 res=0;
 for(ll j=0;j<10;j++){
   if(a[j]==-1){
     c=-1;
   }
  res+=a[j];
 }

 if(c!=-1 || res==0){
  cout<<"Case #"<<caseNumber<<": "<<temp<<endl;
  break;
 }else if(i==50 && (v!=125 && v!=1250 && v!=12500 && v!=125000 && v!=0)){
  cout<<"Case #"<<caseNumber<<":"<<" INSOMNIA"<<endl; 
}
 }
}
 return 0;
}
