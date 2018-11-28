#include <stdio.h>
#include <functional>
#include <bitset>
#include <math.h>
#include <time.h>
#include <stdlib.h>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <sstream>
#include <queue>
#include <string.h>
#include <numeric>
#include <iomanip>
#include <stack>
#include <assert.h>
using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> ii;
typedef long long ll;
#define sz(a) int((a).size())
#define pb push_back
#define mp make_pair
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(typeof((c).begin() i = (c).begin(); i != (c).end(); i++)
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())

int main() {
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int TC;
	cin >> TC;
	int CC=1;

	while (TC--)
	{
		int N;
		cin >> N;
		string s;
		cin >> s;
		int cnt = 0;
		int ret = 0;
		for (int i=0 ; i<sz(s) ; i++)
		{
			if (i > cnt) ret++ , cnt++;
			cnt += (s[i] - '0');
		}
		printf("Case #%d: %d\n",CC++,ret);
	}
}
