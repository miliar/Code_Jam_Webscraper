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
#include <limits>
#include <string>
#include <cassert>

using namespace std;
typedef long long LL;
typedef pair<int,int> pii;

#define forup(i,a,b) for(int i=a; i<b; ++i)
#define fordn(i,a,b) for(int i=a; i>b; --i)
#define rep(i,a) for(int i=0; i<a; ++i)

#define dforup(i,a,b) for(i=a; i<b; ++i)
#define dfordn(i,a,b) for(i=a; i>b; --i)
#define drep(i,a) for(i=0; i<a; ++i)

#define slenn(s,n) for(n=0; s[n]!=13 and s[n]!=0; ++n);s[n]=0

#define gi(x) scanf("%d",&x)
#define gl(x) cin>>x
#define gd(x) scanf("%lf",&x)
#define gs(x) scanf("%s",x)

#define pis(x) printf("%d ",x)
#define pin(x) printf("%d\n",x)
#define pls(x) cout<<x<<" "
#define pln(x) cout<<x<<"\n"
#define pds(x) printf("%.12f ",x)
#define pdn(x) printf("%.12f\n",x)
#define pnl() printf("\n")

#define fs first
#define sc second

#define pb push_back

const int inv=1000000000;
const int minv=-inv;

int T;
int a;
int ans1,ans2;
int row1[16],row2[16];
vector<int> res;

int main()
{
	gi(T);
	rep(z,T)
	{
		gi(ans1); --ans1;
		rep(i,4)
			rep(j,4)
			{
				gi(a); --a;
				row1[a]=i;
			}

		gi(ans2); --ans2;
		rep(i,4)
			rep(j,4)
			{
				gi(a); --a;
				row2[a]=i;
			}

		res.resize(0);
		rep(i,16)
			if(row1[i]==ans1 and row2[i]==ans2)
				res.pb(i);

		if((int)res.size()==0)
			printf("Case #%d: Volunteer cheated!\n",z+1);
		else if((int)res.size()>1)
			printf("Case #%d: Bad magician!\n",z+1);
		else
			printf("Case #%d: %d\n",z+1,res[0]+1);
	}
	
	return 0;
}