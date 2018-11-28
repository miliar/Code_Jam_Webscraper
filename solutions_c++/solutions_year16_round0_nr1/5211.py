#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <string>
#include <cstring>
#include <iomanip>
#include <set>
#include <map>
#include <queue>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair <int, int> pii;
#define x first
#define y second
#define mp make_pair
#define pb push_back
const int N = (int)1e5 + 5, INF = (int)1e9;
const ld EPS = 1e-9;
int a[15];
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("b.txt", "w", stdout);
	int t, n;
	cin >> t;
	for(int z = 1; z <= t; z++){
		cout << "Case #" << z << ": ";
		cin >> n;
		if(n == 0){
			cout << "INSOMNIA\n";
			continue;
		}
		int x, k = 10;
		for(int i = 0; i < 10; i++)
			a[i] = 0;
		for(int i = 1; ; i++){
			x = n * i;
			int y = x;
			while(y){
				a[y % 10]++;
				if(a[y % 10] == 1)
					k--;
				y /= 10;
			}
			if(!k){
				cout << x << "\n";
				break;
			}
		}
	}
	return 0;
}