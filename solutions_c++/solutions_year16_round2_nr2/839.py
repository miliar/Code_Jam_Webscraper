#include <bits/stdc++.h>
using namespace std;

int main()
{
	int t, tc = 0;
	cin >> t;
	while( t -- )
	{
		string a, b;
		cin >> a >> b;
		cout << "Case #" << ++tc << ": ";
		if( a.size() == 1 )
		{
			if( a[0] == '?' )
				if( b[0] == '?' )
					cout << "0 0" << endl;
				else
					cout << b[0] << " " << b[0] << endl;
			else
				if( b[0] == '?' )
					cout << a[0] << " " << a[0] << endl;
				else
					cout << a[0] << " " << b[0] << endl;
		}
		else if( a.size() == 2 )
		{
			int l1[2], l2[2], u1[2], u2[2];
			int ss1, ss2, mn = 10000;
			if( a[0] == '?' )
				l1[0] = 0, u1[0] = 9;
			else
				l1[0] = u1[0] = a[0]-'0';
			if( a[1] == '?' )
				l1[1] = 0, u1[1] = 9;
			else
				l1[1] = u1[1] = a[1]-'0';
			if( b[0] == '?' )
				l2[0] = 0, u2[0] = 9;
			else
				l2[0] = u2[0] = b[0]-'0';
			if( b[1] == '?' )
				l2[1] = 0, u2[1] = 9;
			else
				l2[1] = u2[1] = b[1]-'0';
			for( int i1 = l1[0] ; i1 <= u1[0] ; i1 ++ )
				for( int i2 = l1[1] ; i2 <= u1[1] ; i2 ++ )
					for( int j1 = l2[0] ; j1 <= u2[0] ; j1 ++ )
						for( int j2 = l2[1] ; j2 <= u2[1] ; j2 ++ )
						{
							int s1 = i1 * 10 + i2;
							int s2 = j1 * 10 + j2;
							if( abs( s1-s2 ) < mn )
								mn = abs( s1-s2 ), ss1 = s1, ss2 = s2;
							else if( abs( s1-s2 ) == mn )
							{
								if( s1 < ss1 )
									ss1 = s1, ss2 = s2;
								else if( s1 == ss1 && s2 < ss2 )
									ss1 = s1, ss2 = s2;
							}
						}
			printf( "%02d %02d\n", ss1, ss2 );
		}
		else
		{
			int l1[3] = {0,0,0}, u1[3] = {9,9,9};
			int l2[3] = {0,0,0}, u2[3] = {9,9,9};
			int ss1, ss2, mn = 10000;
			for( int i = 0 ; i < 3 ; i ++ )
			{
				if( a[i] != '?' )
					l1[i] = u1[i] = a[i]-'0';
				if( b[i] != '?' )
					l2[i] = u2[i] = b[i]-'0';
			}
			for( int i1 = l1[0] ; i1 <= u1[0] ; i1 ++ )
				for( int i2 = l1[1] ; i2 <= u1[1] ; i2 ++ )
					for( int i3 = l1[2] ; i3 <= u1[2] ; i3 ++ )
						for( int j1 = l2[0] ; j1 <= u2[0] ; j1 ++ )
							for( int j2 = l2[1] ; j2 <= u2[1] ; j2 ++ )
								for( int j3 = l2[2] ; j3 <= u2[2] ; j3 ++ )
								{
									int s1 = i1 * 100 + i2 * 10 + i3;
									int s2 = j1 * 100 + j2 * 10 + j3;
									if( abs( s1-s2 ) < mn )
										mn = abs( s1-s2 ), ss1 = s1, ss2 = s2;
									else if( abs( s1-s2 ) == mn )
									{
										if( s1 < ss1 )
											ss1 = s1, ss2 = s2;
										else if( s1 == ss1 && s2 < ss2 )
											ss1 = s1, ss2 = s2;
									}
								}
			printf( "%03d %03d\n", ss1, ss2 );
		}
	}
	return 0;
}
