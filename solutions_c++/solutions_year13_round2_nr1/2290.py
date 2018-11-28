/*
 this code was written by Zanaty
 problem kind:
 */
#include<iostream>
#include<string.h>
#include<vector>
#include<stack>
#include<queue>
#include<algorithm>
#include<stdio.h>
#include<set> 
#include<cmath>
#include<fstream>
#include<memory.h>
#include<map>
#include<sstream>
#include<climits>
#include<numeric>/*
#include <ext/hash_set>
#include <ext/hash_map>
using namespace __gnu_cxx;
*/
using namespace std;

#define rep(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define reps(i,x,n) for((i)=(x);(i)<(int)(n);(i)++)
#define repi(i,n) for((i)=(n)-1;(i)>=0;(i)--)
#define SZ(v) (int)v.size()
#define LEN(s) (int)s.length()
#define mp(x,y) make_pair(x,y)
#define all(v) (v).begin(),(v).end()
#define rall(v) (v).rbegin(),(v).rend()

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> pii;
typedef vector<pii> vii;
typedef long long ll;

#define EPS 1e-4
#define INF (int)10e8
#define MAX (int) 1000

int main() {
#ifndef ONLINE_JUDGE
	freopen("test.txt", "r", stdin);
	freopen("out.txt","w",stdout);
#endif

	int test, tt = 1;
	scanf("%d", &test);
	while (test--) {

		int n, sz;
		scanf("%d%d", &sz, &n);

		vi motes(n);

		int i;
		rep(i,n)
			scanf("%d", &motes[i]);

		sort(all(motes));

		int res = 0;

		rep(i,SZ(motes)) {

//    		cout<<"sz: "<<sz<<" "<<motes[i]<<endl;
			if (sz > motes[i]) {
				sz += motes[i];
			} else {
				int rem = SZ(motes) - i;

//    			cout<<"here  "<<rem<<endl;

				int tsz = sz;
				int steps = 0;

				while (tsz <= motes[i]) {


//					cout<<"otz  "<<tsz<<endl;
					tsz += tsz - 1;

//					cout<<"ntz  "<<tsz<<endl;

					steps++;
					if (steps > rem) {
						res += rem;
						goto SOL;

					}
				}

				sz = tsz + motes[i];
				res += steps;
			}

		}

		SOL:
		printf("Case #%d: %d\n",tt++,res);

	}

	return 0;
}
