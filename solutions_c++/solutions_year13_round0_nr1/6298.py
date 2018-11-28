#include<iostream>

struct Cell
{
	int pos;		//T: 0 X: 1 O : 2, . : -1
	char inp;
};

using namespace std;

int main()
{

	Cell cell[4][4];

	
	int testcases;
	cin >> testcases;


	for(int t = 1; t<= testcases ; ++t)
	{
	

	for(int i = 0; i<4; ++i)
	{
		for(int j = 0; j<4; ++j)
		{
			cin>>cell[i][j].inp;
			
			switch(cell[i][j].inp)
			{
				case '.'	:	cell[i][j].pos = -1;
							break;
				case 'X'	:	cell[i][j].pos = 1;
							break;
				case 'O'	:	cell[i][j].pos = 2;
							break;
				case 'T'	:	cell[i][j].pos = 0;
			}
		}
	}

	
	int rx=0, cx = 0, d1x = 0, d2x = 0,  ro=0,  co = 0, d1o =0, d2o = 0, full=0;
	int status = 0; 	// 0: Game Not Complete, 1: X, 2: 0, 3: Draw

	for(i=0; i<4; ++i)
	{
		rx = 0, cx = 0;
		ro  =0, co = 0;
		
		for(int j =0; j<4; ++j)
		{
			if(cell[i][j].pos == 0 || cell[i][j].pos == 1)
				rx++;
			if(cell[i][j].pos == 0 || cell[i][j].pos == 2)
				ro++;

			if(cell[j][i].pos == 0 || cell[j][i].pos == 1)
				cx++;
			if(cell[j][i].pos == 0 || cell[j][i].pos == 2)
				co++;


			if(i == j)
			{
				if(cell[i][j].pos == 0 || cell[i][j].pos == 1)
					d1x++;
				if(cell[i][j].pos == 0 || cell[i][j].pos == 2)
					d1o++;
			}

			else if (i + j == 3)
			{
				if(cell[i][j].pos == 0 || cell[i][j].pos == 1)
					d2x++;
				if(cell[i][j].pos == 0 || cell[i][j].pos == 2)
				{
					d2o++;
				}
			}

			if(cell[i][j].pos >=0)
				full++;
		}

		if(rx == 4 || cx == 4 || d1x == 4 || d2x == 4)
		{
			status = 1;
			break;
		}

		else if(ro == 4 || co == 4|| d1o == 4 || d2o == 4)
		{
			status = 2;
			break;
		}
	}

	if(full == 16 && status == 0)
		status = 3;

	cout<<"Case #"<<t<<": ";
	switch(status)
	{
		case 0 	:	cout<<"Game has not completed"<<endl;
				break;
		case 1	:	cout<<"X won"<<endl;
				break;
		case 2	:	cout<<"O won"<<endl;
				break;
		case 3	:	cout<<"Draw"<<endl;
				break;
	}

	}

	return 0;
}
