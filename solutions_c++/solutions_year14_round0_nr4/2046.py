#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <cstdlib>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <ctime>
#include <queue>
#include <vector>
#include <stack>
#include <list>
#include <cmath>
#include <ctime>
using namespace std;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef vector<vi> vvi;
typedef long long int lli;

#define wez(n) int (n); scanf("%d",&(n));
#define wez2(n,m) int (n),(m); scanf("%d %d",&(n),&(m));
#define wez3(n,m,k) int (n),(m),(k); scanf("%d %d %d",&(n),&(m),&(k));
#define debug(vari) cout<<#vari<<" = "<<(vari)<<endl;
#define TESTS wez(testow)while(testow--)
#define modfun 1000000007
#define pb push_back
#define mp make_pair
#define sz(a) int((a).size())
#define INF 2147483647
#define REP(x,a,b) for(int (x) = (a);(x)<=(b);(x)++)
#define rep(x,n)   for(int (x)=0;(x)<(n);(x)++)
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(typeof((c).begin() i = (c).begin();!= (c).end(); i++) 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end()) 
#define air
using namespace std;
/*
inline long int inp( )
{
long int n=0;
long int ch=getchar_unlocked();
while(!(ch >= '0' && ch <= '9') )ch=getchar_unlocked();
while( ch >= '0' && ch <= '9' )
n = (n<<3)+(n<<1) + ch-'0', ch=getchar_unlocked();
return n;
}
*/
int main()
{
	#ifdef air
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	#endif
	int casea=1;
	TESTS
	{
		wez(n);
		double temp;
		vector<double> naomi,ken;
		rep(i,n){
			scanf("%lf",&temp);
			naomi.pb(temp);
		}
		rep(i,n){
			scanf("%lf",&temp);
			ken.pb(temp);
		}
		sort(naomi.begin(),naomi.end());
		sort(ken.begin(),ken.end());
		// Optimized War
		int scoreWar=0;
		int startNaomi=0,startKen=0,endNaomi=n-1,endKen=n-1;
		while((startNaomi<=endNaomi)&&(startKen<=endKen))
		{
			if(naomi[endNaomi]>ken[endKen])
			{
				scoreWar++;
				endNaomi--;
				startKen++;
			}
			else
			{
				endNaomi--;
				endKen--;
			}
		}
		// rep(i,n)
		// cout<<naomi[i]<<" ";
		// cout<<endl;
		// rep(i,n)
		// cout<<ken[i]<<" ";
		// cout<<endl;

		int scoreDeceitfulWar=0;
		int naomiIndex=n-1,kenIndex=n-1;
		for(int i=0;i<n;i++)
		{
			while(kenIndex>=0)
			{
				if(naomi[naomiIndex]<ken[kenIndex])
					kenIndex--;
				else
				{
					scoreDeceitfulWar++;
					kenIndex--;
					naomiIndex--;
				}
			}
		}
		printf("Case #%d: %d %d\n",casea,scoreDeceitfulWar,scoreWar);
		casea++;
	}
	return 0;
}