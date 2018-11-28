//#pragma comment(linker, "/STACK:134217728")

#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <vector>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <numeric>
using namespace std;

typedef pair<int,int> PII;
typedef vector<int> VI;

#define FOR(i, a, b) for(int i = (a); i < (b); ++i)
#define RFOR(i, a, b) for(int i = (a) - 1; i >= (b); --i)
#define CLEAR(a, b) memset(a, b, sizeof(a))
#define ALL(a) (a).begin(),(a).end()
#define PB push_back
#define MP make_pair
#define MOD 1000000007

int m,n,k;
int t;
char ch[1000007];
string s;
string sol;

bool f(char x)
{
return (x=='a' || x=='e' || x=='i' || x=='o' || x=='u');
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int x,y;
	cin >> t;
	FOR(tests,0,t)
	{
		sol="";
		cin >> x >> y;

		if (x>0)
			FOR(i,0,x) sol+="WE";
		else FOR(i,0,-x) sol+="EW";

		if (y>0)
			FOR(i,0,y) sol+="SN";
		else FOR(i,0,-y) sol+="NS";


		cout << "Case #" << tests+1 << ": " << sol << endl;
	}

	return 0;
}


