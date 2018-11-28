#include<iostream>
#include<fstream>
#include<memory.h>
#include<vector>
#include<limits>

using namespace std;

int x[4][4];
int o[4][4];
int dot[4][4];

const char * s[] = {"X won","O won","Draw","Game has not completed"};

int main()
{
	ifstream in("input.txt");
	ofstream out("output.txt");
	vector<string> result(s,s+4);
	string next;
	char nn;
	int row,col;
	int flag = -1;
	
	int T;
	in>>T;
	for(int t = 1;t<=T;t++)
	{
		flag = -1;
		for(int i = 0;i<4;i++)
		{
			memset(x[i],0,4*sizeof(int));
			memset(o[i],0,4*sizeof(int));
			memset(dot[i],0,4*sizeof(int));
		}
		if(t!=1)
		in.get(nn);//empty line

		for(int i = 0;i<4;i++)
		{
			in>>next;
			for(int j = 0;j<4;j++)
			{
				if(next[j] == 'X')
					x[i][j] = 1;
				else if(next[j] == 'O')
					o[i][j] = 1;
				else if(next[j] == '.')
					dot[i][j] = 1;
				else 
				{
					row = i;
					col = j;
					x[i][j] = 1;
					o[i][j] = 1;
				}
			}
		}
		for(int i = 0;i<4;i++)
		{
			if((x[i][0] == 1 &&x[i][1] == 1 && x[i][2] == 1&&x[i][3] == 1)||(x[0][i] == 1&&x[1][i] == 1&&x[2][i] == 1&&x[3][i] == 1))
			{
				flag = 0;
				break;
			}

			if((o[i][0] == 1 &&o[i][1] == 1 && o[i][2] == 1&&o[i][3] == 1)||(o[0][i] == 1&&o[1][i] == 1&&o[2][i] == 1&&o[3][i] == 1))
			{
				flag = 1;
				break;
			}
		}
		if(flag != -1)
		{
			out<<"Case #"<<t<<": "<<result[flag]<<endl;
			continue;
		}
		if((x[0][0] ==1 && x[1][1] == 1&&x[2][2] == 1&&x[3][3] == 1)||(x[0][3]==1&&x[1][2] == 1&&x[2][1]==1&&x[3][0]==1)) 
		{
			flag = 0;
		}
		if((o[0][0] ==1 && o[1][1] == 1&&o[2][2] == 1&&o[3][3] == 1)||(o[0][3]==1&&o[1][2] == 1&&o[2][1]==1&&o[3][0]==1)) 
		{
			flag = 1;
		}
		if(flag != -1)
		{
			out<<"Case #"<<t<<": "<<result[flag]<<endl;
			continue;
		}
		for(int i = 0;i<4;i++)
			for(int j = 0;j<4;j++)
				if(dot[i][j] == 1)
				{
					flag = 3;
					i =4;
					break;
				}
		if(flag != -1)
			out<<"Case #"<<t<<": "<<result[flag]<<endl;
		else
			out<<"Case #"<<t<<": "<<result[2]<<endl;
	}

}
