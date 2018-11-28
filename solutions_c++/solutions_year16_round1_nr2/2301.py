#include <bits/stdc++.h>
using namespace std;

#define maxsiz 1000000
#define mod 1000000007
#define F first
#define S second
#define si(a) scanf("%d",&a)
#define sl(a) scanf("%llu",&a)
#define pi(a) printf("%d",a)
#define pl(a) printf("%llu",a)
#define fr(i,k,n) for(int i = k ; i < n ; i++ )
#define mp(a,b) make_pair(a,b)
#define pb(a) push_back(a)
#define printvect(a,n) fr(i,0,n) cout << fixed << a[i] << " " ;
typedef unsigned long long int ull;
int a[4000];

int main()
{
	ull test;
	cin >> test;
	fr(t,0,test)
	{
		int n,k;
		cin >> n;
		fr(i,0,4000)
			a[i] = 0 ;

		fr(i,0,2*n-1)
		{
			fr(j,0,n)
			{
				cin >> k ;
				a[k]++;
			}
		}

		vector<int> ans;
		fr(i,0,4000)
		{
			//cout << a[i] << " ";
			if(a[i]%2==1)
				ans.pb(i);
		}
		// cout << endl ;
		cout << "Case #" << t+1 << ": " ;
		fr(i,0,n)
			cout << ans[i] << " ";
		cout << endl ;
	}
	return 0;
}