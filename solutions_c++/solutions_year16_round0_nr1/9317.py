#include <iostream>

using namespace std;

bool c[10];

void clean(){
  for(int i=0;i<10;i++)c[i]=false;
}

bool check(){
  for(int i=0;i<10;i++){
    if(!c[i]){
      return false;
    }
  }
  return true;
}

void add(int n){
  int digit;
  while(n>0)
    {
        digit = n % 10;
        n = n / 10;
        c[digit]=true;
    }
}


int main(){
  int testCases=0,cas=0;
  int n,i;
  bool c[10],insomnia;

  cin>>testCases;
  while(testCases>0){
    clean();
    cin>>n;
    insomnia=true;
    cas++;
    cout<<"Case #"<<cas<<": ";
    for(i=1;i<50000;i++){
      add(i*n);
      if(check()){
        cout<<(i*n)<<endl;
        insomnia=false;
        break;
      }
    }
    if(insomnia){
      cout<<"INSOMNIA"<<endl;
    }
    testCases--;
  }
}
