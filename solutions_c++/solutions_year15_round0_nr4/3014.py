#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;
int main()
{
	int t = 0, T;
	cin>>T;
	while(t++ < T)
	{
		int x, r, c;
		cin>>x>>r>>c;
		cout<<"Case #"<<t<<": "; 
		if(x == 1)
		{
			cout<<"GABRIEL\n";
			continue;
		}
		if(x == 2)
		{
			if(r * c % 2)
			{
				cout<<"RICHARD\n";
				continue;
			}
			cout<<"GABRIEL\n";
			continue;
		}
		if(x == 3)
		{
			if((r == 3 && c == 2) ||
			   (r == 2 && c == 3) ||
			   (r == c && r == 3) ||
			   (r == 3 && c == 4) ||
			   (r == 4 && c == 3) )
			{
				cout<<"GABRIEL\n";
				continue;
			}
			cout<<"RICHARD\n";
			continue;
		}
		if(x == 4)
		{
			if((r == c && c == 4) ||
			   (r == 3 && c == 4) ||
			   (r == 4 && c == 3))
			{
				cout<<"GABRIEL\n";
				continue;
			}
			
			cout<<"RICHARD\n";

		}
	}
	return 0;
}
