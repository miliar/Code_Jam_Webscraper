#include <bits/stdc++.h>

using namespace std;

int main()
{
	freopen ("D-small-attempt2.in.txt" , "r" , stdin);
	freopen ("D-small.txt" , "w" , stdout);
	
	int t , x , r ,c;
	cin >> t;
	for(int i = 1 ; i <= t ; i++)
	{
		cin >> x >> r >> c;
		if( x == 1)
		{
			cout<< "Case #" << i << ": GABRIEL\n";
		}else if (x == 2)
		{
			if(c % 2 == 0 || r % 2 == 0)
			{
			 	cout<< "Case #" << i << ": GABRIEL\n";
			}else 
			{
				cout<< "Case #" << i << ": RICHARD\n";	
			}
		}else if (x == 3)
		{
			if( r*c % 3 == 0 && c > 1 && r > 1)
			{
				cout<< "Case #" << i << ": GABRIEL\n";	
			}else
			{
			    cout<< "Case #" << i << ": RICHARD\n";	
			}
		}else
		{
			if( r*c % 4 == 0 && c > 2 && r > 2)
			{
				cout<< "Case #" << i << ": GABRIEL\n";	
			}else
			{
				cout<< "Case #" << i << ": RICHARD\n";	
			}
		}
	}




	return 0;
}