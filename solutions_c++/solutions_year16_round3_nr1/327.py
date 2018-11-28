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

int n;
LL a,b,c,k;
int t;
int par[30];
set <PII> pok,po;
set <PII>::iterator it1,it2;
PII x,xx;
int sum,psum;
int main()
{
	scanf("%d", &t);
	FOR(tt,1,t)
	{
		printf("Case #%d: ",tt);
		cin>>n;
		REP(i,n)
		{
			scanf("%d", &par[i]);
			sum+=par[i];
			pok.insert(MP(-par[i],'A'+i));
		}
		while(sum>0)
		{
			po=pok;
			psum=sum;
			it1=po.begin();
			x=(*it1);
			po.erase(it1);
			x.ST++;
			psum--;
			if(x.ST!=0)
			{
				po.insert(x);
			}
			if((-(*po.begin()).ST)>(psum/2))
			{
				po=pok;
				psum=sum;
				it1=po.begin();
				x=(*it1);
				po.erase(it1);
				it1=po.begin();
				xx=(*it1);
				po.erase(it1);
				x.ST++;
				xx.ST++;
				psum-=2;
				if(x.ST!=0)
				{	
					po.insert(x);
				}	
				if(xx.ST!=0)
				{	
					po.insert(xx);
				}	
				if((-(*po.begin()).ST)>(psum/2))
				{
					cerr<<"nic nie pomoglo"<<endl;
				}
				else
				{
				
					printf("%c%c ",x.ND,xx.ND);
						sum=psum;
						pok=po;
				}
			}
			else
			{
				printf("%c ",x.ND);
				sum=psum;
				pok=po;
			}
		}
		printf("\n");
	}
}






