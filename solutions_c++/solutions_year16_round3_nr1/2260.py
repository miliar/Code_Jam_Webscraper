#include <cstdio>
#include <iostream>
using namespace std;

int n,tc;
int v[2000];



void best3(int &i1,int &i2,int ix){
  if(v[ix]>v[i2]) i2=ix;
  if(v[i2]>v[i1]) {int tmp=i1;i1=i2;i2=tmp;}
}

void clean_party(int size, char name){
  while(size>0){
    cout<<' '<<name;
    size--;
  }
}

void process(){
  int i1,i2;
  if(v[0]>v[1]){i1=0;i2=1;}
  else {i1=1;i2=0;}
  
  for(int i=2;i<n;i++){
    best3(i1,i2,i);
  }
  int bigger = i1;
  int sbigger = i2;
  int biggerV = v[i1]; 
  int sbiggerV = v[i2];
  v[i1] = 0;
  v[i2] = 0;


  clean_party(biggerV-sbiggerV, bigger+'A');

  for(int i=0;i<n;i++){
    clean_party(v[i], i+'A');
  }

  while(sbiggerV--){
    char pa = bigger+'A';
    char pb = sbigger+'A';
    cout<<' '<<pa<<pb;
  }


  cout<<endl;

}

int main(){
  cin>>tc;
  for(int ii=1;ii<=tc;ii++){
    cin>>n;
    for(int i=0;i<n;i++){
      cin>>v[i];
    }

    cout<<"Case #"<<ii<<":";
    process();    
  }


  return 0;
}
