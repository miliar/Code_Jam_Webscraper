#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>
#include <limits.h>
#include <math.h>
#include <algorithm>
#include <bitset>
#include <vector>
using namespace std;
typedef long long ll;

int main(){
	freopen("D-large.in","r",stdin);
	freopen("dlarge.txt","w",stdout);
	int T,Case=1,k,c,s;
	for(scanf("%d",&T);Case<=T;Case++){
		scanf("%d%d%d",&k,&c,&s);
		printf("Case #%d: ",Case);
		if(c*s<k){
			puts("IMPOSSIBLE");
			continue;
		}
		int p=0;
		vector<ll> q;
		for(;p<k;){
			ll ans=0;
			for(int i=0;i<c;i++){
				ans=ans*k+(p++);
				if(p>=k)break;
			}
			q.push_back(ans);
		}
		for(int i=0;i<q.size();i++){
			printf(i==0?"%I64d":" %I64d",q[i]+1);
		}
		puts("");
	}
    return 0;
}

