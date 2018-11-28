#include <stdio.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <map>
#include <set>
#include <cmath>
#include <sstream>
#include <stack>
#include <string.h>
#include <list>
#include <time.h>

#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define PI 3.14159265358979
#define forn(i, n) for(int i = 0; i < n; ++i)
#define ALL(x) x.begin(), x.end()
#define L(s) (int)((s).size())
#define sz(s) (int)((s).size())
#define ms(x) memset(x,0,sizeof(x))
#define ms1(x) memset(x,-1,sizeof(x))
#define del(y,x) erase(y.begin()+x)

typedef long long ll;
using namespace std;
typedef pair<int,int> pii;
const int INF = 2147483647;
const ll LLINF = 9223372036854775807LL;
const int ST = 100010;
const int ST1 = 1000010;
const ll MOD = 1000000007;

ll ABS(ll a) {
    if(a<0)
        return a*(-1);
    else
        return a;
}

string to_s(ll c)
{
	string s = "";
	while(c)
	{
		ll ch = c % 10;
		c/=10;
		s+=ch;
	}
	return s;
}
int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	int T;
	cin >> T;
	int test = 1;
	while(T--)
	{
		ll n;
		cin >> n;
		set<int> was;
		for(int i = 0;i < 10;i++)
			was.insert(i);
		printf("Case #%d: ",test++);
		if(n==0)
		{
			cout << "INSOMNIA" << endl;
		}else
		{
			ll found = 0;
			for(ll i = 1;i <=1000;i++)
			{
				string todel = to_s(n * i);
				for(int j = 0;j < L(todel);j++)
				{
					int cc = todel[j];
					was.erase(cc);
				}
				if(L(was)==0)
				{
					found = n * i;
					break;
				}
			}
			if(found == 0)
			{
				cout << "INSOMNIA" << endl;
			}
			else
			{
				cout << found << endl;
			}
			
		}
	}

    return 0;
}