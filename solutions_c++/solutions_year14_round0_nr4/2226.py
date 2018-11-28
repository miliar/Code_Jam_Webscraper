#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;
int test = 1, t;
vector<double> ken1;
vector<double> na1;
int n;
bool cf( double a, double b )
{
	return a>b;
}
void solve()
{
	cin >> n;
	double temp;
	for( int i = 0 ; i < n ; i++ )
	{
		cin >> temp;
		na1.push_back(temp);
	}
	for( int i = 0 ; i < n ; i++ )
	{
		cin >> temp;
		ken1.push_back(temp);
	}
	sort(na1.begin(),na1.end());
	sort(ken1.begin(),ken1.end());
	int t1 = n-1 , t2 = n-1;
	int res1 = 0 , res2 = 0;
	while( t1 >= 0 && t2 >= 0 )
	{
		if( na1[t1] > ken1[t2] )
		{
			t1--; t2--; res1++;
		}
		else
		{
			t2--;
		}
	}
	t1 = n-1 ; t2 = n-1;
	while( t1 >= 0 && t2 >= 0 )
	{
		if( na1[t1] < ken1[t2] )
		{
			t1--; t2--; res2++;
		}
		else
		{
			t1--;
		}
	}
	cout << "Case #" << test << ": " << res1 << " " << n-res2 << endl;
	return;
}

int main()
{
	freopen("D-large.in","r",stdin);
	freopen("output.out.","w",stdout);
	cin >> t;
	for( ; test <= t ; test++ )
	{
		ken1.clear();
		na1.clear();
		solve();
	}
	return 0;
}