// GoogleCodeJam_2013_Second.cpp : 콘솔 응용 프로그램에 대한 진입점을 정의합니다.
//

//#include "stdafx.h"


#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>


using namespace std;

int main(int argc, char * argv[])
{
	ifstream in;
	ofstream out;

	int iPro;
	int	M, N;

	vector<int> map;
	vector<int> premap;
	
	int i,j,k,l;

	int row[10];
	int col[10];

	in.open("B-small-attempt1.in");
	
	out.open("out_2.text");

	in >> iPro;

	for ( k=1;k<=iPro;k++)
	{
		in >> M >> N;

		map.clear();
		premap.clear();

		int temp;

		for ( i=0; i< M*N;i++)
		{
			in >> temp;
			map.push_back(temp);
			premap.push_back(100);
		}

		// input end

		for ( i=0; i<M;i++)
		{
			int dest = 100;
			row[i] = 100;

			for ( j=0; j<N;j++)
			{
				if ( dest == 100 ) dest = map[i*N+j];
				else
				if ( dest < map[i*N+j] ) dest = map[i*N+j]; 
			}

			if ( dest != 0 && dest < 100 )
			{
				row[i] = dest;
			}
		}

		for ( i=0; i<N;i++)
		{
		
			int dest = 100;

			for ( j=0; j<M;j++)
			{
				if ( dest == 100 ) dest = map[j*N+i];
				else
				if ( dest < map[j*N+i] ) dest = map[j*N+i]; 
			}

			if ( dest != 0 && dest < 100 )
			{
				col[i] = dest;
			}
		}

		for (l=100-1;l>0;l--)
		{
			for (i=0;i<M;i++)
			{
				if ( row[i] == l )
				{
					for (j=0;j<N;j++)
					{
						premap[i*N+j] = row[i];
					}
				}
			}

			for (j=0;j<N;j++)
			{
				if ( col[j] == l )
				{
					for (i=0;i<M;i++)
					{
						premap[i*N+j] = col[j];
					}
				}
			}

		}

		// output start
		
		out << "Case #" << k << ": " ;

		for ( i=0;i<M*N;i++)
		{
			if ( map[i]!=premap[i])
			{
				out << "NO" << endl;
				break;
			}
		}

		if (i==M*N)
			out << "YES" <<endl;
	}


	return 0;
}

