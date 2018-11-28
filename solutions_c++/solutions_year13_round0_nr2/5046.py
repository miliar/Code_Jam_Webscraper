#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;

int T,N,M;
int a[100][100];
int row_max[100],col_max[100];


void gcj(const int& count)
{
	//  initial
	int i ,j,max;
	for( i = 0;i < N; ++i)
	{
		for( max = a[i][0],j = 0; j < M; ++j )
			if( a[i][j] > max )
				max = a[i][j];
		row_max[i] = max;
	}

	for( i = 0; i < M; ++i )
	{
		for( max = a[0][i],j = 0; j < N; ++j )
			if( a[j][i] > max  )
				max = a[j][i];
		col_max[i] = max;
	}

	/*

	for( i = 0; i < N; ++i)
		cout << row_max[i] << ',';
	cout << endl;
	for( i = 0; i < M; ++i )
		cout << col_max[i] <<  ',';
	cout << endl;
	*/

	for( i = 0; i < N; ++i )
		for( j = 0; j < M; ++j )
			if( a[i][j] < row_max[i] && a[i][j] < col_max[j] )
			{
				cout << "Case #" << count << ": NO" << endl;
				return;
			}
	cout << "Case #" << count << ": YES" << endl;

}
int main()
{

	freopen("B-large.in","r",stdin);
	//freopen("B-small-attempt0.in","r",stdin);

	//freopen("B-small.out","w",stdout);
	freopen("B-large.out","w",stdout);
	cin >> T;

	for( int count =
	 1; count <= T; ++count )
	{
		cin >> N >> M;
		for( int i = 0; i < N; ++i )
			for( int j = 0; j < M; ++j )
				cin >> a[i][j];
		gcj(count);
	}
	return 0;
}
