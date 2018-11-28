#include <iostream>
#include <math.h>
#include <string.h>
#include <string>
#include <cmath>
#include <stdio.h>
#include <vector>
#include <map>
#include <list>
#include <queue>
#include <functional>
#include <algorithm>
#include <bitset>
#include <set>
#include <stack>
#include <limits>
#include <sstream>
#include <ctime> 
#define endl '\n'
#pragma warning (disable : 4996)

using namespace std;

#define lli long long int
#define ull unsigned long long int
#define MP make_pair

const int N = (int)(5e2 + 20);
const int L = 20;
const lli M = 1000000007;
const double E = 1e-7;

char field[N][N];
int rowSmalest[N], rowBigger[N], colSmalest[N], colBigger[N];

int main()
{
	ios_base::sync_with_stdio(0);
#ifdef FILE_IO
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif 
	int T;
	cin >> T;
	for (int qq = 0; qq < T; ++qq) {
		cout << "Case #" << (qq + 1) << ": ";
		
		int r, c;
		cin >> r >> c;
		for (int i = 0; i < N; ++i) {
			rowSmalest[i] = colSmalest[i] = N;
			rowBigger[i] = colBigger[i] = -1;
		}
		for (int i = 0; i < r; ++i) {
			for (int j = 0; j < c; ++j) {
				cin >> field[i][j];
				if (field[i][j] != '.') {
					rowSmalest[i] = min(rowSmalest[i], j);
					rowBigger[i] = max(rowBigger[i], j);
					colSmalest[j] = min(colSmalest[j], i);
					colBigger[j] = max(colBigger[j], i);
				}
			}
		}

		bool canChange = true;
		int changeCount = 0;

		for (int i = 0; i < r; ++i) {
			for (int j = 0; j < c; ++j) {
				if (field[i][j] != '.') {
					bool needChange = false;
					switch (field[i][j])
					{
					case '^': 
						needChange = colSmalest[j] == i;
						canChange &= (colBigger[j] > i) || rowSmalest[i] < j || rowBigger[i] > j /*|| colSmalest[j] < i*/ || !needChange;
						break;
					case 'v':
						needChange = colBigger[j] == i;
						canChange &= /*(colBigger[j] > i) || */ rowSmalest[i] < j || rowBigger[i] > j || colSmalest[j] < i || !needChange;
						break;
					case '>':
						needChange = rowBigger[i] == j;
						canChange &= (colBigger[j] > i) || rowSmalest[i] < j || /*rowBigger[i] > j ||*/ colSmalest[j] < i || !needChange;
						break;
					case '<':
						needChange = rowSmalest[i] == j;
						canChange &= (colBigger[j] > i) /*|| rowSmalest[i] < j*/ || rowBigger[i] > j || colSmalest[j] < i || !needChange;
						break;
					default:
						break;
					}
					if (needChange) changeCount++;
				}
			}
		}

		if (!canChange) cout << "IMPOSSIBLE"; else cout << changeCount;

		cout << endl;
	}
}
