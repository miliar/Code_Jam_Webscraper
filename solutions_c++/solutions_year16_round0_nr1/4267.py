
#include <iostream>

#include <vector>
#include <string>


using namespace std;


int main( int, const char*[] )
{

	int test_num;
	cin >> test_num;

	for( int test=0; test<test_num; ++test )
	{
		int v;
		cin >> v;

		int d[10] = { 0 };
		int c = 0;

		int res = 0;
		for( int i=0; i<100; ++i )
		{
			const int vv = v*(i+1);
			int vvc = vv;
			while( vvc > 0 )
			{
				const int dd = vvc%10;
				if ( d[dd] == 0 )
				{
					++c;
					if ( c == 10 )
					{
						res = vv;
						break;
					}
				}
				d[dd] = 1;
				vvc /= 10;
			}
			if ( res > 0 ) break;
		}

		cout << "Case #" << (test+1) << ": ";
		if ( res )
		{ cout << res; }
		else
		{ cout << "INSOMNIA"; }
		cout << endl;
	}

	return 0;
}

