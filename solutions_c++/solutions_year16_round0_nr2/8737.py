#include <bits/stdc++.h>
#define pb push_back
#define fi first
#define sc second
#define inf 2000000000
#define MP make_pair
#define orta ((a+b)/2)
#define min3(a,b,c) min(a,min(b,c))
#define max3(a,b,c) max(a,max(b,c))
#define dbg(x) cerr<<#x<<":"<<x<<endl
#define N 105
#define MOD 1000000007
using namespace std;
typedef  pair <int ,int> ii;
typedef  long long int lint;

int n,d[N];	
string a;
int main()
{
//	freopen("asdsada.in","r",stdin);
//	freopen("asdsada.out","w",stdout);
	
	int ts;
	scanf("%d",&ts);
	for (int qqq = 0; qqq < ts; qqq++)
	{
		cin >> a;
		n=a.size();
		for (int i = 0; i < n; i++)
			d[i]= (a[i]=='+');
		int t=0,r=d[0],cev=0;
		for(int t=0;t<n;t++)
		{
			if(r!=d[t])
			{
				cev++;
				r=d[t];
			}
		}
		if(r==0)
			cev++;
		printf("Case #%d: %d\n",qqq+1,cev);
	}
}




