#include <iostream>
#include <fstream>
using namespace std;
bool match(int r1,int r2,int r3,int r4,int t){
  if(r1==t||r2==t||r3==t||r4==t)return true;
  else return false;
}
int main(int argc,char **argv){
//A A A A
//A A A A
//A A A A
//A A A A
  char *file_name=argv[1];
  ifstream infile(file_name);
  if(!infile){
    cout<<"error opening file\n";
  }
  int T;
  int g1,g2;
  int r1,r2,r3,r4;
  infile>>T;
  int n,t,res;
  for(int i=1;i<=T;i++){
    cout<<"Case #"<<i<<": ";
    infile>>g1;
    for(int k=1;k<=4;k++){
      if(g1!=k){
        infile>>t;
        infile>>t;
        infile>>t;
        infile>>t;
        continue;
      }
      infile>>r1;
      infile>>r2;
      infile>>r3;
      infile>>r4;
    }
    infile>>g1;
    n=0;
    for(int k=1;k<=4;k++){
      if(g1!=k){
        infile>>t;
        infile>>t;
        infile>>t;
        infile>>t;
        continue;
      }
      for(int i=0;i<4;i++){
        infile>>t;
        //cout<<r1<<" "<<r2<<" "<<r3<<" "<<r4<<" "<<t<<endl;
        if(match(r1,r2,r3,r4,t)){
          n++;res=t;
        }
      }
    }
    if(n==0){
      cout<<"Volunteer cheated!"<<endl;
    }
    else if (n>1){
      cout<<"Bad magician!"<<endl;
    }
    else{
      cout<<res<<endl;
    }
  }
  return 0;
}
