#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <map>
#include <set>
#include <vector>

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;

#define f first
#define s second
#define next qwertyusdfgh
#define read(x) scanf("%d", &x)
#define write(x) printf("%d ", x)
#define writeln(x) printf("%d\n", x)
#define pb push_back
#define mp make_pair

const int n = 4;

int a[10][10], b[10][10];
int us[20];

//-------------------------------------------------------------------------------------------------

int main() {

	int t;
	cin >> t;
	for (int tt = 0; tt < t; tt++) {
		int x, y;
		cin >> x;
		for (int i = 1; i <= n; i++)	
			for (int j = 1; j <= n; j++)
				cin >> a[i][j];
		cin >> y;
		for (int i = 1; i <= n; i++)	
			for (int j = 1; j <= n; j++)
				cin >> b[i][j];			
	
		for (int i = 1; i <= 16; i++)
			us[i] = 0;
		for (int j = 1; j <= n; j++) {
			us[a[x][j]]++;
			us[b[y][j]]++;
		}
		int k = 0;
		int ls = 0;
		for (int i = 1; i <= 16; i++)
			if (us[i] == 2) {
				k++;
				ls = i;
			}
		printf("Case #%d: ", tt + 1);
		if (k > 1)
			printf("Bad magician!");
		else
			if (k == 0)
				printf("Volunteer cheated!");
			else
				printf("%d", ls);
		cout << endl;			
	}
	
	return 0;
}