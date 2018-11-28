#include<stdio.h>
#include<iostream>
#include<conio.h>
using namespace std;
int main()
{
	int t, f = 1,x,r,c,flag=0;
	char * tak = { "GABRIEL" };
	char * giv = { "RICHARD" };
	cin >> t;
	while (t > 0)
	{
		cin >> x >> r >> c;
		if (r < x && c < x)
		{
			flag = 1;// 1 is for givr
		}
		else if (x==1)
		{
			flag = 0;
		}
		else
		{
			if (x == 4)
			{
				if (r == 4 && c == 4)
					flag = 0;
				else if ((r == 3 && c == 4) || (r == 4 && c == 3))
					flag = 0;
				else
					flag = 1;
			}
			if (x == 3)
			{
				if (r == 3 && c == 3)
					flag = 0;
				else if ((r == 3 && c == 4) || (r == 4 && c == 3))
					flag = 0;
				else if ((r == 2 && c == 3) || (r == 3 && c == 2))
					flag = 0;
				else
					flag = 1;

			}
			if (x == 2)
			{
				if (r == 4 && c == 4)
					flag = 0;
				else if (r == 2 && c == 2)
					flag = 0;
				else if ((r == 2 && c == 1) || (r == 1 && c == 2))
					flag = 0;
				else if ((r == 2 && c == 3) || (r == 3 && c == 2))
					flag = 0;
				else if ((r == 1 && c == 4) || (r == 4 && c == 1))
					flag = 0;
				else if ((r == 3 && c == 4) || (r == 4 && c == 3))
					flag = 0;
				else if ((r == 2 && c == 4) || (r == 4 && c == 2))
					flag = 0;
				else
					flag = 1;
			}
		}
		if (flag==1)
		printf("Case #%d: %s\n", f++, giv);
		else
			printf("Case #%d: %s\n", f++, tak);
		t--;
	}
	_getch();
	return 0;
}