#include<iostream>

using namespace std;

void fillDigitsInNum(int num[], long long numGen){
  int remainder = 1;
  while(numGen != 0){
    remainder = numGen%10;
    num[remainder] = remainder;
    numGen = numGen / 10;
  }
}

long long findDigits(long long n){
  int num[10] = {-1,-1,-1,-1,-1,-1,-1,-1,-1,-1};
  // cout<<" \n n : "<<n <<"\n";
  // for(int _in = 0 ; _in < 10 ; _in++){
  //   cout<<num[_in]<<" ";
  // }
  long long i = 1;
  while(i <= 10000000){
    long long numGen = i*n;
    fillDigitsInNum(num, numGen);
    int isFull = 1;
    for(int index = 0 ; index < 10 ; index++){
      if(num[index] != index){
        isFull = 0;
      }
    }
    if(isFull == 1){
      // cout<<"\n";
      // for(int _in = 0 ; _in < 10 ; _in++){
      //   cout<<num[_in]<<" ";
      // }
      return numGen;
    }
    i++;
  }
  return -1;

}


int main(){
  long t;
  cin>>t;
  long _case = 0;
  while(t--){
    _case++;
    long long n;
    cin>>n;
    if(n == 0){
      cout<<"Case #"<<_case<<": "<<"INSOMNIA"<<"\n";
    }
    else{
      long long lastNum = findDigits(n);
      if(lastNum == -1){
        cout<<"Case #"<<_case<<": "<<"INSOMNIA"<<"\n";
      }
      else{
        cout<<"Case #"<<_case<<": "<<lastNum<<"\n";
      }
    }

  }
  return 0;
}
