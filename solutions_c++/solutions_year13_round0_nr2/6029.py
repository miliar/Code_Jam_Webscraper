#include <iostream>
#include <conio.h>
#include <fstream>
int r, c, i, j, k;
int a[10][10] = {0};
int check(int r, int c)				
{
	int max = 0;
	if(r == 1 || c == 1)
		return 1;
	for(i = 0; i < r; i++)
	{
		max = a[i][0];
		for(j = 0; j < c; j++)
		{
			//if(a[i][0] == 1)
			if(a[i][j] < max)
			{
				for(k = 0; k < r; k++)
				{
					if(a[k][j] == a[0][j])
						continue;
					else
						return 0;
				}
				//max = a[i][j];
			}

			else if(a[i][j] > max)
			{
				for(k = 0; k < r; k++)
				{
					if(a[k][j-1] == a[0][j-1])
						continue;
					else
						return 0;
				}
				max = a[i][j];
			}
			
		}
	
	}
	return 1;
}

int main()
{
	int T, cnt = 0; 
	std::ifstream in;
	std::ofstream out;
	in.open("B-small-attempt1.in");
	out.open("B-small-attempt1.out");
	if(in.is_open() && out.is_open())
	{
			in>>T;
			while(T--)
			{
				cnt++;
				in>>r;
				in>>c;
				//flag = 0;
				for(i = 0; i < r; i++)
					for(j = 0; j < c; j++)
						in>>a[i][j];
				k = check(r,c);
				if(k == 0)
					out<<"Case #"<<cnt<<": NO\n";
				else
					out<<"Case #"<<cnt<<": YES\n";
			}
	}
	getch();
}