#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>

using namespace std;

int ctr = 1;

int MaxRow(  int arr[][130], int r, int m ) {
	int max = arr[r][0];
	for ( int i = 0; i < m; i++ ) {
		if ( max < arr[r][i] ) {
			max = arr[r][i];
		}
	}

	return max;
}

int MaxCol(  int arr[][130], int c, int n ) {
	int max = arr[0][c];
	for ( int i = 0; i < n; i++ ) {
		if ( max < arr[i][c] ) {
			max = arr[i][c];
		}
	}

	return max;
}

bool isPossible( int arr[][130], int n, int m ) {
	int rowMax[n];
	int colMax[m];

	for ( int i = 0; i < n; i++ ) {
		rowMax[i] = MaxRow(arr, i, m);
	}
	
	for ( int i = 0; i < m; i++ ) {
		colMax[i] = MaxCol(arr, i, n);
	}
	
	for ( int i = 0; i < n; i++ ) {
		for ( int j = 0; j < m; j++ ) {
			if ( !( arr[i][j] == rowMax[i] || arr[i][j] == colMax[j] ) ) {
				return false;
			}
		}
	}

	return true;
}


int main() 
{
	int t;
	cin >> t;

	for ( int i = 0; i < t; i++ ) {
		int n;
		int m;
		
		cin >> n;
		cin >> m;
		
		int arr[n][130];

		for ( int i = 0; i < n; i++ ) {
			for ( int j = 0; j < m; j++ ) {
				cin >> arr[i][j];
			}
		}
		
		if ( isPossible(arr, n, m) ) {
			cout << "Case #" << ctr << ": YES" << endl;
		} else {
			cout << "Case #" << ctr << ": NO" << endl;
		}

		ctr++;
	}
	
	return 0;
}
