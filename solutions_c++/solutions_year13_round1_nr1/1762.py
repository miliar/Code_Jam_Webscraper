#include <iostream>
#include <cmath>
#include <cstdlib>
#include <cstdio>
using namespace std;

void calc(int r,int t,const int& count)
{
	int temp = 2*r-1;
	int result = floor( (sqrt(temp*temp+8*t)-temp)/4 );
	cout << "Case #" << count << ": " << result << endl;
}
int T,r,t;
int main()
{
	 freopen("A-small-attempt0.in","r",stdin);
	freopen("rounda.txt","w",stdout);
	cin >> T;
	for( int count = 1; count <= T; ++count)
	{
		cin >> r >> t;
		calc(r,t,count);
	}
	return 0;
}