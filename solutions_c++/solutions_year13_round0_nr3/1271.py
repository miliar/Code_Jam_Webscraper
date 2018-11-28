#include <stdio.h>
#include <string.h>

#include <algorithm>

using namespace std;

long long tag[2000];


bool check(char str[]){
	int len=strlen(str);
	int i,j;
	i = 0; j = len - 1;
	while(i < j)
	{
		if(str[i] != str[j]) return false;
		i ++;
		j --;
	}
	return true;
}

int main(){
	int n = 0;
	for(int i=1;i<=10000000;i++){
		char num[100];
		sprintf(num,"%d",i);
		if(!check(num))continue;
		long long x=(long long)i*(long long)i;
		sprintf(num,"%lld",x);
		if(check(num)){
			tag[n++]=x;
		}
	}
	int T;
	freopen("C-large-1.in","r",stdin);
	freopen("C-large-1.out","w",stdout);
	scanf("%d",&T);
	long long a,b;
	for(int cas = 1;cas <= T; cas ++){
			scanf("%lld %lld",&a,&b);
			int ans = 0;
			for(int i = 0; i < n; i ++){
				if(tag[i] >= a && tag[i] <= b){
					ans ++;
				}
			}
			printf("Case #%d: %d\n",cas,ans);
		
	}
	return 0;

}