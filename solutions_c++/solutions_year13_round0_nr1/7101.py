#include <iostream>
#include <vector>
#include <string>
#include <cstdio>
#include <algorithm>
#include <set>
#include <string>
#include <cstdio>
#include <cmath>
#include <queue>
#include <iterator>
#include <climits>
#include <complex>
#include <deque>
#include <iomanip>
#include <map>
using namespace std;

#define X real()
#define Y imag()

typedef complex<double> Point;

int main()
{
	ios_base::sync_with_stdio(false);
	int n;
	cin>>n;
	for(int k = 0 ; k < n ; k ++)
	{
		int o = 0 , x = 0 , dot = 0;
		char ch[4][4];
		for(int i = 0 ; i < 4 ; i ++)
			for(int j = 0 ; j < 4 ; j ++)
			{
				cin>>ch[i][j];
				if(ch[i][j] == '.')
					dot ++;
				if(ch[i][j] == 'X')
					x ++;
				if(ch[i][j] == 'O')
					o ++;
			}
		cout<<"Case #"<<k + 1<<": ";
		int x1 = 0 , o1 = 0 ;
		for(int i = 0 ; i < 4 ; i ++)
		{
			if(ch[0][i] == 'X')
				x1 ++;
			if(ch[0][i] == 'O')
				o1 ++;
			if(ch[0][i] == 'T')
			{
				x1 ++;
				o1 ++;
			}
		}
		if(x1 == 4)
		{
			cout<<"X won"<<endl;
			continue ;
		}
		else if (o1 == 4)
		{
			cout<<"O won"<<endl;
			continue ;
		}
		else
		{
			x1 = 0;
			o1 = 0;
		}
		for(int i = 0 ; i < 4 ; i ++)
		{
			if(ch[i][i] == 'X')
				x1 ++;
			if(ch[i][i] == 'O')
				o1 ++;
			if(ch[i][i] == 'T')
			{
				x1 ++;
				o1 ++;
			}
		}
		if(x1 == 4)
		{
			cout<<"X won"<<endl;
			continue ;
		}
		else if (o1 == 4)
		{
			cout<<"O won"<<endl;
			continue ;
		}
		else
		{
			x1 = 0;
			o1 = 0;
		}
		for(int i = 0 ; i < 4 ; i ++)
		{
			if(ch[i][3 - i] == 'X')
				x1 ++;
			if(ch[i][3 - i] == 'O')
				o1 ++;
			if(ch[i][3 - i] == 'T')
			{
				x1 ++;
				o1 ++;
			}
		}
		if(x1 == 4)
		{
			cout<<"X won"<<endl;
			continue ;
		}
		else if (o1 == 4)
		{
			cout<<"O won"<<endl;
			continue ;
		}
		else
		{
			x1 = 0;
			o1 = 0;
		}
		for(int i = 0 ; i < 4 ; i ++)
		{
			if(ch[1][i] == 'X')
				x1 ++;
			if(ch[1][i] == 'O')
				o1 ++;
			if(ch[1][i] == 'T')
			{
				x1 ++;
				o1 ++;
			}
		}
		if(x1 == 4)
		{
			cout<<"X won"<<endl;
			continue ;
		}
		else if (o1 == 4)
		{
			cout<<"O won"<<endl;
			continue ;
		}
		else
		{
			x1 = 0;
			o1 = 0;
		}
		for(int i = 0 ; i < 4 ; i ++)
		{
			if(ch[2][i] == 'X')
				x1 ++;
			if(ch[2][i] == 'O')
				o1 ++;
			if(ch[2][i] == 'T')
			{
				x1 ++;
				o1 ++;
			}
		}
		if(x1 == 4)
		{
			cout<<"X won"<<endl;
			continue ;
		}
		else if (o1 == 4)
		{
			cout<<"O won"<<endl;
			continue ;
		}
		else
		{
			x1 = 0;
			o1 = 0;
		}
		for(int i = 0 ; i < 4 ; i ++)
		{
			if(ch[3][i] == 'X')
				x1 ++;
			if(ch[3][i] == 'O')
				o1 ++;
			if(ch[3][i] == 'T')
			{
				x1 ++;
				o1 ++;
			}
		}
		if(x1 == 4)
		{
			cout<<"X won"<<endl;
			continue ;
		}
		else if (o1 == 4)
		{
			cout<<"O won"<<endl;
			continue ;
		}
		else
		{
			x1 = 0;
			o1 = 0;
		}
		for(int i = 0 ; i < 4 ; i ++)
		{
			if(ch[i][0] == 'X')
				x1 ++;
			if(ch[i][0] == 'O')
				o1 ++;
			if(ch[i][0] == 'T')
			{
				x1 ++;
				o1 ++;
			}
		}
		if(x1 == 4)
		{
			cout<<"X won"<<endl;
			continue ;
		}
		else if (o1 == 4)
		{
			cout<<"O won"<<endl;
			continue ;
		}
		else
		{
			x1 = 0;
			o1 = 0;
		}
		for(int i = 0 ; i < 4 ; i ++)
		{
			if(ch[i][1] == 'X')
				x1 ++;
			if(ch[i][1] == 'O')
				o1 ++;
			if(ch[i][1] == 'T')
			{
				x1 ++;
				o1 ++;
			}
		}
		if(x1 == 4)
		{
			cout<<"X won"<<endl;
			continue ;
		}
		else if (o1 == 4)
		{
			cout<<"O won"<<endl;
			continue ;
		}
		else
		{
			x1 = 0;
			o1 = 0;
		}
		for(int i = 0 ; i < 4 ; i ++)
		{
			if(ch[i][2] == 'X')
				x1 ++;
			if(ch[i][2] == 'O')
				o1 ++;
			if(ch[i][2] == 'T')
			{
				x1 ++;
				o1 ++;
			}
		}
		if(x1 == 4)
		{
			cout<<"X won"<<endl;
			continue ;
		}
		else if (o1 == 4)
		{
			cout<<"O won"<<endl;
			continue ;
		}
		else
		{
			x1 = 0;
			o1 = 0;
		}
		for(int i = 0 ; i < 4 ; i ++)
		{
			if(ch[i][3] == 'X')
				x1 ++;
			if(ch[i][3] == 'O')
				o1 ++;
			if(ch[i][3] == 'T')
			{
				x1 ++;
				o1 ++;
			}
		}
		if(x1 == 4)
		{
			cout<<"X won"<<endl;
			continue ;
		}
		else if (o1 == 4)
		{
			cout<<"O won"<<endl;
			continue ;
		}
		else
		{
			x1 = 0;
			o1 = 0;
		}
		if(dot == 0)
			cout<<"Draw"<<endl;
		else
			cout<<"Game has not completed"<<endl;
	}
}