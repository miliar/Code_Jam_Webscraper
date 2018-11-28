/*
* @Author: amber
* @Date:   2015-04-11 12:52:44
* @Last Modified by:   amber
* @Last Modified time: 2015-04-11 13:13:25
*/

#include <iostream>
#include <cstdio>

using namespace std;

int g_smax = 0;
char g_array[1200];

int run(int smax, char* array) {
	int my = 0;
	int sum_y = 0;
	for(int i = 0; i < smax; i++) {
		sum_y += (array[i] - '0');
		my = max(my, (i+1) - sum_y);
	}
	return my;
}

int main() {
	int T;
	// freopen("Q-A-standing-ovation.in", "r", stdin);

	scanf("%d", &T);
	// cout << T << endl;
	for (int i = 0; i < T; ++i) {
		scanf("%d %s", &g_smax, g_array);
		// cout << g_smax << "#" << array << endl;
		printf("Case #%d: %d\n", i+1, run(g_smax, g_array));
	}

    return 0;
}