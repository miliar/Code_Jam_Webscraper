#include<coin/ClpSimplex.hpp>
#include<coin/CoinBuild.hpp>
#include<stdio.h>
#include<algorithm>
using namespace std;

int N;
double Vol,TempGoal;
double Rate[1000], Temp[1000];
int row2Index[1000];
double row2Value[1000];

void solve(int t) {
  scanf("%d %lf %lf",&N,&Vol,&TempGoal);
  int i,j,k, feasible = 0;
  for(i=0;i<N;i++) {
    scanf("%lf %lf",Rate+i,Temp+i);
    if(Temp[i] == TempGoal) feasible = 3;
    if(Temp[i] < TempGoal) feasible |= 1;
    if(Temp[i] > TempGoal) feasible |= 2;
  }
  if(feasible != 3) {
    printf("Case #%d: IMPOSSIBLE\n",t);
    return;
  }
  double ans;
  /*
  if(N<=2) {
    i = 0; j = min(1,N-1);
    if(Temp[i] > Temp[j]) {
      k = i; i = j; j = k;
    }
    if(Temp[i] == Temp[j]) {
      ans = min(Vol /  Rate[j], Vol /  Rate[i]);
      if(N>1) ans = -1;
    } else {
      double x = (TempGoal - Temp[i]) / (Temp[j]-Temp[i]);
      double y = 1-x;
      ans = max(Vol * x /  Rate[j], Vol * y /  Rate[i]);
    }
    printf("Case #%d: %.9lf\n",t,ans);
  }
  */
  ClpSimplex model;

  model.setDualTolerance(1e-12);
  model.setPrimalTolerance(1e-12);
  //printf("%.9lf\n",model.primalTolerance());
  model.setLogLevel(0);
  model.setOptimizationDirection(1);

  model.resize(0, N+1);

  model.setObjectiveCoefficient(N, 1);
  
  for(i=0;i<=N;i++) model.setColumnLower(i, 0.0);
  
  CoinBuild buildObject;
  
  for(i=0;i<N;i++) {
    row2Index[i] = i;
    row2Value[i] = 1;
  }
  buildObject.addRow(N, row2Index, row2Value, 1, 1);
  
  for(i=0;i<N;i++) {
    row2Index[i] = i;
    row2Value[i] = Temp[i];
  }
  buildObject.addRow(N, row2Index, row2Value, TempGoal, TempGoal);
  
  
  for(i=0;i<N;i++) {
    row2Index[0] = i;
    row2Value[0] = -Vol;
    row2Index[1] = N;
    row2Value[1] = Rate[i];
    buildObject.addRow(2, row2Index, row2Value, 0.0, COIN_DBL_MAX);
  }
  
  model.addRows(buildObject);
  model.primal();
  
  double total = model.objectiveValue();
  //if(ans > 0) if(total < ans - 1e-6 || total > ans + 1e-6) printf("------nequal--------\n");
  printf("Case #%d: %.9lf\n",t,total);
}

int main() {
  int t,T;
  //freopen("/Users/sushi/Downloads/C-small-attempt1.in","r",stdin);
  scanf("%d",&T);
  for(t=1;t<=T;t++) solve(t);
  return 0;
}
