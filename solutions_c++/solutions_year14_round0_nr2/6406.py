#include<cstdio>
#include<cstdlib>
#include<ctime>
#include<cmath>
#include<cstring>
#include<cctype>
#include<complex>
#include<iostream>
#include<sstream>
#include<algorithm>
#include<functional>
#include<vector>
#include<string>
#include<stack>
#include<queue>
#include<map>
#include<set>
#include<bitset>
#include<numeric>
using namespace std;
const int dx[] = {-1,0,1,0};
const int dy[] = {0,-1,0,1};
#define INF 1e+8
#define EPS 1e-7
#define PB push_back
#define fi first
#define se second
#define ll long long 
#define reps(i,j,k) for(int i = (j); i < (k); i++)
#define rep(i,j) reps(i,0,j)
typedef pair<int,int> Pii;
typedef vector<int> vi;
int main(){
	int T;
	scanf("%d",&T);
	rep(t,T){
		double c,f,x;
		double ans = 100000000000.0;
		vector < double > Min;
		scanf("%lf%lf%lf",&c,&f,&x);
		double v = 2.0;
		rep(i,1000000){
			if(c/v <= EPS)break;
			Min.PB(c/v);
			v+=f;
		}
		partial_sum(Min.begin(),Min.end(),Min.begin());
		ans = x/2.0;
		rep(i,Min.size()){
			double tmp = 2.0+(i+1)*f;

			ans = min(Min[i]+x/tmp,ans);
		}
		printf("Case #%d: %.7lf\n",t+1,ans);
	}
	return 0;
}