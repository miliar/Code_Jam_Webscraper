#include <cstdio>
#include <vector>
#include <utility>
#include <cstring>
#include <cstdlib>
#include <map>
#include <iostream>
#include <algorithm>
#include <string>
#include <stack>
#include <queue>
#include <cmath>
#include <set>
#include <assert.h>
#include <bitset>
#include <climits>
#include <sstream>

using namespace std;
#define pb push_back
#define mp make_pair
#define S second
#define F first
#define INF 0x3f3f3f3f
#define ll long long
#define mod 10
#define B 33
#define MAX 100011
#define eps 1e-7
#define ull unsigned long long

double pi = acos(-1);

typedef vector<int> vi;
typedef pair<int,int>ii;
typedef vector<ii> vii;

int main() {
	int n;
	double r,c,x,f,t;
	cin >> n;
	for (int i = 0; i < n; ++i)
	{
		cin >> c >> f >> x;
		t = 0;
		r = 2;
		while((c/r)+(x/(r+f)) < x/r){
			t+=c/r;
			r+=f;
		}
		printf("Case #%d: %.7lf\n", i+1, t+ x/r);
	}
	return 0;
}