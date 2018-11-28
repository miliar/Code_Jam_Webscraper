#include <iostream>
#include <cstring>
#include <string>
#include <math.h>
#include <stack>
#include <sstream>
#include <math.h>
using namespace std;
unsigned long long ar[] = {1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404,10000200001,10221412201,12102420121,12345654321,40000800004,1000002000001,1002003002001,1004006004001,1020304030201,1022325232201,1024348434201,1210024200121,1212225222121,1214428244121,1232346432321,1234567654321,4000008000004,4004009004004}; 
int main()
{
	freopen("input.txt","r",stdin);
	freopen("Text.txt","a",stdout);
	unsigned long long k,v;
	int t;
	cin >> t;
	
	for ( int p = 1 ; p <= t ; p++ )
	{
		int sum = 0;
		cin >> k >> v;
		for ( int i = 0 ; i < 39 ; i++ )
		{
			if ( ar[i] >= k && ar[i] <= v ) // if this number in range.
			{
				sum++;
			}
		}
		cout<<"Case #"<<p<<": "<<sum<<endl;
	}
	/*unsigned long long tc;
	//cin >> tc;
	 tc=100000000000000;

	for ( unsigned long long i = 1 ; i <= sqrt(tc) ; i++ )
	{
		//a++;
		//cin >> a >> b;
		//int sum=0;
		//for ( int p = a ; p <= b ; p++ )
	//	{
			string res;
			stringstream convert;
			convert<<i;
			res = convert.str();
			if ( res == string ( res.rbegin() , res.rend() ) )
			{
				stringstream co;
				string r;
				co<<i*i;
				r = co.str();
				if ( r == string(r.rbegin(),r.rend()) )
				{
					cout<<r<<endl;
				}
				/*if ( l == k )
				{
					string h;
					stringstream co;
					co<<l;
					h = co.str();
					if ( h == string ( h.rbegin() , h.rend() ) )
					{
						//sum++;
						cout<<i<<endl;
					}
				}
			}
		//}

		/*cout<<"Case #"<<i<<": ";
		if ( sum == 1 ) cout<<"111111"<<endl;
		else
			cout<<sum<<endl;
	}*/

	return 0;
}