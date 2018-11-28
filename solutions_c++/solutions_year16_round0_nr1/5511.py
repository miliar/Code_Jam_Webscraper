#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <vector>
#include <string.h>
#include <queue>
#include <map>
#include <set>

using namespace std;

#define MAXN 1000005
#define INF 2000000000
int C;
int visited[10];
int N, M;

bool check() 
{
	for(int i=0; i<10; i++) if(visited[i] == 0) return false;
	return true;
}

void mark(int num)
{
	while(num > 0) {
		int nxt = num%10;
		visited[nxt] = 1;
		num -= nxt;
		num = num/10;
	}
	return;
}
		
int main(void)
{
	cin >> C;
	for(int c=1; c<=C; c++) {
		memset(visited, 0, sizeof(visited));
		cin >> N;
		long long tmp = N;
		if(N == 0) {
			printf("Case #%d: INSOMNIA\n", c);
			continue;
		}
		long long cnt = 1;
		while(!check()) {
			mark(tmp);
			tmp = N*cnt;
			cnt++;
		}
		printf("Case #%d: %lld\n", c, tmp-N);
	}
	
	return 0;
}
