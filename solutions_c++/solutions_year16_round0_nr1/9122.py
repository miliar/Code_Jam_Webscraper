#include <cstdio>
#include <iostream>
using namespace std;
#define ulli unsigned long long int

int n;
bool v[10];
int counter;
unsigned long long value, tmp,original;

void init(){
    for(int i=0;i<10;i++)
      v[i]=false;
    counter = 0;
}

int main(){
  int tc = 1;
  cin>>n;
  while(n--){
    init();
    cin>>value;
    original = value;
    
    if(value==0){
      cout<<"Case #"<<(tc++)<<": INSOMNIA"<<endl;
    } else{
      while(counter!=10){
        tmp = value;
        while(tmp>0){
          if(!v[tmp%10]){
            counter++;
            v[tmp%10] = true;
          }
          tmp = tmp/10;
        }
        value+=original;
      }
      cout<<"Case #"<<(tc++)<<": "<<(value-original)<<endl;

    }


  }

  return 0;
}

