#include <iostream>

using namespace std;

int main()
{
	int t, max, x, n, y, i, j;
	string s;

	cin>>t;

	for( j=1; j<=t; j++ )
	{
		cin>>max>>s;
		x=y=0;
		//cout<<max<<' '<<s;

		for( i=0; i<=max; i++ )
		{
			if(x<i)
				{
					y+=i-x;
					x+=i-x;
				}

			n=s[i]-'0';
			x+=n;
		}

		cout<<"Case #"<<j<<": "<<y<<"\n";
	}

	return 0;
}