#include <algorithm>
#include <functional>
#include <numeric>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <sstream>
using namespace std;

#define LL long long
#define LD long double
#define PR pair<int,int>

#define For(i,n) for (i=0; i<int(n); i++)
#define ForR(i,n) for (i=int(n)-1; i>=0; i--)
#define Sz(s) int((s).size())
#define All(s) (s).begin(),(s).end()
#define Fill(s,v) memset(s,v,sizeof(s))
#define pb push_back
#define mp make_pair
#define x first
#define y second

template<typename T> T Abs(T x) { return(x < 0 ? -x : x); }
template<typename T> T Sqr(T x) { return(x*x); }

const int INF = (int)1e9;
const LD EPS = 1e-9;
const LD PI = acos(-1.0);

#define DEBUG 0

int main()
{
	FILE *fin;
	FILE *fout;
	//files
	freopen_s(&fin,"in.txt", "r", stdin);
	if (!DEBUG)
		freopen_s(&fout,"out.txt", "w", stdout);
	//vars
	int tt, TT;
	//testcase loop
	scanf_s("%d", &TT);
	For(tt, TT)
	{
		//init
		printf("Case #%d: ", tt + 1);
		//input
		set<int> have;
		have.clear();
		int r;
		scanf_s("%d", &r);
		for (int i = 1; i<=4; i++){
			for (int j = 0; j<4; j++)
			{
				int temp;
				scanf_s("%d", &temp);
				if (i == r)
				{
					have.insert(temp);
				}
			}
		}
		int res = -1;
		int mul = 0;
		scanf_s("%d", &r);
		for (int i = 1; i <= 4; i++){
			for (int j = 0; j<4; j++)
			{
				int temp;
				scanf_s("%d", &temp);
				if (i == r)
				{
					if (have.find(temp) != have.end())
					{
						if (res != -1)
						{
							mul = 1;
							//break;
						}
						else
						{
							res = temp;
						}
					}
				}
			}
		}
		if (mul != 0)
		{
			printf("Bad magician!\n");
		}
		else
		{
			if (res == -1)
			{
				printf("Volunteer cheated!\n");
			}
			else
			{
				printf("%d\n", res);
			}
		}
	}
	return(0);
}