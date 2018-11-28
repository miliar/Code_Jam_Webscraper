#include <iostream>
#include <string>
#include <map>
#include <set>
#include <ctime>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <deque>
#include <fstream>
#include <queue>
#include <stack>
#include <vector>
#include <iomanip>
#include <cstdio>
#include <new>
#define mp make_pair
#define MATH_DEFINES
#define INF (long long)1e18
#define pb push_back
#define pf push_front
#define F first
#define S second
#define ll long long
#define MS0(a) memset((a),0,sizeof(a))
#define MS1(a) memset((a),-1,sizeof(a))
#define fname ""
#define ed cout<<endl
#define sz size()
#define eps 1e-11
using namespace std;
const int N = 100500;
int t, n, need, now, cases;
string s;
int main()
{
//	ios_base::sync_with_stdio(0);cin.tie(NULL);
//	freopen(fname".in","r",stdin);
//	freopen(fname".out","w",stdout);
	cin >> t;
	while (t --)
	{
		++ cases;
		cin >> n >> s;
		now = 0;
		need = 0;
		now += s[0] - '0';
		for (int i = 1; i < s.size(); i ++)
		{
			if (now > i)
			{
				now += s[i] - '0';
			}
			else
			{
				need += i - now;
				now = i + s[i] - '0';
			}
		}
		printf("Case #%d: %d\n", cases, need);
	}
 	return 0;
}