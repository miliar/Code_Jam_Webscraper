#include <iostream>
#include <cstdio>
#include <vector>
#define MAX 19
#define LIM 8000000
using namespace std;

int main(){
	int n, casos, j, k, s;
	cin >> casos;
	for(int i = 1; i <= casos; i++){
		cin >> n >> k >> s;
		printf("Case #%d:", i);
		for(int j = 1; j<= n; j++)
            printf(" %d", j);
        printf("\n");
	}
	return 0;
}
