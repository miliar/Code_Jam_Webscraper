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

using namespace std;

#define FOR(i,n) for (int i=0; i<n; ++i)
#define FORE(i,n) for (int i=0; i<=n; ++i)
#define REP(i,a,b) for (int i=a; i<b; ++i)
#define REPE(i,a,b) for (int i=a; i<=b; ++i)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define mp make_pair
#define INF (1e9)

typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef long long int LL;
typedef vector<int> VI;
typedef vector<bool> VB;
typedef vector<VI> VVI;
const double pi = acos(-1.0);
const int inf =(int) 1e9;

const double eps = 1e-4;
const int ss=(int)1e6+3;
const int base=inf;

bool pred (const pair<int,int>& i, const pair<int,int>& j) 
{
    if (i.first==j.first)
        return i.second>j.second;
    else
        return i.first>j.first;
}

//LL out[] = {1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404,10000200001,10221412201,12102420121,12345654321,40000800004,1000002000001,1002003002001,1004006004001,1020304030201,1022325232201,1024348434201,1210024200121,1212225222121,1214428244121,1232346432321,1234567654321,4000008000004,4004009004004};

int main()
{
#ifdef _DEBUG
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
#else
	//freopen("island2.in","r",stdin);
   //freopen("island2.out","w",stdout);
#endif
	int t;
	scanf("%d",&t);
	FOR(t1,t)
	{
		int n,m;
		scanf("%d%d",&n,&m);
		VVI a(n,VI(m));
		int kol = 0;
		FOR(i,n) {
			FOR(j,m) {
				scanf("%d",&a[i][j]);
				if (a[i][j] == 1)
					++kol;
			}
		}
		int now = 0;
		vector<VB> b(n,VB(m));
		FOR(i,n) {
			bool check = false;
			if (a[i][0] == 1) {
				check = true;
				FOR(j,m) {
					if (a[i][j]==2)
					{
						check = false;
						break;
					}
				}
			}
			if (check)
			{
				FOR(j,m) {
					if (b[i][j]==false)
					{
						b[i][j] = true;
						++now;
					}
				}
			}
		}
		FOR(i,m) {
			bool check = false;
			if (a[0][i] == 1) {
				check = true;
				FOR(j,n) {
					if (a[j][i]==2)
					{
						check = false;
						break;
					}
				}
			}
			if (check)
			{
				FOR(j,n) {
					if (b[j][i]==false)
					{
						b[j][i] = true;
						++now;
					}
				}
			}
		}
		if (now == kol) {
			printf("Case #%d: YES\n",t1+1);
		} else {
			printf("Case #%d: NO\n",t1+1);
		}
	}
#ifdef _DEBUG
    fprintf(stderr, "Time: %.2lf sec\n", (clock()*1./CLOCKS_PER_SEC));
#endif
    return 0;
}

