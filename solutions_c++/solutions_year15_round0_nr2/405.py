#include <cstdio>
#include <string>
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int t=1;
void solve()
{
	vector<int> in;
	int n,max_=-1;
	cin >> n;
	in.resize(n);
	for( int i = 0 ; i< n ; i++ )
	{
		cin >> in[i];
		max_=max(max_,in[i]);
	}
	int min_ = max_,temp;
	for( int k = 1 ; k <= max_ ; k++ )
	{
		temp = 0;
		for( int i = 0 ; i < n ; i++ )
			if( k < in[i] )
				temp += (in[i]-1)/k;
		min_ = min(min_,k+temp);
	}
	cout << "Case #" << t << ": " << min_ << endl;
}
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int tt;
	cin >> tt;
	for(t=1;t<=tt;t++)
	{
		solve();
	}
	return 0;
}