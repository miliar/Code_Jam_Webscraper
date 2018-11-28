#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define MAXVAL 10010
 
 
int main()
{
	int t;
	scanf("%d",&t);
	for(int k=1;k<=t;k++)
	{
		int d;
		cin >> d;
		int a[d+1];
		int m= 0;
		for (int i = 0; i < d; i++)
		{
			scanf("%d",&a[i]);
		}
 		for(int i=0;i<d;i++)
 		{
 			if(a[i]>=m)
 			{
 				m=a[i];
			 }
		 }
		 
 		ll val;
 		int i,j;
		ll ans = MAXVAL;
		for (i = 1; i <=m; i++)
		{
			val= i;
			for ( j= 0; j<d; j++)
			{
				if(a[j]%i==0)
				{
					val+=(a[j]/i)-1;
				}
				else
				val+=(a[j]/i);
			}
			ans = min(ans,val);
		}
		cout << "Case #" <<k<< ": " << ans << endl;
	}
	return 0;
}
