#include<iostream>
#include<algorithm>
#include<stdio.h>
#include<limits.h>
#include<string.h>
#include<math.h>
#include<vector>
#include<queue>
#include<map>
#include<set>

#define s(N) scanf("%d",&N)
#define REP(i,N) for(int i=0;i<N;i++)
#define pb push_back
#define XX first
#define X first
#define Y second
#define YY second.first
#define ZZ second.second
#define mp make_pair
#define all(i) i.begin(),i.end()
#define tr(i,it) for(typeof(i.begin()) it=i.begin();it!=i.end();it++)

#define cpe(i) ((i)*((i)-1)/2)

using namespace std;

typedef pair<int,int> pii;
typedef pair<int,pair<int,int> > piii;
typedef long long LL;

bool comp(const pii &A, const pii &B)
{
	if(A.Y!=B.Y) return A.Y<B.Y;
	return A.X<B.X;
}

int main()
{
	int T; s(T);
	int N,M,o,e,p;
	vector<pii> pass;
	REP(c,T)
	{
		s(N); s(M);
		pass.clear();
		REP(i,M)
		{
			s(o); s(e); s(p);
			REP(j,p) pass.pb(mp(o,e));
		}
		LL diff=0,mx,mxj;
		sort(all(pass),comp);
		bool found=true;
		while(found)
		{
			found=false;
			REP(i,pass.size())
			{
				mx=0;
				REP(j,pass.size())
				{
					if(pass[j].Y<pass[i].X||pass[j].Y>pass[i].Y||pass[j].X>=pass[i].X) continue;
					if(((cpe(pass[i].Y-pass[j].X+1)+cpe(pass[j].Y-pass[i].X+1))-(cpe(pass[i].Y-pass[i].X+1)+cpe(pass[j].Y-pass[j].X+1)))>mx)
					{
						mx=((cpe(pass[i].Y-pass[j].X+1)+cpe(pass[j].Y-pass[i].X+1))-(cpe(pass[i].Y-pass[i].X+1)+cpe(pass[j].Y-pass[j].X+1)));
						mxj=j;
					}
				}
				if(mx!=0)
				{
					swap(pass[i].X,pass[mxj].X);
					diff+=mx;
					found=true;
				}
			}
		}
		printf("Case #%d: %lld\n",c+1,diff);
	}
	return 0;
}
