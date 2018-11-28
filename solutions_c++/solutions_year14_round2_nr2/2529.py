#include<iostream>
#include<algorithm>
#include<cstdio>

using namespace std;

int main() {
  int a,b,k;
  int T;
  cin>>T;
  for(int t=1;t<=T;++t) {
  cin>>a>>b>>k;
  long ans=0;
  for(int n=0;n<k;++n) {
  for(int i=0;i<a;++i) {
    for(int j=0;j<b;++j) {
      if((i&j)==n)
	ans++;
    }
  }
  }
  printf("Case #%d: %ld\n",t,ans);
  }
  return 0;
}
