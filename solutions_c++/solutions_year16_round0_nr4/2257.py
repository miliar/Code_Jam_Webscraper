#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<string>
#include<set>
#include<map>
#include<vector>
using namespace std;
typedef long long LL;
int T, K, C, S;
int main(){
	freopen("D_in.txt", "r", stdin);
	freopen("D_out.txt", "w", stdout);
	scanf("%d", &T);
	for(int c = 1; c<=T; ++c){
		scanf("%d%d%d", &K, &C, &S);
		printf("Case #%d:", c);
		for(int i = 1; i<=S; ++i)
			printf(" %d", i);
		printf("\n");
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
