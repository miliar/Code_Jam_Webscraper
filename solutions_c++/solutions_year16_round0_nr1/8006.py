#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	int t;
	cin >> t;
	for ( int tc = 1 ; tc <= t ; ++tc)
	{
		long long n;
		cin >>n ;
		cout << "Case #"<< tc <<": " ;
		if ( n == 0 )
		{
			cout << "INSOMNIA"<<endl;
			continue;
		}
		bool visited[10];
		for ( int i = 0 ; i < 10 ; ++i)
		{
			visited[i] = false;
		}	
		long long a = n,  cont = 0 , ans = 1;
		while ( true ) 
		{
			//cout << a << endl;
			
			a = n * ans ; 
			while ( a > 9 ) 
			{
				if (!visited[a%10] )
					cont ++ , visited[a%10] = true;
				a/=10;
			}	
			if (!visited[a] )
				cont ++, visited[a] = true;
			if ( cont == 10 )
			{	
				ans = n * ans ;
				break;
			}
			ans ++;
		}
		cout << ans << endl;
	}
}
