#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<functional>
#include<algorithm>
#include<utility>
#define PB push_back
#define MP make_pair
#define _F first
#define _S second

using namespace std;

int main(int argc, char* argv[]){
    int T;
	scanf("%d", &T);
	for(int i = 1; i <= T; i++){
		printf("Case #%d:", i);
		long long int K, C, S;
		scanf("%lld%lld%lld", &K, &C, &S);
		long long int tar = 1;
		for(int j = 1; j < C; j++)
			tar *= K;
		for(int j = 0; j < K; j++)
			printf(" %lld", 1+tar*j);
		puts("");
	}	
    return 0;
}
