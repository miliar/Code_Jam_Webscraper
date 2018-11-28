#define _CRT_SECURE_NO_WARNINGS
#pragma comment (linker, "/STACK:16777216")
#include <algorithm>
#include <numeric>
#include <string>
#include <string.h>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <iostream>
#include <fstream>
#include <cmath>
#include <math.h>
#include <iomanip>
#include <stdlib.h>
#include <time.h>
#include <sstream>
#include <stdio.h>
#include <stack>
#include <time.h>

using namespace std;

#define FOR(i,n) for (int i=0; i<n; ++i)
#define FORE(i,n) for (int i=0; i<=n; ++i)
#define REP(i,a,b) for (int i=a; i<b; ++i)
#define REPE(i,a,b) for (int i=a; i<=b; ++i)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define mp make_pair
#define pb push_back
#define INF (1e9)

typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef long long int LL;
typedef vector<int> VI;
typedef vector<bool> VB; 
typedef vector<VI> VVI;
const long double pi = 3.14159265358979323846;
const int inf = (int)1e9;

const LL base=inf;

bool pred (const string& i, const string& j)
{
    return i.size()<j.size();
}

double go() {
	double c,f,x;
	cin >> c >> f >> x;
	double res = x / 2.0;
	double p = 2.0;
	double prev = 0;
	while(true) {
		double now = prev + c / p + x / (f + p);
		if (now > res) {
			break;
		}
		res = now;
		prev += c / p;
		p += f;
	}
	return res;
}

int main(){
#ifdef _DEBUG
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
#else
   // freopen("input.txt","r",stdin);
    //freopen("output.txt","w",stdout);
#endif  
	int t;
	cin >> t;
	FOR(tt,t) {
		cout << "Case #" << tt + 1 << ": ";
		cout << fixed << setprecision(9) << go() << "\n";
	}
    return 0;
}