#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <complex>
#include <iterator>
#include <set>
#include <bitset>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <deque>

using namespace std;
typedef vector<int> VI;
typedef long long LL;
typedef vector<VI> VVI;
typedef vector<LL> VLL;
typedef vector<double> VD;
typedef vector<string> VS;
typedef pair<int, int> PII;
typedef vector<PII> VPII;

#define FOR(x, b, e) for(int x = b; x <= (e); ++x)
#define FORD(x, b, e) for(int x = b; x >= (e); --x)
#define REP(x, n) for(int x = 0; x < (n); ++x)
#define VAR(v, n) typeof(n) v = (n)
#define ALL(c) (c).begin(), (c).end()
#define SIZE(x) ((int)(x).size())
#define FOREACH(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define PB push_back
#define ST first
#define ND second
#define MP make_pair
#define PF push_front

int n,t	;
int j,p,s,k;
map <PII,int> jp,js,ps;
struct ub{
	int j;
	int p;
	int s;
};
vector <ub> wszy;
ub temp;
int mas;
int wyn;
int ile;
int mwyn;
bool ok;
int main()
{
	scanf("%d", &t);
	FOR(tt,1,t)
	{
		//cerr<<tt"/"<<t<<endl;
		printf("Case #%d: ",tt);
		scanf("%d %d %d %d", &j, &p, &s, &k);
		wszy.clear();
		mwyn=0;
		wyn=0;
		FOR(i1,1,j)
		{
			FOR(i2,1,p)
			{
				FOR(i3,1,s)
				{
					temp.j=i1;
					temp.p=i2;
					temp.s=i3;
					wszy.PB(temp);
				}
			}
		}
		FORD(z,(1<<(SIZE(wszy)))-1,0)
		{
			mas=z;	
			ile=__builtin_popcount(mas);
			if(ile>wyn)
			{
				ok=1;
				jp.clear();
				js.clear();
				ps.clear();
				REP(i,SIZE(wszy))
				{
					if(mas%2)
					{
						jp[MP(wszy[i].j,wszy[i].p)]++;
						if(jp[MP(wszy[i].j,wszy[i].p)]>k)
						{
							ok=false;
							break;
						}
						js[MP(wszy[i].j,wszy[i].s)]++;
						if(js[MP(wszy[i].j,wszy[i].s)]>k)
						{
							ok=false;
							break;
						}
						ps[MP(wszy[i].p,wszy[i].s)]++;
						if(ps[MP(wszy[i].p,wszy[i].s)]>k)
						{
							ok=false;
							break;
						}
					}
					mas/=2;
				}
				if(ok)
				{
					wyn=ile;
					mwyn=z;
				}
			}
		}
		printf("%d\n",wyn);
		mas=mwyn;
		int wypisal=0;
		REP(i,SIZE(wszy))
		{
			if(mas%2){
			wypisal++;
			printf("%d %d %d\n",wszy[i].j,wszy[i].p,wszy[i].s);
			}
			mas/=2;
		}
		if(wypisal!=wyn)
		{
			cerr<<"zla ilosc wypisana przy "<<tt<<endl;
		}
	}

}







