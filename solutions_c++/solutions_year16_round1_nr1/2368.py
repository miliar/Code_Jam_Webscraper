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

int main()
{
	ull test;
	cin >> test;
	fr(t,0,test)
	{
		string s,k;
		cin >> s;
		k = s[0]; 
		fr(i,1,s.length())
		{
			if(s[i]>=k[0])
				k = s[i]+k;
			else
				k = k + s[i];
		}
		cout << "Case #" << t+1 << ": " << k << endl;
	}
	return 0;
}