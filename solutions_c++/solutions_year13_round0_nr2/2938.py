#include <fstream>
using namespace std;

int T,N,M;
int a[100][100];
int rowflag[100][100];
int colflag[100][100];

void setrow(int rowidx)
{
	int max = -1;
	int c;
	for (c = 0; c < M; c++)
		if(a[rowidx][c] > max)
			max = a[rowidx][c];
	for (c = 0; c < M; c++)
		if(a[rowidx][c] < max)
			rowflag[rowidx][c] = 1;
}

void setcol(int colidx)
{
	int max = -1;
	int r;
	for (r = 0; r < N; r++)
		if(a[r][colidx] > max)
			max = a[r][colidx];
	for (r = 0; r < N; r++)
		if(a[r][colidx] < max)
			colflag[r][colidx] = 1;
}

void main()
{
	ifstream fin;
	ofstream fout;
	fin.open("B-large.in");
	fout.open("3.txt");
	fin >> T;
	for (int i = 0; i < T; i++)
	{
		fin >> N >> M;
		for (int r = 0; r < N; r++)
			for (int c = 0; c < M; c++)
				fin >> a[r][c];
		memset(rowflag,0,sizeof(int)*10000);
		memset(colflag,0,sizeof(int)*10000);
		for (int r = 0; r < N; r++)
			setrow(r);
		for (int c = 0; c < M; c++)
			setcol(c);
		int flag = 0;
		for (int r = 0; r < N; r++)
			for (int c = 0; c < M; c++)
				if (rowflag[r][c] == 1 && colflag[r][c] == 1)
					flag = 1;
		if(flag == 0)
			fout << "Case #" << i+1 << ": YES" << endl;
		else
			fout << "Case #" << i+1 << ": NO" << endl;
	}
	fin.close();
	fout.close();
}