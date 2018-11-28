#ifdef ONLINE_JUDGE
#include <bits/stdc++.h>
#else
#include "header.h"
#endif

using namespace std;
typedef unsigned long long ll;
#define MOD 1000000007

int main( int argc, char** argv ){
int T;cin >> T;
for(int nc=1;nc<=T;nc++){
  int D;cin >> D;
  int P[D];
  for(int i =0;i<D;i++){
    cin >> P[i];
  }
  sort(P,P+D);
  int ans=P[D-1];
  for(int i=1;i<P[D-1];i++){
    int tmp=0;
    for(int j=0;(j<D) ;j++){
      if(P[j]<i)continue;
      tmp+=P[j]/i+(P[j] % i != 0)-1;

    }
    ans=min(ans,tmp+i);
  }

cout << "Case #"<<nc<<": "<<ans<<endl;
}
}
