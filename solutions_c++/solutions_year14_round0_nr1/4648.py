/*
Abolfazl Kazemi

BSc in Software Engineering: IAUN Iran
MSc student of Software Engineering: IUST
UVA, topcoder, codeforces, facebook account: AKJ88
*/

#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <climits>
#include <cstring>
#include <cmath>
#include <map>
#include <set>
#include <queue>
#include <functional>
#include <string>
#include <sstream>
#include <ctime>
#include <bitset>
#include <cstdlib>

using namespace std;

#define     For(i,a,b)        for (i=a; i<b; i++)
#define     FoR(i,a,b)        for (i=a; i<=b; i++)
#define     Rep(i,a)          for (i=0; i<a; i++)
#define     FIT(it,v)         for (it=(v).begin(); it!=(v).end(); ++it)
#define     ALL(v)            (v).begin(),(v).end()
#define     Set(a,x)          memset((a),(x),sizeof(a))
#define     EXIST(a,b)        find(ALL(a),(b))!=(a).end()
#define     Sort(x)           sort(ALL(x))
#define     UNIQUE(v)         Sort(v); (v).resize(unique(ALL(v)) - (v).begin())
#define     SF                scanf
#define     PF                printf

#define 	EPS  		1e-8
#define 	PI			acos(-1)
#define 	MAXN 		105
#define 	MOD 		1000000007
#define 	INF 		1000000000
#define 	X 			first
#define 	Y 			second

typedef pair<int, int> ii;
typedef pair<double, double> dd;
typedef long long ll;
typedef unsigned long long llu;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<dd> vdd;


int main(){
	int tc, Case = 1, r, i, j, k, num;
	set<int> s[2];
	vi::iterator it;
#ifndef ONLINE_JUDGE
	freopen("C:\\acm_inp\\cj\\A-small-attempt0.in", "r", stdin);
	freopen("C:\\acm_inp\\cj\\A-small-attempt0.OUT", "w", stdout);
#endif

	SF("%d", &tc);
	while (tc--){
		Rep(k, 2){
			SF("%d", &r), r--;
			s[k].clear();
			Rep(i, 4){
				Rep(j, 4){
					SF("%d", &num);
					if (i == r)
						s[k].insert(num);
				}
			}
		}
		vi res(4);
		it = set_intersection(s[0].begin(), s[0].end(), s[1].begin(), s[1].end(), res.begin());
		res.resize(it-res.begin());
		PF("Case #%d: ", Case++);
		if (res.size() == 1)
			PF("%d\n", *res.begin());
		else if (res.size() > 1)
			PF("Bad magician!\n");
		else
			PF("Volunteer cheated!\n");
	}

	return 0;
}













