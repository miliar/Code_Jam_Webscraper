#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>
#include <limits.h>
#include <math.h>
#include <algorithm>
using namespace std;

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("clarge.txt","w",stdout);
	int T,Case=1;
	for(scanf("%d",&T);Case<=T;Case++){
		long long c,d,v;
		scanf("%I64d%I64d%I64d",&c,&d,&v);
		long long tmp;
		long long mark=0;
		int ans=0;
		for(int i=0;i<d;i++){
			scanf("%I64d",&tmp);
			while(tmp>mark+1){
				mark+=(mark+1)*c;
				ans++;
			}
			mark+=tmp*c;
		}
		while(mark<v){
			mark+=(mark+1)*c;
			ans++;
		}
		printf("Case #%d: %d\n",Case,ans);
	}
    return 0;
}

