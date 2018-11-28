#include<iostream>
#include<cmath>
using namespace std;

#include<fstream>
ifstream fin ("C-large-1.in");
ofstream fout ("out.txt");
#define cin fin 
#define cout fout

#define LL long long
LL arr[10000004];

bool check_pali (LL num){
  LL num_ = 0;
  LL num__ = num;

  while (num>0){
    num_ = (num_ * 10) + num%10;
    num/=10;
  }
  if (num_ == num__)return 1;
  else return 0;
}

int main (){
  int t;
  cin>>t;
  arr[0] = 0;
  for (LL i=1;i<10000004;++i){
    if ((check_pali(i) == 1) && (check_pali(i*i) == 1)){arr[i] = arr[i-1] + 1;}
    else arr[i] = arr[i-1];
  }

  for (int num_t=0;num_t<t;++num_t){
    LL a, b;cin>>a>>b;
    int a_ =(int) ceil (sqrt(a));
    int b_ =(int)  floor (sqrt(b));
    cout<<"Case #"<<num_t + 1<<": "<<arr[b_] - arr[a_-1]<<"\n";
  }

  return 0;
}
