#include <iostream>
#include <cstdio>
#include <iomanip>
#include <cmath>
#include <complex>
#include <numeric>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <cstring>
#include <cstdlib>
#include <algorithm>

using namespace std;
#define FOR(i,m,n) for(int i = (m); i < (n); i++)
#define ROF(i,m,n) for(int i = (n)-1; i >= (m); i--)
#define foreach(x,i) for( __typeof((x).begin()) i = (x).begin(); i != (x).end(); i++)
typedef long long LL;
typedef unsigned long long uLL;
typedef vector<int> VI;
typedef vector<LL> VLL;
#define SZ(x) ((int)(x).size())
typedef pair<int,int> pii;
typedef pair<LL,LL> pll;
#define FR first
#define SC second

const int Gmax = 10000+10;
int n;
int a[Gmax];

int main(){
	ios_base::sync_with_stdio(false);
	int T;
	cin >> T;
	FOR(x,0,T){
		cin >> n;
		FOR(i,0,n)
			cin >> a[i];
//		while(n > 1 && a[n-1] >= a[n-2])
//			n--;
		int y = 0, z = 0;
		int speed = 0;
		FOR(i,0,n-1){
			y += max(0,a[i]-a[i+1]);
			speed = max(speed, a[i]-a[i+1]);
		}
		int rem = a[0];
		FOR(i,1,n){
			z += min(rem, speed);
			rem = max(a[i], rem-speed);
		}

		cout << "Case #" << x+1 << ": " << y << ' ' << z << '\n';

	}

	return 0;
}
