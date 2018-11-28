#include <iostream>
#include <fstream>
using namespace std;

bool break_flag = false;

void flagit(int i, int j, int **lawn, int N, int M, int **flag)
{
	int k;
	bool col = true, row = true;
	for (k=0; k<M; k++)
		if (lawn[i][j] < lawn[i][k])
			row = false;
	for (k=0; k<N; k++)
		if (lawn[i][j] < lawn[k][j])
			col = false;

	if (row && col)
		flag[i][j] = 3;
	else if (row)
		flag[i][j] = 1;
	else if (col)
		flag[i][j] = 2;
	else
		break_flag = true;
}

void main()
{
	fstream fs, fs_out;
	fs.open("input.txt", ios::in);
	fs_out.open("output.txt", ios::out);
	int n;
	fs>>n;
	for (int loop=0; loop<n; loop++)
	{
		break_flag = false;
		int N, M;
		int i, j;
		fs>>N>>M;
		int **lawn;
		int **flag;
		lawn = new int *[N];
		flag = new int *[N];
		for (i=0; i<N; i++)
		{
			lawn[i] = new int [M];
			flag[i] = new int [M];
		}
		for (i=0; i<N; i++)
			for (j=0; j<M; j++)
				fs>>lawn[i][j];

		for (i=0; i<N; i++)
			for (j=0; j<M; j++)
				flagit(i, j, lawn, N, M, flag);

		//for (i=0; i<N; i++)
		//{
		//	for (j=0; j<M; j++)
		//		cout<<flag[i][j]<<' ';
		//	cout<<endl;
		//}

		if (break_flag)
		{
			fs_out<<"Case #"<<loop+1<<": NO"<<endl;
			continue;
		}

		bool check_flag = true;
		for (i=0; i<N; i++)
		{
			bool row = false, col = false;
			for (j=0; j<M; j++)
				if (flag[i][j] == 1)
					row = true;
				else if (flag[i][j] == 2)
					col = true;
			if (row && col)
			{
				check_flag = false;
				break;
			}
		}
		for (j=0; j<M; j++)
		{
			bool row = false, col = false;
			for (i=0; i<N; i++)
				if (flag[i][j] == 1)
					row = true;
				else if (flag[i][j] == 2)
					col = true;
			if (row && col)
			{
				check_flag = false;
				break;
			}
		}

		if (check_flag)
		{
			fs_out<<"Case #"<<loop+1<<": YES"<<endl;
			continue;
		}
		else
		{
			fs_out<<"Case #"<<loop+1<<": NO"<<endl;
		}
	}
	fs.close();
	fs_out.close();
}