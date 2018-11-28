#include <iostream>

using namespace std;

int main() {
  unsigned long A, B, K, T, count, r, p;

  cin>>T;

  p = 1;
  while(T--) {
    cin>>A>>B>>K;
    count = 0;
    
    for(int i = 0; i < A; i++)
      for(int j = 0; j < B; j++){
	r = i & j;
	if(r < K) {
	  // cout<<i<<" "<<j<<endl;
	  count++;
	}
      }
    cout<<"Case #"<<p<<": "<<count<<endl;
    p++;
  }

  return 0;
}
