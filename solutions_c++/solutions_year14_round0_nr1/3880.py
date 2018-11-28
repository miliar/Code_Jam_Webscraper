#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <bitset>
#include <utility>
#include <ctime>
#include <cassert>
#include <climits>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<vi> vvi;
typedef pair<int,int> pii;
typedef vector<pii > vii;
typedef pair<ll,ll> pll;
typedef vector<string> vs;

#define MOD 1000000007
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define MEM(a,b) memset(a,(b),sizeof(a))
#define pr(a) cout<<#a<<" = "<<(a)<<endl
#define cin(n) int (n); scanf("%d", &(n))
#define cin2(n,m) int (n),(m); scanf("%d%d",&(n),&(m))
#define sz(a) int((a).size())
#define all(a) a.begin(),a.end()
#define loop(x,a,b) for(int (x) = (a);(x)<(b);(x)++)
#define rep(x,n)   for(int (x)=0;(x)<(n);(x)++)
#define tr(c,it) for(typeof((c).begin()) it = (c).begin(); it != (c).end(); it++)
#define prc(a) tr(a, it) cout<<*(it)<<" "; cout<<endl
#define pra(a,n) for(int i=0; i<(n); i++) printf("%d ",((a)[i])); printf("\n") 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define ain(a,n) int ((a)[(n)]); for(int i=0; i<(n); i++) scanf("%d",&((a)[i])) 
#define vin(a,n) vector<int> (a); (a).resize((n)); for(int i=0; i<(n); i++) scanf("%d",&((a)[i])) 
#define TEST cin(test);	while(test--)
//#define FILE

int main()
{
	#ifdef FILE
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	#endif
	int a[4][4],b[4][4],c[4];
	int  k = 0 ;
	TEST
	{
		k++;
		int f = 0,ind;
		cin(a1);
		rep(i,4)
			rep(j,4)
				scanf("%d",&a[i][j]);
		cin(a2);
		rep(i,4)
			rep(j,4)
				scanf("%d",&b[i][j]);
		rep(i,4)
		{
			c[i] = 0;
			rep(j,4)
			{
				if(a[a1-1][i] == b[a2-1][j])
					c[i]++;
			}
		}
		rep(i,4)
		{
			if(c[i] > 0)
				f++,ind = a[a1-1][i];
		}
		if(f == 0)
			printf("Case #%d: Volunteer cheated!\n",k);
		else if(f == 1)
			printf("Case #%d: %d\n",k,ind);
		else if(f > 1)
			printf("Case #%d: Bad magician!\n",k);
	}

	return 0;
}

