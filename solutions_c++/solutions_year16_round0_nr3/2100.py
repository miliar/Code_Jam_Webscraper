#include<iostream>
#include<string>
#include<vector>
#include<boost/multiprecision/cpp_int.hpp>
#include<boost/random.hpp>
#include<random>
using namespace std;
namespace mp = boost::multiprecision;

typedef struct hoge{
  mp::cpp_int coin;
  mp::cpp_int base[11];
  hoge(){};
}hoge;

int main(){
  int n;
  cin >> n;
  int len,j;
  //input
  for(int i=0;i<n;i++){
    cin >> len >> j;
  }
  vector<hoge> ans(j);

  std::mt19937 engine;
  std::uniform_int_distribution<long long> distribution(1,1LL<<(len-2)-1);
  int cnt=0;
  for(long long i=0;i<1LL<<(len-2) && cnt<j;i++){

    i=distribution(engine);
    cerr<< i<<endl;
    long long coin2=(1LL<<(len-1))+1+(i<<1);
    mp::cpp_int coin10 =0;
    mp::cpp_int buf[11] ={};
    for(int base=2;base<=10;base++){
      mp::cpp_int x =0;
      mp::cpp_int y =1;
      long long cp = coin2;

      while(cp){
        x+=(cp%2)*y;
        y*=base;
        cp/=2;
      }
      if(base==10) coin10= x;
     // cerr<<coin10<<endl;

      for(mp::cpp_int k=2;k*k<x&&k<10000;k++){
        if(x%k==0){
          buf[base]=k;
          break;
        }
      }
      if(buf[base]==0)break;
    }
    for(int base = 2; base<=10;base++){
      if(buf[base]==0)break;
      if(base<10)continue;
      ans[cnt].coin=coin10;
      for(int i=0;i<11;i++){
        ans[cnt].base[i]=buf[i];
      }
      //cerr<<cnt <<endl;
        cnt++;
    }
  }
  //output
  for(int i=0;i<n;i++){
    cout<<"Case #"<<(i+1)<<": ";
    for(auto it:ans){
      cout<< it.coin;
      for(int base=2;base<11;base++)
        cout<<" "<<it.base[base];
      cout<<endl;
    }
  }
}
