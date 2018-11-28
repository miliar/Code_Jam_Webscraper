#include<iostream>
#include<cstring>
#include<algorithm>
#include<fstream>
using namespace std;

ifstream in ("A.in");
ofstream out("GCJ14QA.out");

int main()
{
	int T, R1, R2, GRID[4][4], i, j, k, ANS, N;
	bool NUMS[17];
	in>>T;
	for ( int i = 1; i <= T; i++ )
	{
		memset(NUMS,false,sizeof(NUMS)); N = 0;
		in>>R1;
		for ( j = 0; j < 4; j++ )
		{
			for ( k = 0; k < 4; k++ )
			{
				in>>GRID[j][k];
				if ( j == R1-1 ) NUMS[GRID[j][k]] = true;
			}
		}
		in>>R2;
		for ( j = 0; j < 4; j++ )
		{
			for ( k = 0; k < 4; k++ )
			{
				in>>GRID[j][k];
				if ( j == R2-1 )
				{
					if ( NUMS[GRID[j][k]] )
					{
						N++;
						ANS = GRID[j][k];
					}
				}
			}
		}
		out<<"Case #"<<i<<": ";
		switch ( N )
		{
			case 0	:	out<<"Volunteer cheated!"<<endl; break;
			case 1	:	out<<ANS<<endl; break;
			default	:	out<<"Bad magician!"<<endl;
		}
		
	}
	return 0;
}
