#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int test = 1, t;
double c,f,x;

void solve()
{
	cin >> c >> f >> x;
	if( c >= x )
	{
		printf("Case #%d: %.7f\n",test,x/2);
		return;
	}
	double temp1=x/2,temp2=(c/2)+x/(2+f),nut=2;
	int indx = 1;
	while( temp1 > temp2 )
	{
		temp1 = temp2;
		temp2 = 0;
		for( int i = 0 ; i <= indx ; i++ )
		{
			temp2 += c/(2+i*f);
		}
		temp2 += x/(2+(indx+1)*f);
		indx++;
	}
	printf("Case #%d: %.7f\n",test,temp1);
	return;
}
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output.out.","w",stdout);
	cin >> t;
	for( ; test <= t ; test++ )
	{
		solve();
	}
	return 0;
}