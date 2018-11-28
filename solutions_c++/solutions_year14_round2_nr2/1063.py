#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <algorithm>


#define MAX 110

using namespace std;

int a,b,k;

int solve(){
	int sum=0;
	for(int i=0;i<a;++i)
	for(int j=0;j<b;++j)
	if((i&j)<k)
	++sum;
	return sum;
}
int main(){
	int t,i;
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	scanf("%d",&t);
	for(i=1;i<=t;++i){
		scanf("%d%d%d",&a,&b,&k);
		
		printf("Case #%d: %d\n",i,solve());
	}
	return 0;
}
