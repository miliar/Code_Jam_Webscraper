#include<iostream>
using namespace std;
bool sheep[10];
int main()
{
	int n;
	cin >> n;
	int m=n, a, all=0, x=0, ct=0;
	while ( n-- )
	{
		for ( int i=0; i<10; i++ )
			sheep[i] = false;
		all=0, x=0, ct=0;
		bool gt=true;
		cin >> a;
		if ( a == 0 )
			cout << "Case #" << m-n << ": INSOMNIA" << endl; 
		else
		{
			while ( gt )
			{
				ct = a*(x+1);
				x++;
				while ( ct > 0 )
				{
					if ( sheep[ct%10]==false )
						all++;
					sheep[ct%10] = true;
					ct /= 10;
				}
				if ( all >= 10 )
				{
					gt = false;
					x *= a;
				}
			}
			cout << "Case #" << m-n << ": " << x << endl;
		}
	}
	return 0;
}

