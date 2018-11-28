#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>
#include <queue>
using namespace std;

int T, nt=0, num[10];
long long N, t, x;

bool sleep()
{
	for(int i=0; i<10; ++i)
		if(!num[i]) return false;
	return true;
}

int main(int argc, char const *argv[])
{
	scanf("%d", &T);
	while(T--){
		scanf("%ld", &N);
		if(!N){
			printf("Case #%d: INSOMNIA\n", ++nt);
			continue;
		}
		x = 1;
		memset(num, 0, sizeof(num));
		while(!sleep()){
			t = N * x;
			while(t){
				++num[t%10];
				t /= 10;
			}
			++x;
		}
		printf("Case #%d: %-ld\n", ++nt, N*(x-1));
	}
	return 0;
}