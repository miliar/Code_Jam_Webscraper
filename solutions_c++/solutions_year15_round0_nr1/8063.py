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
#include <stack>

using namespace std;

#define     For(i,a,b)        for (i=a; i<b; i++)
#define     FoR(i,a,b)        for (i=a; i<=b; i++)
#define     Rep(i,a)          for (i=0; i<a; i++)
#define     FIT(it,v)         for (it=(v).begin(); it!=(v).end(); ++it)
#define     ALL(v)            (v).begin(),(v).end()
#define     Set(a,x)          memset((a),(x),sizeof(a))
#define     Sort(x)           sort(ALL(x))
#define     SF                scanf
#define     PF                printf

#define 	EPS  		1e-8
#define 	PI			acos(-1)
#define 	MAXN 		1005
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
	int ans = 0, t, curr, Case = 1, T, i, sm, v;
	string str;
#ifndef ONLINE_JUDGE
	freopen("c:\\acm_inp\\A-large.in", "r", stdin);
	freopen("C:\\acm_inp\\A-large.OUT", "w", stdout);
#endif

	cin >> T;
	while (T--){
		cin >> sm >> str;
		curr = ans = 0;
		FoR(i, 0, sm){
			v = str[i] - '0';
			if (v && i > curr){
				t = abs(curr - i);
				ans += t;
				curr += (v + t);
			}
			else if (v)
				curr += v;
		}
		PF("Case #%d: %d\n", Case++, ans);
	}

	return 0;
}










