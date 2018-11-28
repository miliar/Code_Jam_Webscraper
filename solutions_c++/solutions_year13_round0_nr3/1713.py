#include <cstdio>
#include <string>
#include <memory.h>
#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
#include <set>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <stack>
#include <queue>
#include <iomanip>
 
using namespace std;
 
#define forn(i,n) for (int i = 0; i < int(n); i++)
#define pb push_back
#define mp make_pair

typedef long long li;
 
template <typename T> T sqr(const T &x) {
	return x * x;
}
                                    
const int INF = 1e9;                                      
const long double EPS = 1e-9;
const long double PI = acos(-1.0);
const int N = 20002;

set <li> good;

bool palindrom(li a){
	vector <int> d;
	while(a){
		d.pb(a % 10);
		a /= 10;
	}
	int n = d.size();
	forn(i, n / 2){
		if(d[i] != d[n - i - 1])
			return false;
	}
	return true;
}

void fr(){
	for(li i = 1; i <= 10000002; i++)
		if(palindrom(i) && palindrom(i * i))
			good.insert(i * i);
}
		
int main() {
	freopen("C-large-1.in", "rt", stdin);
	freopen("out.txt", "wt", stdout);
	fr();
	int t;
	scanf("%d", &t);
	forn(c, t){
		li a, b;
		cin>>a>>b;
		int ans = 0;
		for(set <li>::iterator it = good.begin(); it != good.end(); it++)
			if(*it >= a && *it <= b)
				ans++;
 		printf("Case #%d: %d\n", c + 1, ans);
	}	
   	return 0;
}