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

int ans[1000100];

int main(int argc, char* argv[]){
	int in;
	int sc = 1;
	FILE *fp;
	fp = fopen("out", "r");
	for(int i = 1; i <= 1000000; i++)
		fscanf(fp, "%d", &ans[i]);	
	fclose(fp);
	int T;
	scanf("%d", &T);
	for(int i = 1; i <= T; i++){
		printf("Case #%d: ", i);
		int tar;
		scanf("%d", &tar);
		if(tar == 0)
			puts("INSOMNIA");
		else
			printf("%d\n", ans[tar]);	
	}	
    return 0;
}
