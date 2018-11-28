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
	int i, j, k, tc, N, Case = 1, nsc, ksc;
	double m;
	set<double> s;
	set<double>::iterator it;
	vector<double> km, nm;
#ifndef ONLINE_JUDGE
	freopen("C:\\acm_inp\\cj\\D-large.in", "r", stdin);
	freopen("C:\\acm_inp\\cj\\D-large.OUT", "w", stdout);
#endif

	cin >> tc;
	while (tc--){
		cin >> N;
		Rep(i, N)
			cin >> m, nm.push_back(m);
		Rep(i, N)
			cin >> m, km.push_back(m), s.insert(m);
		Sort(nm), Sort(km);

		ksc = nsc = 0;
		Rep(i, N){
			it = s.lower_bound(nm[i]);
			if (it != s.end()){
				s.erase(it);
				ksc++;
			}
		}

		i = 0, j = N - 1, k = N - 1;
		while (k>=0){
			if (nm[j] < km[k])
				i++;
			else
				j--, nsc++;
			k--;
		}

		PF("Case #%d: %d %d\n", Case++, nsc, N - ksc);
		s.clear(), km.clear(), nm.clear();
	}

	return 0;
}













