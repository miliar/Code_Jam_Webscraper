#include<fstream>
#include<iostream>
#include<string>
using namespace std;
void main()
{
	ifstream infile;
	ofstream outfile;

	infile.open("A-small.in");
	outfile.open("out-A.txt");
	
	char c;
	bool x[4][4], o[4][4];
	int n, l, m, j = 0;
	bool incomplete = 0, xwon = 0, owon = 0;

	infile >> n;

	while(j < n)
	{
		for(l = 0; l < 4; l++)
		{	
			for(m = 0; m < 4; m++)
			{
				x[l][m] = 0;
				o[l][m] = 0;
			}
		}
		xwon = 0;
		owon = 0;
		incomplete = 0;
		l = 0;
		m = 0;
		for(l = 0; l < 4; l++)
		{	
			for(m = 0; m < 4; m++)
			{
				infile >> c;
				if(c == '.')
					incomplete = 1;
				if(c == 'X')
					x[l][m] = 1;
				if(c == 'O')
					o[l][m] = 1;
				if(c == 'T')
				{
					x[l][m] = 1;
					o[l][m] = 1;
				}
			}
		}
		for(l = 0; l < 4; l++)
		{
			for(m = 0; m < 4; m++)
			{
				cout << o[l][m] << " ";
			}
			cout << endl;
		}
		system("pause");
		cout << incomplete << endl;
		system("pause");
		m = 0;
		for(l = 0; l < 4; l++)
		{	
			if(x[l][m])
			{
				if(x[l][m+1])
				{
					if(x[l][m+2])
					{
						if(x[l][m+3])
							xwon = 1;
					}
				}
			}
			if(xwon)
				break;
		}

		cout << xwon << endl;
		system("pause");
		l = 0;
		if(!xwon)
		{
			for(m = 0; m < 4; m++)
			{
				if(x[l][m])
				{
					if(x[l+1][m])
					{
						if(x[l+2][m])
						{
							if(x[l+3][m])
								xwon = 1;
						}
					}
				}
				if(xwon)
					break;
			}
		}
		cout << xwon << endl;
		system("pause");
		l = 0; m = 0;
		if(!xwon)
		{
			if(x[0][0])
			{
				if(x[1][1])
				{
					if(x[2][2])
					{
						if(x[3][3])
							xwon = 1;
					}
				}
			}
		}
		cout << xwon << endl;system("pause");
		if(!xwon)
		{
			if(x[0][3])
			{
				if(x[1][2])
				{
					if(x[2][1])
					{
						if(x[3][1])
							xwon = 1;
					}
				}
			}
		}
		cout << xwon << endl;system("pause");
		for(l = 0; l < 4; l++)
		{	
			if(o[l][m])
			{
				if(o[l][m+1])
				{
					if(o[l][m+2])
					{
						if(x[l][m+3])
							owon = 1;
					}
				}
			}
			if(owon)
				break;
		}
		l = 0;
		cout << owon << endl;system("pause");
		if(!owon)
		{
			for(m = 0; m < 4; m++)
			{
				if(o[l][m])
				{
					if(o[l+1][m])
					{
						if(o[l+2][m])
						{
							if(o[l+3][m])
								owon = 1;
						}
					}
				}
				if(owon)
					break;
			}
		}	
		l = 0; m = 0;
		cout << owon << endl;system("pause");
		if(!owon)
		{
			if(o[0][0])
			{
				if(o[1][1])
				{
					if(o[2][2])
					{
						if(o[3][3])
							owon = 1;
					}
				}
			}
		}
		cout << owon << endl;system("pause");
		if(!owon)
		{
			if(o[0][3])
			{
				if(o[1][2])
				{
					if(o[2][1])
					{
						if(o[3][0])
							owon = 1;
					}
				}
			}
		}
		cout << owon << endl;system("pause");
		outfile << "Case #" << j+1 << ": ";
		if(xwon)
		{
			outfile << "X won" << endl;
		}
		else if(owon)
		{
			outfile << "O won" << endl;
		}
		else if(!incomplete)
		{
			outfile << "Draw" << endl;
		}
		else outfile << "Game has not completed" << endl;
		j++;
	}
}