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
#define N 55555
int main()
{
	freopen("data.in","r",stdin);
	freopen("data.out","w",stdout);
    int t;cin>>t;
	
	while (t--){
		int n;string temp;cin>>n>>temp;
		int ans=0;
		int now=0;
		for (int i=0;i<n+1;i++){
			if (temp[i]!='0'){
			if (now>=i) now+=temp[i]-'0';
			else {
				ans+=(i-now);
				now=i+temp[i]-'0';
			}
			}
		}
		static int tot=1;
		cout<<"Case #"<<tot++<<": "<<ans<<endl;
	}
	//system("pause");
    return 0;
}