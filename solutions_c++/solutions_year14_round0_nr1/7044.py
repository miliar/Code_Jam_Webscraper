/*
 GCJ 2014 Qual A 
 Saurav Shekhar
 */
#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <set>
#include <map>
#include <bitset>

using namespace std;
#define EPS 1e-6
#define INF 2000000000
#define P 1000000009
typedef unsigned int ui;
typedef unsigned long long llu; //I64d
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<vi> vvi;

const ui LIM = 17; 

int main()
{
  ui T;
  ui a[5][5], b[5][5];
  ui pos1[LIM] , pos2[LIM], r1, r2;
  scanf("%u",&T);

  for(ui qq=1; qq<=T; qq++) {
  	ui count = 0;
	ui y;
	cin >> r1;
	for(ui i=1; i<=4; i++)
		for(ui j=0; j<4; j++)
			cin >> a[i][j];
	cin >> r2;

	for(ui i=1; i<=4; i++)
		for(ui j=0; j<4; j++)
			cin >> b[i][j];

	for(ui j=0; j<4; j++)
		for(ui k=0; k<4; k++)
			if(a[r1][j] == b[r2][k]) {
				count++;
				y = a[r1][j];
			}
		
	


	cout << "Case #" << qq << ": ";
	if(count == 1) cout << y << "\n";
	else if(count == 0) cout << "Volunteer cheated!\n";
	else cout << "Bad magician!\n";
  }

  return 0;
}




















