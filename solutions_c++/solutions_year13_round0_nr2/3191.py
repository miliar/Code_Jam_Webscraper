#include <iostream>
#include <fstream>

#define N_MAX 100
#define M_MAX 100
#define A_MAX 100

using namespace std;

int T;
int N, M;
	

int checkHorizon(int data[N_MAX][M_MAX], int y, int n)
{
	for(int i=0; i<M; i++)
	{
		if(data[y][i] > n)
		{
			return 0;
		}
	}

	return 1;
}

int checkVertical(int data[N_MAX][M_MAX], int x, int n)
{
	for(int i=0; i<N; i++)
	{
		if(data[i][x] > n)
		{
			return 0;
		}
	}

	return 1;
}

void lawnHorizon(int data[N_MAX][M_MAX], int y, int n)
{
	for(int i=0; i<M; i++)
	{
		data[y][i] = n;
	}
}

void lawnVertical(int data[N_MAX][M_MAX], int x, int n)
{
	for(int i=0; i<N; i++)
	{
		data[i][x] = n;
	}
}

int equalsData(int input[N_MAX][M_MAX], int output[N_MAX][M_MAX])
{
	for(int i=0; i<N; i++)
	{
		for(int j=0; j<	M; j++)
		{
			if(input[i][j] != output[i][j])
				return 0;
		}
	}

	return 1;
}

int main()
{
//	int T;
//	int N, M;
	int input[N_MAX][M_MAX];
	int output[N_MAX][M_MAX];

	ifstream fin;
	ofstream fout;

	//fin = ifstream("input.txt");
	//fout = ofstream("output.txt");
	fin = ifstream(stdin);
	fout = ofstream(stdout);

	fin>>T;

	for(int count=1; count<=T; count++)
	{
		fin>>N>>M;

		for(int i=0; i<N; i++)
		{
			for(int j=0; j<M; j++)
			{
				fin>>input[i][j];
			}
		}


		for(int a=A_MAX; a>0; a--)
		{
			for(int i=0; i<N; i++)
			{
				if(checkHorizon(input, i, a))
					lawnHorizon(output, i, a);
			}
			for(int i=0; i<M; i++)
			{
				if(checkVertical(input, i, a))
					lawnVertical(output, i, a);
			}
		}

		
		if(equalsData(input, output))
			fout << "Case #" << count << ": " << "YES" << endl;
		else
			fout << "Case #" << count << ": " << "NO" << endl;
	}

	return 0;
}