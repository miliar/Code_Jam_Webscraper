#include<stdio.h>
#include<string.h>
#include<vector>
#include<set>

using namespace std;

set<int> found;
char buff[1000];

void insert(int x){
	sprintf(buff,"%d",x);
	int len = strlen(buff);
	for(int i = 0;i < len;++i)
		found.insert(buff[i] - '0');
}

int solve(int n){
	found.clear();
	for(int i = 1;;++i){
		if(i > 1000){
			printf("error %d\n",n);
			while(1);
			break;
		}
		insert(i * n);
		if(found.size() == 10){
			return n * i;
		}
	}
	return -1;
}

int main(){
	int T;
	scanf("%d",&T);
	for(int cas = 1;cas <= T;++cas){
		int n;
		scanf("%d",&n);
		if(n == 0)
			printf("Case #%d: INSOMNIA\n",cas);
		else
			printf("Case #%d: %d\n",cas,solve(n));
	}
	return 0;
}

