#include<iostream>
#include<cstdio>
#include<vector>
#include<string>
#include<map>
#include<set>
#include<algorithm>
using namespace std;

double clac_prob(vector<double> &P){
  int flag = 0;
  double prob[300][2] = {0};
  prob[0][0] = 1;
  int K = P.size();
  for(int i = 0; i < K;i++){
    flag = 1-flag;
    prob[0][flag] = prob[0][1-flag] * (1-P[i]);
    for(int j = 1; j <=K;j++){
      prob[j][flag] = prob[j][1-flag] *(1-P[i]) + prob[j-1][1-flag] *P[i];
    }
  }
  return prob[K/2][flag];
}
void work()
{
  int N, K;
  double P[300];
  double res= 0;
  scanf("%d%d", &N, &K);
  for(int i = 0; i < N; i++)
    scanf("%lf", &P[i]);
  sort(P, P+N);
  for(int i = 0; i <=K;i++){
    vector<double> p;
    for(int j = 0; j <i; j++)
      p.push_back(P[j]);
    for(int j = i; j<K;j++)
      p.push_back(P[N-(j-i)-1]);
    //cout << p.size() << endl;
    //cout << res << endl;
    res = max(res, clac_prob(p));
  }

  printf("%lf\n", res);
}
int main()
{
  int T;
  scanf("%d",&T);
  for(int i =1; i <=T; i++){
    printf("Case #%d: ", i);
    work();
  }
}
