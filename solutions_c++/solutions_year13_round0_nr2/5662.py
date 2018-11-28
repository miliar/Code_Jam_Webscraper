#include <iostream>
#include <fstream>

using namespace std;

ifstream fin("B-small-attempt7.in");
ofstream fout("B-small-attempt7.out");

//ifstream fin("input.txt");
//ofstream fout("output.txt");

int T,N,M;
int map[12][12] = {0,};
int sum = 0;


int main()
{
	int i,j,z;
	int flag;
	int edge_cnt,edge_enter;

	fin >> T;

	//T =1;
	for(z=1;z<=T;z++)
	{
		fin >> N >> M;

		//data input
		flag = 0;
		edge_cnt  = edge_enter = 0;

		for(i=1;i<=N;i++)
		{
			for(j=1;j<=M;j++)
			{
				fin >> map[i][j];

				if(map[i][j] == 1)
				{
					map[i][M+1] += 1;
					map[N+1][j] += 1;
				}
			}
		}

		for(i=1;i<=N;i++)
		{
		
			for(j=1;j<=M;j++)
			{
				if( ((i == 1 || j == 1) || (i == N || j == M)) && map[i][j] < 2)
				{	// 모서리에 1 이 가능한 패턴인지?? 

					if(map[i][M+1] == M)
					{
						for(int e=1;e<=M;e++)
							map[i][e] = 0;
					}
					
					if(map[N+1][j] == N)
					{
						for(int e=1;e<=N;e++)
							map[e][j] = 0;
					}
				}
			}
					
		}

		for(i=1;i<=N;i++)
		{
			if(flag == 1)
				break;

			for(j=1;j<=M;j++)
			{
				if(map[i][j] == 1)
				{
					flag = 1;
					break;
				}
			}
		}

		if(flag == 1)
			fout << "Case #" << z << ": NO" <<endl;
		else
			fout << "Case #" << z << ": YES" <<endl;


		
		for(i=1;i<=N+1;i++)
		{
			for(j=1;j<=M+1;j++)
			{
				//cout << map[i][j] << " ";
				map[i][j] = 0;
			}
			//cout << endl;
		}
		
	}
	return 0;
}

