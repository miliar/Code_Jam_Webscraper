#pragma comment(linker,"/STACK:102400000,102400000")
#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstring>
#include <string>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <queue>
#include <cctype>
#include <list>
#include <stack>
#include <sstream>
#include <set>
#include <map>
#include <utility>
#include <algorithm>
#include <iomanip>
#include <vector>
using namespace std;
#define X first
#define Y second
#define mp make_pair
#define pb push_back
#define mset(a) memset(a,0,sizeof(a))
#define mmset(a) memset(a,-1,sizeof(a))
#define mcpy(a,b) memcpy(a,b,sizeof(a))
const int inf=1e9+7;
const long long linf=1e18;
const double pi=acos(-1.0);
typedef long double lf;
typedef vector <int> vi;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
typedef pair<double,double> pdd;
typedef pair<long long,long long> pll;
typedef vector<int> vi;
double tim[111111];
double speed[111111];
int main()
{
	ios::sync_with_stdio(false);
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	int t;cin>>t;
	for (int tt=1;tt<=t;tt++){
		double	c,f,x;cin>>c>>f>>x;
		speed[0]=2;
		double ans=1e100;
		for (int i=1;i<111111;i++)
			speed[i]=speed[i-1]+f,
			tim[i]=tim[i-1]+c/speed[i-1];
		for (int i=0;i<x/c;i++){
			ans=min(ans,tim[i]+x/speed[i]);
		}
		cout<<"Case #"<<tt<<": "<<fixed<<setprecision(7)<<ans<<endl;
	}
	//system("pause");
    return 0;
}        