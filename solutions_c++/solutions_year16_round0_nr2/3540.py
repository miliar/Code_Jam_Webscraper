#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <numeric>

using namespace std;

#define FOR(i, n) for(int i = 0; i < (n); ++i)
#define SIZEOF(a) (sizeof(a)/sizeof((a)[0]))

typedef long long ll;

const int MAX_N = 1e6+10;
int a[MAX_N];
int res;

const int BUFSIZE = 1000000;
char buf[BUFSIZE + 1];
string nextString() {
	scanf("%s", buf); return buf;
}

int SolveCase()
{
	string s; cin >> s;
	int cnt = 0;
	FOR(i,s.size()) if(i>0 && s[i-1]!=s[i]) cnt++;
	return cnt + (s.back()=='-' ? 1 : 0);
}

int main()
{
	//test();return 0;
	int t; cin >> t;
	FOR(i,t){
		cout << "Case #" << i+1 << ": ";
		const int r = SolveCase();
		cout << r;
		cout << endl;
	}
	return 0;
}
