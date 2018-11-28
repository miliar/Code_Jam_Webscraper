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
template <class T> T sqr(T x){return x*x;}
int n,x;
multiset<int> a;
int main(){
	ios::sync_with_stdio(false);
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	int t;cin>>t;
	while (t--){
		cin>>n>>x;
		a.clear();
		for (int i=0;i<n;i++) {
			int x;cin>>x;
			a.insert(x);
		}
		int total=0;
		while (!a.empty()){
			int now=*a.begin();
			total++;
			multiset<int>::iterator it=a.upper_bound(x-now);
			if (it==a.begin()){
				a.erase(a.begin());
			}
			else{
				it--;
				if (it==a.begin()){
					a.erase(a.begin());
				}
				else{
					a.erase(it);
					a.erase(a.begin());
				}
			}
		}
		static int T=1;
		cout<<"Case #"<<T++<<": "<<total<<endl;
	}
	return 0;
}