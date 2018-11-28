#include <cstdio>
#include <cstring>
#include <cmath>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <list>
#include <utility>
#include <string>
#include <algorithm>
#include <iostream>
#define infinity 2139062143
#define infinity64 9187201950435737471LL
#define foreach( i, n ) 	for(int (i) = 0; (i) < (n); ++(i))
#define abs( x ) (((x) < 0)? (-x) : (x) )
#define full 1010
using namespace std;

int naomi[full], ken[full];

int convertToInt(char * input) {
	int len = strlen(input);
	while (len < 7) {
		input[len++] = '0';
	}
	input[len] = '\0';
	int i = 7, mul = 1, res = 0;
	while (input[i] != '.') {
		res += (input[i] - '0') * mul;
		i--;
		mul *= 10;
	}
	return res + 48;
}

int main () {
	int n, t, war, dwar, j;
	char read[20];
	scanf("%d", &t); 
	foreach (it, t) {
		scanf("%d", &n); 
		foreach (i, n) {
			scanf("%s", read); 
			naomi[i] = convertToInt(read);
		}
		foreach (i, n) {
			scanf("%s", read); 
			ken[i] = convertToInt(read);
		}
		sort(naomi, naomi+n);
		sort(ken, ken+n);
		j = war = dwar = 0;
		foreach (i, n) {
			while (j < n && ken[j] < naomi[i]) {
				j++;
			}
			if (j < n) {
				j++;
				war++;
			}
		}
		j = 0;
		foreach (i, n) {
			while (j < n && naomi[j] < ken[i]) {
				j++;
			}
			if (j < n) {
				j++;
				dwar++;
			}
		}
		printf("Case #%d: %d %d\n", it+1, dwar, n-war);
	}
	return 0;
}


