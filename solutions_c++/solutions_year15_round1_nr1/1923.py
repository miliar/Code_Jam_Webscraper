#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
using namespace std;
int m[1001];
int main(){
  int T;
  cin >> T;
  for(int t=1;t<=T;++t){
    int n; cin >> n;
    for(int i=0;i<n;++i) cin >> m[i];
    int a=0;
    for(int i=0;i+1<n;++i) if(m[i]>m[i+1]) a+=m[i]-m[i+1];
    int b=0;
    double r=0.0;
    for(int i=0;i+1<n;++i) if(m[i]>m[i+1]) r=max(r,(m[i]-m[i+1])/10.0);
    for(int i=0;i+1<n;++i){
      b+=min(m[i],(int)(r*10));
    }
    printf("Case #%d: %d %d\n",t,a,b);
  }
  return 0;
}
