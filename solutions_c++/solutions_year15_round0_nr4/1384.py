#include <bits/stdc++.h>
using namespace std;
#define int long long
main()
{
	freopen("in.txt", "r", stdin); 
	freopen("out.txt", "w", stdout); 
	int a; cin >> a;
	for (int g=0; g<a; g++)
	{
		cout << "Case #"<< g+1 << ": "; 
		int b,c,d; cin >> d >> b >> c;
		if ((b*c)%d)
		{
			cout << "RICHARD" << '\n'; continue; 
		}
		if (b>c) swap(b, c); 
		if (c==4)
		{
			if (b==4)
			{
				cout << "GABRIEL" << '\n'; 
			}
			else if (b==3)
			{
				cout << "GABRIEL" << '\n'; 
			}
			else if (b==2)
			{
				if (d==4)
				cout << "RICHARD" << '\n'; 
				else cout << "GABRIEL" << '\n';
			}
			else if (b==1)
			{
				if (d==4)
				cout << "RICHARD" << '\n';
				else cout << "GABRIEL" << '\n';  
			}
		}
		else if (c==3)
		{
			if (b==3)
			{
				cout << "GABRIEL" << '\n'; 
			}
			else if (b==2)
			{
				cout << "GABRIEL" << '\n'; 
			}
			else
			{
				if (d==3)
				{
					cout << "RICHARD" << '\n'; 
				}
				else cout << "GABRIEL" << '\n'; 
			}
		}
		else if (c==2)
		{
			if (b==2)
			{
				if (d==4) cout << "RICHARD" << '\n'; 
				else cout << "GABRIEL" << '\n'; 
			}
			else
			{
				cout << "GABRIEL" << '\n'; 
			}
		}
		else
		{
			cout << "GABRIEL" << '\n'; 
		}
	}
	return 0; 
}
