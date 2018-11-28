#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
#include <iomanip>
using namespace std;

int main() {
	int T;
	scanf("%d", &T);
	for (int count = 1; count <= T; count++) {
		int sum = 0;
		int m = 0, n = 0;
		int i = 0;
		cin >> m >> n;
		int a[100];
		for (i = 0; i < n; i++)
			scanf("%d",&a[i]);
		sort(a, &a[n]);
		for (i = 0; i < n; i++){
			if ( m > a[i])
				m += a[i];
			else if (m == a[i]){
				m += m - 1;
				sum++;
			}
			else if (m < a[i]){
				while ( m < a[i]){
					m = 2 * m - 1;
					sum++;
				}
				m += a[i];
			}
		}
		printf("Case #%d:%d\n", count, sum);
	}
	return 0;
}

