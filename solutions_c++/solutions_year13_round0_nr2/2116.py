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
#include <assert.h>

#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define PI 3.14159265358979
#define forn(i, n) for(int i = 0; i < n; ++i)
#define ALL(x) x.begin(), x.end()
#define L(s) (int)((s).size())
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

ll ABS(ll a)
{
    if(a<0)
        return a*(-1);
    else
        return a;
}

int mas[110][110];
int main()
{
#ifdef _DEBUG
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
	int T;
	cin >> T;
	for(int test = 1;test<=T;test++)
	{
		int n,m;
		cin >> n >> m;
		for(int i = 0;i < n;i++){
			for(int j = 0;j < m;j++){
				cin >> mas[i][j];
			}
		}
		bool ans = true;
		for(int i = 0;i < n;i++){
			for(int j = 0;j < m;j++){
				bool can = true;
				int cur = mas[i][j];
				for(int w = 0;w < n;w++)
				{
					if(mas[w][j] > cur)
					{
						can = false;
						break;
					}
				}
				if(!can)
				{
					can = true;
					for(int w = 0;w < m;w++)
					{
						if(mas[i][w] > cur)
						{
							can = false;
							break;
						}
					}
					if(!can)
					{
						ans = false;
						break;
					}
				}
			}
		}

		printf("Case #%d: ",test);
		if(ans)
			cout << "YES" << endl;
		else
			cout << "NO" << endl;
	}


    return 0;
}