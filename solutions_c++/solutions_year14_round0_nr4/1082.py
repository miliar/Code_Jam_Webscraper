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
#define     MAXN              1001
#define     MAXM              1001
#define     MOD               1000000007
#define     Dbug             cout<<"";
#define     EPS              1e-15
typedef long long ll;
typedef pair<int,int> pii;
int n;
vector<double> a, b;
bool vis[MAXN];
string st;
int main(){
	//ios_base::sync_with_stdio(false);
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int tc, t=1;
	cin>>tc;
	while (tc--)
	{
		PF("Case #%d: ", t++);
		cin>>n;
		a.resize(n), b.resize(n);
		Rep(i, n) cin>>a[i];
		Rep(i, n) cin>>b[i];
		Sort(a), Sort(b);
		int p1=0, p2=0, l1=0, l2=0, r1=n-1, r2=n-1;
		Rep(i, n)
		{
			vis[i]=0;
			if(a[r1]>b[r2]) r1--, r2--, p1++;
			else l1++, r2--;
		}
		Rep(i, n) 
		{
			bool fi=0;
			Rep(j, n) if(vis[j]==0 && b[j]>a[i])
			{
				fi=vis[j]=1;
				break;
			}
			if(!fi) p2++;
		}
		cout<<p1<<' '<<p2<<endl;
	}
	return 0;
}