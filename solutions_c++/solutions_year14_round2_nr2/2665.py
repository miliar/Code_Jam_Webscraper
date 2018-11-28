#include <iostream>
#include <cstdio>
using namespace std;

int main(){
  unsigned long long int a, b, k, nCase;
  cin >> nCase;
  for (int c = 1; c <= nCase; c++){
    unsigned long long res = 0;
    cin>>a>>b>>k;
    for(int i = 0; i<a; i++){
      for (int j= 0; j<b; j++){
        if((i&j) < k)
          res++;
      }
    }
    cout<<"Case #"<<c<<": "<<res<<endl;
  }
}