#include<bits/stdc++.h>
#define ll long long
using namespace std;
int fast(int base, int exp ,int mod ){
  int res = 1;
  while(exp){
    if(exp & 1)
    res = (res * base)%mod;
    exp = exp >> 1;
    base = (base * base)%mod;
  }
  return res;
}
int main(){
    int N , J , T ;
    cin  >> T >> N >> J;
   // ofstream cout("b.txt");
    cout << "Case #1:" << endl;
    int sz = min(N - 2 , 16);
     for(int i = 1 ; i < (1<<sz) && J ; ++i ){
          int flag = 0;
          int hsh[11];
        for(int base = 2 ; base <= 10 ; ++base ){
          for(int k = 2 ; k <= 100 ; ++k ){
           int rem = (fast(base,N-1,k)+1)%k;
          for(int j = 0 ; j < sz ; ++j ){
            if((1<<j) & i)
            rem = (rem + fast(base,j+1,k))%k;
          }
          if(rem == 0){
          hsh[base] = k;
          flag++;
          break;
          }
        }
        if(flag != (base - 1))
         break;
        }
        if(flag == 9 ){
          --J;
         string x;
         x = '1';
         for(int j = sz ; j >= 1 ; --j ){
           if((1<<(j-1)) & i )
           x += '1';
           else
           x += '0';
         }
         x += '1';
          cout << x << " ";
          for(int i = 2 ; i <= 10 ; ++i )
          cout << hsh[i] <<" ";
          cout << endl;
        }
     }
}
