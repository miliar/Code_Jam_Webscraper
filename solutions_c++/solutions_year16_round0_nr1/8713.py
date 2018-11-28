#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <stack>
#include <queue>
#include <cstring>
using namespace std;

typedef long long lld;

#define SIZE 100

#define IN freopen("A-large.in","r",stdin);
#define OUT freopen("A-large.out","w",stdout);

int T;

int main()
{
	IN
	OUT
	int i,t, N;

	cin >> T;

	for(t=1;t<=T;t++){
		printf("Case #%d: ",t);
		
		scanf("%d", &N);

		if(N == 0) {
			printf("INSOMNIA\n");
			continue;
		}

		int count = 0;
		bool mark[10];
		memset(mark, 0, sizeof(mark));

		int NN, i = 1;
		while(true) {
			NN = N * i;

			while(NN) {
				if(mark[ NN % 10 ] == false) {
					count++;
					mark[ NN % 10 ] = true;
				}
				NN /= 10;
			}

			if(count == 10) {
				printf("%d\n", N * i);
				break;
			}

			i++;
		}
	}
	return 0;
}
