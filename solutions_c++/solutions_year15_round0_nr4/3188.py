#include <iostream>
#include <vector>

using namespace std;

int main()
{
	int tc;
	cin >> tc;
	int g[65];
	for (int i =0; i< tc; i++)
	{		
		g[i] =0;
		int x,r,c;
		cin >> x;
		cin >> r;
		cin >> c;
		switch(x)
		{
			case 1: 
				g[i] = 1; 
				break;
			case 2:
				if (r%2==0 || c%2==0) g[i] = 1;
				break;
			case 3: 
				if (((r*c)%3==0) && r!=1 && c!=1) g[i]=1;
				break;
			case 4:
				if (((r*c)%4==0) && r>=3 && c>=3) g[i]=1;
				break;				
		}		
	}
	for (int i = 0; i < tc; ++i)
	{
		if(g[i] == 1)
			cout << "Case #" << (i+1) << ": " << "GABRIEL" <<endl;
		else
			cout << "Case #" << (i+1) << ": " << "RICHARD" <<endl;		
	}
	return 0;
}
