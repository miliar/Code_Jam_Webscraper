#include <iostream>
#include <fstream>
using namespace std;

#define T_MAX 100
#define N 4

int DetCard( int ans1, int arr1[][N], int ans2, int arr2[][N] )
{
	int *row1 = arr1[ans1-1];
	int *row2 = arr2[ans2-1];
	int i, j;
	int same = 0;
	int sameCard = 0;
	for ( i = 0; i < N; i++ )
	{
		for ( j = 0; j < N; j++ )
		{
			if( row1[i] == row2[j] )
			{
				same++;
				sameCard = row1[i];
			}
		}
	}
	if ( same == 0 ) return 0;
	if ( same == 1 ) return sameCard;
	return -1;
}

void main()
{
	ifstream fin( "A-small-attempt2.in" );
	ofstream fout( "A-small-attempt2.out" );
	int T;
	fin>>T;
	int ans1[T_MAX], ans2[T_MAX];
	int arr1[T_MAX][N][N], arr2[T_MAX][N][N];
	int t, i;
	for ( t = 0; t < T; t++ )
	{
		fin>>ans1[t];
		for( i = 0; i < N*N; i++ )
		{
			fin>>arr1[t][i%4][i-i%4*4];
		}
		fin>>ans2[t];
		for( i = 0; i < N*N; i++ )
		{
			fin>>arr2[t][i%4][i-i%4*4];
		}
	}
	int same;
	for ( t = 0; t < T; t++ )
	{
		fout<<"Case #"<<t+1<<": ";
		same = DetCard( ans1[t], arr1[t], ans2[t], arr2[t] );
		if ( same == 0 ) fout<<"Volunteer cheated!";
		if ( same > 0 )  fout<<same;
		if ( same < 0 )  fout<<"Bad magician!";
		fout<<endl;
	}
	fin.close();
	fout.close();
}
