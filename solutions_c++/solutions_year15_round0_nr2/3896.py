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
#define printvect(a,n) fr(z,0,n) cout << a[z] << " " ;
typedef unsigned long long int ull;

int passenger(vector<int> arr,int run,int max)
{
	sort(arr.begin(),arr.end());
	for(int i = 0 ; i < max ; i++ )
	{
		int a,b;
		//printvect(arr,arr.size()); cout << endl ;
		if(run%2 == 1)
		{
			//cout << "1 -> ";
			int num = arr[arr.size()-1];
			if(num%2 == 0)
			{
				a = num/2 ; b = num/2 ;
			}
			else if(num%3 == 0)
			{
				a = num/3 ; b = 2*(num/3);
			}
			else
			{
				a = num/2 ; b = num/2 + num%2 ; 
			}
			arr.pop_back();
			arr.pb(a);
			arr.pb(b);
		}
		else
		{
			//cout << "0 -> ";
			fr(j,0,arr.size())
				arr[j]-- ; 
		}
		sort(arr.begin(),arr.end());
		if(arr[arr.size()-1] == 0)
			return i + 1;
		run /= 2 ;
	}
}

int main()
{
	int test,n,ans;
	cin >> test ;
	fr(t,0,test)
	{
		cin >> n ;
		vector<int> arr(n);
		int max = 0 ; 
		fr(i,0,n) 
		{
			cin >> arr[i];
			if(arr[i] > max)
				max = arr[i];
		}
		
		//brute
		int min = max; 
		fr(i,0,pow(2,max))
		{
			ans = passenger(arr,i,max);
			//cout << "RUN "  << ans << endl ;
			if(ans < min)
				min = ans ;
		}
		cout << "Case #" << t+1 << ": " << min << endl;
	}
	return 0 ;
}