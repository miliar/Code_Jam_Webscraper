#include <iostream>
#include <iomanip>
#include <fstream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <cassert>

#define FOR(i,n) for(int i=0,_n=n;i<_n;i++)
#define FORR(i,s,n) for(int i=s,_n=n;i<_n;i++)
#define mp make_pair
#define pb push_back
#define pii pair<int,int>
#define pli pair<ll,int>
#define vi vector<int>
#define fs first
#define sec second

#define maxn 100000
#define EPS 0.0000001

using namespace std;
typedef long long ll;

const ll MOD = 1000000007LL;

void solve(int zaporedna){
	int rez=0;
	int n;
	cin >> n;
	double v,x;
	cin >> v >> x;
	if(n>2)return;
	cout << fixed << setprecision(13);
	if(n==1){
		double rate, t;
		cin >> rate >> t;
		if(fabs(t-x)>EPS){
			printf("Case #%d: IMPOSSIBLE\n",zaporedna);
			return;
		}
		double cajt=v/rate;
		cout << "Case #" << zaporedna<<": "<<cajt<<"\n";
		return;
	}
	double r0,r1,x0,x1;
	cin >> r0 >> x0 >> r1 >> x1;
	if(x<min(x0,x1) || x>max(x0,x1)){
			printf("Case #%d: IMPOSSIBLE\n",zaporedna);
			return;
	}
	if(fabs(x0-x1)<EPS){
		cout << "Case #" << zaporedna<<": "<<v/(r0+r1)<<"\n";
		return;
	}
	double v1=(x*v-x0*v)/(x1-x0);
	double v0 = v-v1;
	double cajt = max(v1/r1,v0/r0);
	cout << "Case #" << zaporedna<<": "<<cajt<<"\n";
}

int main(){
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)solve(i);
	return 0;
}
