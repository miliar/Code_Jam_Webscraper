#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
using namespace std;

typedef vector<vector<int> > vii;
typedef vector<int> vi;
typedef vector<string> vs;
typedef long long LL;

#define sz size()
#define all(n) n.begin(),n.end()
#define clr(a,n) memset(a,n,sizeof(a))
#define pb push_back
#define fo(i,j) for(int i=0;i<j;i++)
#define foreach(it,a) for(__typeof((a).begin()) it=(a).begin();it!=(a).end();it++)

int main()
{
    //freopen ("B-small-attempt3.in","r",stdin);
    freopen ("B-large.in","r",stdin);
    freopen ("B2.out","w",stdout);
	
	int T,KK=1;
	
	scanf("%d",&T);
	
	while(T--)
	{
		printf("Case #%d:",KK);
		
		int N;
		LL P;
		
		scanf("%d %lld",&N,&P); // codeblocks
		
		LL L=0ll,W=0ll;
		LL t,TP=P;
		
		if(TP==(1ll<<N))printf(" %lld",(1ll<<N)-1ll);
		
		else
		{
			t=(1ll<<N)/2ll;
		
			while(TP>0)
			{
				TP-=t;
				t/=2ll;
				L++;
			}
			printf(" %lld",(1ll<<L)-2ll);
		}
		
		TP=(1ll<<N)-P;
		t=(1ll<<N)/2;
		
		if(TP==0)printf(" %lld\n",(1ll<<N)-1ll);
		else if(P==1)printf(" 0\n");
		else
		{
			while(TP>0)
			{
				TP-=t;
				t/=2;
				W++;
			}
			//W++;
			printf(" %lld\n",(1ll<<N)-(1ll<<W));
		}
		
		KK++;
	}
}


































