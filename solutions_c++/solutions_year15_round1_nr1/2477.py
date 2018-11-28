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
#define printvect(a,n) fr(i,0,n) cout << a[i] << " " ;
typedef unsigned long long int ull;



int main()
{
	int test,n;
	cin >> test ;
	fr(t,0,test)
	{
		cin >> n ; 
		vector<int> num(n);
		fr(i,0,n) cin >> num[i] ;

		ull sum1 = 0 ;
		ull sum2 = 0 ;
		ull rate = 0 ; 
		fr(i,0,n-1)
		{
			if(num[i] > num[i+1])
			{
				sum1 += (num[i] - num[i+1]);
				if((num[i] - num[i+1]) > rate)
					rate = (num[i] - num[i+1]);
			}
		}

		fr(i,0,n-1)
		{
			if(num[i] > rate)
				sum2 += rate;
			else
				sum2 += num[i];
		}
		cout << "Case #" << t+1 << ": " << sum1 << " " << sum2 <<  endl;
	}
	return 0 ;
}