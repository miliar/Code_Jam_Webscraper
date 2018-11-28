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
#include <iomanip>
#include <list>
#include <stack>
#include <sstream>
#include <set>
#include <map>
#include <complex>
#include <utility>
#include <algorithm>
#include <iomanip>
#include <vector>
#include <cassert>
#include <bitset>
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
const double eps=1e-6;
multiset<int,greater<int> > f;
int main()
{
	freopen("data.in","r",stdin);
	freopen("data.out","w",stdout);
    int t;cin>>t;
	while (t--){
		int D;cin>>D;
		f.clear();
		int x;
		int time=0;
		for (int i=0;i<D;i++)
		{
			cin>>x;f.insert(x);
		}
		for (time=0;time<=1000;time++){
			bool flag=false;
			for (int i=0;i<time;i++){
				int cut=i,limit=time-i;
				multiset<int,greater<int> > temp(f);
				for (int j=0;j<cut;j++)
				{
					int x=*temp.begin();
					temp.erase(temp.begin());
					temp.insert(limit);temp.insert(x-limit);
				}
				if (*temp.begin()<=limit) {
					flag=true;
					break;
				}
			}
			if (flag) {break;}
		}
		static int tot=1;
		cout<<"Case #"<<tot++<<": "<<time<<endl;
	}
	//system("pause");
    return 0;
}