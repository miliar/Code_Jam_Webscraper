#include<stdio.h>
#include<sstream>
#include<algorithm>
#include<map>
#include<string>

using namespace std;

int A[200];
int N,K;
double prob[202];
int selected[201];

double eval() {
  for(int z=0;z<=N;z++) prob[z] = 0;
  prob[0] = 1;
  for(int i=0;i<N;i++) {
    if(!selected[i]) continue;
    double p = A[i]*0.01, cur = 0, nex;
    for(int z=0;z<=N;z++) {
      nex = prob[z];
      prob[z] = p * cur + (1-p) * prob[z];
      cur = nex;
    }
  }
  return prob[ K / 2 ];
}

void solve(int T) {
  
  scanf("%d %d\n",&N,&K);
  double mx = 0;
  for(int i=0;i<N;i++) {
    double x;
    scanf("%lf",&x);
    A[i] = (int)(x*100+0.5);
  }
  for(int i=0;i<(1<<N);i++) {
    int cnt = 0;
    for(int j=0;j<N;j++) {
      if( (i>>j)&1 ) cnt++;
      selected[j] = (i>>j)&1;
    }
    if(cnt == K) {
      double v = eval();
      if(v > mx) mx = v;
    }
  }
  
  printf("Case #%d: %lf\n",T,mx);
}

int main() {
  int t,T;
  //freopen("/Users/sushi/Downloads/C-small-attempt1.in","r",stdin);
  scanf("%d",&T);
  for(t=1;t<=T;t++) solve(t);
  return 0;
}
