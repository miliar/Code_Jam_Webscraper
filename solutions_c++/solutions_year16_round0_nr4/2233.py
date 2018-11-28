#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

int main()
{
	freopen("D-small-attempt1.in","r",stdin);
	freopen("a1.out","w",stdout);
	int task;
	scanf("%d", &task);
	for (int cs=1; cs<=task; cs++){
		int a, b, c;
		scanf("%d%d%d", &a, &b, &c);
		printf("Case #%d:", cs);
		if (a == c){
			for (int i=1; i<=a; i++)
				printf(" %d", i);
			printf("\n");
		}else{
			printf(" IMPOSSIBLE\n");
		}
	}
	return 0;
}
