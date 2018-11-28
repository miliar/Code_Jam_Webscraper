#include <iostream>
#include <sstream>
#include <ios>
#include <iomanip>
#include <functional>
#include <algorithm>
#include <vector>
#include <string>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <climits>
using namespace std;
#define XINF INT_MAX
#define INF 0x3FFFFFFF
#define MP(X,Y) make_pair(X,Y)
#define PB(X) push_back(X)
#define REP(X,N) for(int X=0;X<N;X++)
#define REP2(X,L,R) for(int X=L;X<=R;X++)
#define IT iterator
typedef long long ll;
typedef pair<int,int> PII;
typedef vector<PII> VII;
typedef vector<int> VI;

int main()
{
	ios::sync_with_stdio(false);
	//freopen("B-small-attempt0.in","r+",stdin);
	//freopen("B-small-attempt0.out","w+",stdout);
	int t,cs=1;
	cin>>t;
	while(t--)
	{
		double c,f,x;
		cin>>c>>f>>x;
		double ans=0., r=2.0;
		while(ans+c/r+x/(r+f) < ans+x/r + 1e-7)
		{
			ans+=c/r;
			r+=f;
		}
		cout<<"Case #"<<cs++<<": ";
		cout<<fixed<<setprecision(7)<<ans+x/r<<endl;
	}
	return 0;
}

