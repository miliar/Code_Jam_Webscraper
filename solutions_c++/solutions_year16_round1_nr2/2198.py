#include <cstdio>
#include <iostream>
#include <cstring>
using namespace std;
int cnt[2555];
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int t; cin >> t;
	int test = 0;
	while(t--)
	{
		test++;
		cout << "Case #" << test << ": ";
		memset(cnt,0,sizeof(cnt));
		int n,tt; cin >>n;
		int mx=-1;
		for( int i = 0 ; i < 2*n-1 ; i++ )
		{
			for( int j = 0 ; j < n ; j++ )
			{
				cin >> tt;
				cnt[tt]++;
				if(tt>mx) mx = tt;
			}
		}
		for( int i = 1 ; i <= mx ; i++ )
		{
			if(cnt[i]%2==1)
				cout << i << " ";
		}
		cout << endl;
	}
	return 0;
}