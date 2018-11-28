#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
#include<map>
#include<set>
#include<string>
#include<stack>
#include<cstdio>
#include<cmath>
using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int,int> P;
typedef pair<int,P> P1;

#define fr first
#define sc second
#define mp make_pair
#define pb push_back
#define rep(i,x) for(int i=0;i<x;i++)
#define rep1(i,x) for(int i=1;i<=x;i++)
#define rrep(i,x) for(int i=x-1;i>=0;i--)
#define rrep1(i,x) for(int i=x;i>0;i--)
#define sor(v) sort(v.begin(),v.end())
#define rev(s) reverse(s.begin(),s.end())
#define lb(vec,a) lower_bound(vec.begin(),vec.end(),a)
#define ub(vec,a) upper_bound(vec.begin(),vec.end(),a)
#define uniq(vec) vec.erase(unique(vec.begin(),vec.end()),vec.end())
#define mp1(a,b,c) P1(a,P(b,c))

const int INF=1000000000;
const int dir_4[4][2]={{1,0},{0,1},{-1,0},{0,-1}};
const int dir_8[8][2]={{1,0},{1,1},{0,1},{-1,1},{-1,0},{-1,-1},{0,-1},{1,-1}};

int main(){
	int T;
	cin >> T;
	rep1(ppp,T){
		printf("Case #%d: ",ppp);
		int n,k;
		int sum[1002];
		scanf("%d%d",&n,&k);
		rep(i,n-k+1){
			scanf("%d",&sum[i]);
		}
		int x[1002] = {};
		for(int i = 0 ; i+k < n ; i ++){
			x[i+k] = x[i] + sum[i+1] - sum[i];
		}
		int l[1002] = {} , r[1002] = {};
		for(int i = 0 ; i < k ; i ++){
			for(int j = i ; j < n ; j += k){
				l[i] = min ( l[i] , x[j] );
				r[i] = max ( r[i] , x[j] );
			}
		}
		int MIN = 0 , MAX = 0;
		rep(i,k){
			MIN = min ( MIN , l[i] );
			MAX = max ( MAX , r[i]-l[i] );
		}
		int cnt = sum[0];
		rep(i,k){
			cnt += l[i]-MIN;
		}
		while(cnt < k)cnt += k*100000;
		cnt %= k;
		int ret = 0;
		rep(i,k){
			ret += MAX-(r[i]-l[i]);
		}
		if(ret >= cnt)printf("%d\n",MAX);
		else printf("%d\n",MAX+1);
	}
}
		

