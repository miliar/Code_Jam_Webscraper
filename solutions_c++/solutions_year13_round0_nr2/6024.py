#include <iostream>
#include <string>
#include <fstream>
#include <sstream>

using namespace std;

int main()
{
	ifstream infile("B-small-attempt2.in");
	ofstream outfile("out.txt");
	int T, flag;
	int rowflag, cflag;
	int N, M;
	int lawn[10][10];
	infile>>T;
	for(int i = 0; i < T; ++i)
	{
		flag = 0;
		rowflag = 0;
		cflag = 0;
		infile>>N;
		infile>>M;
		for(int t = 0; t < N; ++t)
		{
			for(int k = 0; k < M; ++k)
			{
				infile>>lawn[t][k];
			}
		}
		//row
		for(int t = 0; t < N; ++t)
		{
			for(int k = 0; k < M; ++k)
			{
				if(lawn[t][k] == 2)
				{
					rowflag = 1;
					continue;
				}
				if(rowflag)
				{
					int r = 0;
					int temp = lawn[r][k];
					r++;
					while(temp == lawn[r][k] && r < N)
						r++;
					if(r < N)
					{
						stringstream ss;
						flag = 1;
						ss<<"Case #"<<i + 1<<": "<<"NO"<<endl;
						outfile<<ss.str().c_str();
						break;
					}
				}
				else
				{
					int m = 0;
					int tem = lawn[t][m];
					m++;
					while(tem == lawn[t][m] && m < M)
						m++;
					if(m < M)
					{
						int r = 0;
						int temp = lawn[r][k];
						r++;
						while(temp == lawn[r][k] && r < N)
							r++;
						if(r < N)
						{
							stringstream ss;
							flag = 1;
							ss<<"Case #"<<i + 1<<": "<<"NO"<<endl;
							outfile<<ss.str().c_str();
							break;
						}
					}
				}
			}
			if(flag)
				break;
			rowflag = 0;
		}
		if(flag == 0)
		{
			stringstream ss1;
			ss1<<"Case #"<<i + 1<<": "<<"YES"<<endl;
			outfile<<ss1.str().c_str();
		}
	}
	infile.close();
	outfile.close();
	return 0;
}