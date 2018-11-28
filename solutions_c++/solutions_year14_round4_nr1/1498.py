#include<iostream>
#include<vector>
#include<fstream>
#include<queue>
#include<algorithm>
#include<list>
#include<cstdio>
#include<stack>
#include<cstring>
#include <climits>
#include<cmath>
#include<string>
#include <functional>
#include<sstream>
#include<map>
#include<set>

#pragma comment(linker, "/STACK:100000000000000")

using namespace std;
#define     For(i,a,b)        for (int i=a; i<b; i++)
#define     Rep(i,a)          for (int i=0; i<a; i++)
#define     ALL(v)            (v).begin(),(v).end()
#define     Set(a,x)          memset((a),(x),sizeof(a))
#define     EXIST(a,b)        find(ALL(a),(b))!=(a).end()
#define     Sort(x)           sort(ALL(x))
#define     UNIQUE(v)         Sort(v); (v).resize(unique(ALL(v)) - (v).begin())
#define     MP                make_pair
#define     SF                scanf
#define     PF                printf
#define     MAXN              10011
#define     MAXM              1001
#define     MOD               1000000007
#define     Dbug              cout<<"";
#define     EPS               1e-15
typedef long long ll;
typedef pair<int,int> pii;
int n, x, arr[MAXN];
string st;
int main(){
	//ios_base::sync_with_stdio(false);
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int tc=1, t;
	cin>>t;
	while(t--)
	{
		cin>>n>>x;
		Rep(i, n) cin>>arr[i];
		sort(arr, arr+n);
		int l=0, r=n-1, ans=0;
		while(l<=r)
		{
			if(l==r)
			{
				ans++;
				break;
			}
			if(arr[l]+arr[r]<=x) ans++, r--, l++;
			else ans++, r--;
		}
		PF("Case #%d: %d\n", tc++, ans);
	}
	return 0;
}