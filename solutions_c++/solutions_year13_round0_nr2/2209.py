#include <iostream>
#include <vector>
#include <cassert>
#include <queue>

using namespace std;

#define ll long long

const int MN = 100 + 10;

int arr[MN][MN];


int n, m;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int k = 1; k <= t; k ++) {
		
		cin >> n >> m;
		for(int i = 0; i < n; i ++) {
			for(int j = 0; j < m; j ++)
				cin >> arr[i][j];
		}
		bool ok = true;
		for(int str = 0; str < n; str ++) {
			for(int stb = 0; stb < m; stb ++) {
				bool ok1 = true, ok2 = true;
				for(int i = 0; i < n; i ++) {
					if (arr[i][stb] > arr[str][stb])
						ok1 = false;
				}
				for(int i = 0; i < m; i ++) {
					if (arr[str][i] > arr[str][stb])
						ok2 = false;
				}
				ok &= (ok1 | ok2);
			}
		}
		printf("Case #%d: ", k);
		cout << (ok ? "YES\n" : "NO\n");
	}

	return 0;
}