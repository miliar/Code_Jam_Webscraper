/*
*/
#include <cstdio>
#include <iostream>
using namespace std;

int arr[100][100];
bool flag[100][100];

typedef struct Point {
	int x;
	int y;
} Point;

Point MaxHeight(int n, int m)
{
	int max = 0;
	Point p;
	p.x = -1;
	p.y = -1;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			if ( ( flag[i][j] == false) && (arr[i][j] > max) ) {
				max = arr[i][j];
				p.x = i;
				p.y = j;
			}
	return p;
}

void Judge(int n, int m)
{
	Point p = MaxHeight(n, m);
	if ( p.x == -1) {
		cout << "YES" << endl;
		return ;
	}
	
	int row = p.x;
	int col = p.y;	
	int height =  arr[p.x][p.y];
	
	
	bool mow = true;   //row
	for (int i = 0; i < m; i++) {
		if ( (flag[row][i] == true) && (arr[row][i] > height) )
			mow = false;
	}
	if (mow == true)
  		for (int i = 0;  i < m; i++) {
			if (arr[row][i] == height)
				flag[row][i] = true;
		}

	mow = true;			//col
	for (int i = 0; i < n; i++) {
		if ( (flag[i][col] == true) && (arr[i][col] > height) )
			mow = false;
	}
	if (mow == true)
  		for (int i = 0; i < n; i++) {
			if (arr[i][col] == height)
			flag[i][col] = true;
		}
	
	/*cout << height << " is at " << row << " " << col << endl;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cout << flag[i][j] << " ";
		}
		cout << endl;
	}*/
	if (flag[row][col] == false) {
		cout << "NO" << endl;
		return ;
	}
	else
		Judge(n, m);
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	//freopen("sample.in", "r", stdin);
	//freopen("sample.out", "w", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		int n, m;
		cin >> n >> m;
		for (int j = 0; j < n; j++)
			for (int k = 0; k < m; k++) {
				int height;
				cin >> height;
				arr[j][k] = height;
				flag[j][k] = false;
			}		
	
		cout << "Case #" << i+1 << ": ";
		Judge(n, m);
	}		

	return 0;
}
