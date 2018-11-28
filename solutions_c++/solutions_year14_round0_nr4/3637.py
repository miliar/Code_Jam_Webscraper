#include <bits/stdc++.h>
#define fi "D.INP"
#define fo "D.OUT"
#define nmax 1000+5
#define INF
using namespace std;
typedef double dd;
typedef multiset<dd> SS;
//VARIABLES
int test,res,ans,n;
dd a[nmax],b[nmax];
SS my_set;
//PROTOTYPES
void Process();

//MAIN
int main()
{
	int tc;
	freopen(fi,"r",stdin);
	freopen(fo,"w",stdout);
	scanf("%d",&tc);
	while (tc--) Process();
	return 0;
}

//FUNCTIONS
void Process()
{
	int k;
	SS::iterator it;
	res=ans=0;
	scanf("%d",&n);
	for (int i=1;i<=n;++i) scanf("%lf",&a[i]);
	for (int i=1;i<=n;++i) scanf("%lf",&b[i]);
	sort(a+1,a+n+1);
	sort(b+1,b+n+1);
	//for (int i=1;i<=n;++i) cerr << a[i] << " "; cerr << endl;
	//for (int i=1;i<=n;++i) cerr << b[i] << " "; cerr << endl;
	k=n;
	for (int i=n;i>=1;--i)
	{
		while (k>=1)
		if (b[k]>a[i]) --k; else break;
		if (k==0) break;
		++res;
		if (k==1) break;
		--k;
	}
	my_set.clear();
	for (int i=1;i<=n;++i) my_set.insert(b[i]);
	for (int i=1;i<=n;++i)
	{
		it=my_set.end();--it;
		if (*it<a[i])
		{
			ans=(n+1-i);
			break;
		}
		it=my_set.lower_bound(a[i]);
		my_set.erase(it);
	}
	printf("Case #%d: %d %d\n",++test,res,ans);
}
