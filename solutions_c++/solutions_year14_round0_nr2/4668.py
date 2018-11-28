#pragma warning (disable: 4530) 
#include<map>
#include<set>
#include<list>
#include<cmath>
#include<queue>
#include<stack>
#include<cstdio>
#include<string>
#include<vector>
#include<complex>
#include<cstdlib>
#include<cstring>
#include<numeric>
#include<sstream>
#include<iostream>
#include<algorithm>
#include<functional>
#include<climits>


#define mp       make_pair
#define pb       push_back
#define all(x)   (x).begin(),(x).end()
#define rep(i,n) for(int i=0;i<(n);i++)
 
using namespace std;
 
typedef    long long          ll;
typedef    unsigned long long ull;
typedef    vector<bool>       vb;
typedef    vector<int>        vi;

typedef    vector<vb>         vvb;
typedef    vector<vi>         vvi;
typedef    pair<int,int>      pii;
 
const int INF=1<<29;
const double EPS=1e-9;
 
const int dx[]={1,0,-1,0},dy[]={0,-1,0,1};//right down left up

double C,F,X;
double FactTime(int num){
  double res = 0.0;
  for(int n = 0; n < num; n++){
    double per = 2.0 + F * n;
    double sec = C / per;
    res += sec;
  }
  return res;
}
int main(){
  int T; scanf("%d",&T);
  for(int t = 0; t < T; t++){
    cin>>C>>F>>X;
    int Max = (int)(X / C) + 1;
    double res = INF;
    for(int i = 0; i <= Max; i++){
      double FT = FactTime(i);
      double per = 2.0 + F * i;
      double rest = X / per;
      double sum = FT + rest;
      res = min(res,sum);
    }
    printf("Case #%d: %.7f\n",t + 1,res);
  }
  return 0;
}
