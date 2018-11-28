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
set<double> a,b;
int main()
{
	ios::sync_with_stdio(false);
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	int t;cin>>t;
	for (int tt=1;tt<=t;tt++){
		int n;cin>>n;a.clear();b.clear();
		for (int i=0;i<n;i++){
			double x;cin>>x;a.insert(x);
		}
		for (int i=0;i<n;i++){
			double x;cin>>x;b.insert(x);
		}
		set<double> c=a;
		set<double> d=b;
		int t1=0;int ans1=0;
		for (set<double>::iterator it=a.begin();it!=a.end();){
			if (b.lower_bound(*it)==b.end()) break;
			else if (*it>*b.begin()) {
				ans1++;a.erase(it++);b.erase(b.begin());
			}
			else b.erase(--b.end()),a.erase(it++);
		}
		ans1+=a.size();
		for (set<double>::iterator it=c.begin();it!=c.end();){
			if (d.lower_bound(*it)==d.end()) break;
			else d.erase(d.lower_bound(*it)),c.erase(it++);
		}
		int ans2=c.size();
		cout<<"Case #"<<tt<<": "<<fixed<<setprecision(7)<<ans1<<' '<<ans2<<endl;
	}
	//system("pause");
    return 0;
}        