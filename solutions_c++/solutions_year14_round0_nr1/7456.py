#include<iostream>
using namespace std;

int a[16],b[16];
int main(){
  int T;
  cin>>T;
  int n=1;
  while(T--){
    int p1,p2;
    cin>>p1;
    for(int i=0;i<16;++i)
      cin>>a[i]; 
    cin>>p2;
    for(int i=0;i<16;++i)
      cin>>b[i];
    int cnt=0,v=-1;
    for(int k=(p1-1)*4;k<p1*4;++k)
      for(int z=(p2-1)*4;z<p2*4;++z){
        if(a[k]==b[z]){
          cnt++;
          v=a[k];
         }
      }
    // cout<<cnt<<endl;
     cout<<"Case #"<<n++<<": ";
     if(cnt==1)
        cout<<v<<endl;
     else if(cnt==0)
        cout<<"Volunteer cheated!"<<endl;
     else
        cout<<"Bad magician!"<<endl;
  }
}
