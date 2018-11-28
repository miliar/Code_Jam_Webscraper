#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdlib>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <set>
#include <queue>
#include <deque>
#include <map>
#include <stack>
#include <string>
#include <sstream>
#include <vector>
#include <ctime>
#include <cstring>

#define ll long long
#define ld long double
#define vi vector<int>
#define vvi vector<vi >
#define pii pair<int,int>
#define pll pair<ll,ll>
#define vpii vector<pii >
#define vb vector<bool>
#define min(x,y) (x < y ? x : y)
#define min3(x,y,z) (min(x,min(y,z)))
#define max(x,y) (x > y ? x : y)
#define max3(x,y,z) (max(x,max(y,z)))
#define forn(i,n) for(int i = 0;i < n;i++)
#define sqrt(x) (pow(x,0.5))
#define sqr(x) (x * x)
#define mp make_pair
#define STDFILE 1
#define TASKNAME "xx"

const int inf = 1000 * 1000 * 1000;
const int mod = 1000 * 1000 * 1000 + 7;
const ld eps = 1e-9;

using namespace std;

int main(){
	freopen("INPUT.TXT","r",stdin);
	freopen("OUTPUT.TXT","w",stdout);
	int t;
	cin >> t;
	forn(i,t){
		cout << "Case #" << (i + 1) << ": ";
		cout.precision(20);
		double c,f,x;
		cin >> c >> f >> x;
		double ans = 0;
		double ftime = 0;
		double eftime = x / 2;
		double cv = 2;
		double min = x / 2;
		forn(i,1e5){
			ftime += (c / cv);
			eftime = ftime + x / (cv + f);
			if(eftime <= min)
				min = eftime;
			cv += f;
		}
		cout << min << endl;
	}
	return 0;
}