#include <iostream>
#include <algorithm>
using namespace std;

const int MA = 1500;

long double    a[ MA ];
long double	   b[ MA ];
bool		mark[ MA ];


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	cin >> T;
	int n;
	int y;
	int z;

	for(int tmp = 1; tmp <= T; ++ tmp)
	{
		cin >> n;
		for(int i = 0; i < n; ++i)
			cin >> a[i];
		for(int i = 0; i < n; ++i)
			{	
				cin >> b[i];
				mark[i] = 0;
			}

		y = 0;
		z = 0;

		sort(a,a+n);
		sort(b,b+n);

		int i1 = 0;
		int i2 = 0;
		int h = 0;

		for(i1 = 0; i1 < n; ++i1)
			if(a[i1] > b[i2])
			{
				y++;
				i2++;
			}

		for( int i = n - 1; i >= 0; -- i)
		{
			h = 0;
			for(int j = 0; j < n; ++j)
				if(mark[j] == 0 && b[j] > a[i])
					{
						mark[j] = 1;
						h = 1;
						break;
					}
			if( h == 0 )
				z++;
		}

		cout << "Case #" << tmp << ": "<<y<<" "<<z<<endl;
	}



	return 0;
}