#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <list>
using namespace std;

int file[10005];
bool vis[10005];

int solution(int n, int disk) {
	int ans = 0;
	for (int i = n - 1; i >= 0; i--) {
		if (vis[i]) {
			continue;
		}
		for (int j = i - 1; j >= 0; j--) {
			if (!vis[j] && file[i] + file[j] <= disk) {
				ans++;
				vis[i] = true; vis[j] = true;
				break;
			}
		}
		if (!vis[i]) {
			vis[i] = true;
			ans++;
		}
	}
	return ans;
}

int main(int argc, const char *argv[]){

	int times;
	cin >> times;
	int n, disk;

	for (int ti = 1; ti <= times; ti++) {
		scanf("%d %d", &n, &disk);
		for (int i = 0; i < n; i++) {
			vis[i] = false;
			scanf("%d", &file[i]);
		}
		sort(file, file + n);
		printf("Case #%d: %d\n", ti, solution(n, disk));
	}
	
	return 0;
}
