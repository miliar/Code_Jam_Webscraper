#include <cstdio>
#include <iostream>
#include <vector>
#include <list>
#include <queue>
#include <map>
#include <set>
#include <utility>
#include <functional>
#include <string>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
typedef map<int,int> mii;
typedef vector<int> vi;
typedef vector< vector<int> > vvi;
typedef vector<string> vs;

#define rep(i,n) for(int i=0;i<(n);i++)
#define forup(i,a,b) for(int i=(a);i<(b);i++)
#define fordn(i,a,b) for(int i=(a);i>(b);i--)
#define all(x) x.begin(),x.end()
#define permute(x) next_permutation(all(x))
#define gi(x) scanf("%d",&x)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second

int T;
double c,f,x,rate;

int main() {
	gi(T);
	rep(z,T) {
		cin>>c>>f>>x;
		rate=2.0;
		double ans=0.0;
		while(true) {
			double t1=c/rate + x/(rate+f);
			double t2=x/rate;
			if(t2>t1) {
				ans+=c/rate;
				rate+=f;
			}
			else {
				ans+=t2;
				break;
			}
		}
		printf("Case #%d: %.9lf\n",z+1,ans);
	}
	return 0;
}
