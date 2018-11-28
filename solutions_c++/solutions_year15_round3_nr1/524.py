#include <iostream>
using namespace std;
int test = 1;
void solve()
{
	int r,c,w;
	cin >> r >> c >> w;
	int res= (r-1)*(c/w);
	while(true)
	{
		if(c-w<=w) break;
		c -= w;
		res++;
	}
	if( c == w ) res = w;
	else res += w+1;
	cout << "Case #" << test++ << ": " << res << endl;
	return;
}
int main()
{
	freopen("2.in","r",stdin);
	freopen("2.out","w",stdout);
	int t;
	cin >> t;
	while(t--)
	{
		solve();
	}
	return 0;
}