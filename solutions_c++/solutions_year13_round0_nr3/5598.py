#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
using namespace std;

typedef long long int64;

bool isPalindromes(int number) {
	char data[22];
	sprintf(data, "%d", number);
	int len = strlen(data);
	char* start = data;
	char* end = data + len - 1;
	while(start < end) {
		if(*start != *end)
			return false;
		start++;
		end--;
	}
	return true;
}

int main() {
	int numOfCasese;
	cin>>numOfCasese;
	freopen("out.txt", "w", stdout);
	for(int p = 1; p <= numOfCasese; p++) {
		int low, high;
		scanf("%d%d", &low, &high);
		printf("Case #%d: ", p);
		int count = 0;
		for(int i = low; i <= high; i++) {
			if(!isPalindromes(i)) {
				continue;
			}
			int sRoot = sqrt((double)i);
			if(sRoot * sRoot != i) {
				continue;
			} else if(isPalindromes(sRoot)) {
				count++;
			}
		}
		printf("%d\n", count);
	}
}