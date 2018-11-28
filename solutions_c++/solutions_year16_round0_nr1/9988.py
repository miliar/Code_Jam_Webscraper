#include <iostream>
#include <string>
#include <algorithm>
#include <list>
#include <stdio.h>
#include <vector>
#include <stack>
#include <queue>
#include <bitset>
#include <set>
#include <cmath>
#include <map>
#include <string.h>
#include <cassert>

using namespace std;


#define ALL(v)  v.begin(), v.end()
#define SZ(v)   ((int)(v.size()))
#define ALLR(v) v.rbegin(), v.rend()
#define pii pair<int,int>
#define pb push_back
#define Int long long
#define ull unsigned long long
#define mp make_pair
#define For(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)

inline void end(string s){cout << s; exit(0);}
inline void end(Int n){cout << n; exit(0);}

Int mod(Int a, Int b) {
	return (((a % b) + b) % b);
}
const double PI = acos(-1);

const int N = 1e5 + 5;



int main(){
#ifndef ONLINE_JUDGE
	freopen("code.in","r", stdin);
	freopen("code.out","w", stdout);
#endif
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; ++i)
	{
		set<int> s;
		int n;
		scanf("%d", &n);

		if (!n) {
			printf("Case #%d: INSOMNIA\n", i+1);
			continue;
		}

		ull rep = 1;
		while(s.size() < 10) {
			ull num = n * rep++;
			while(num > 0 && s.size() < 10) {
				s.insert(num%10);
				num /= 10;
			}
		}

		printf("Case #%d: %lld\n", i+1, n * --rep);

	}
	return 0;
}