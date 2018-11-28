#include<iostream>
#include<string>
using namespace std;
int main(){
   int tcase;
   cin>>tcase;
   for(int i=0;i<tcase;i++){
     int a;
     int b;
     int k;
     cin>>a>>b>>k;
     int count=0;
     for(int p=0;p<a;p++){
        for(int l=0;l<b;l++){
        for(int z=0;z<k;z++){
          if(z==(p&l)){
         // cout<<p<<" "<<l<<endl;
          count++;
          break;
          }
          }
          }
          }
    cout<<"case #"<<i+1<<": "<<count<<endl;
   }
}
