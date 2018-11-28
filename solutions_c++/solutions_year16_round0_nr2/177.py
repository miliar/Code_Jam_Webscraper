#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>
#include <limits.h>
#include <math.h>
#include <algorithm>
#include <bitset>
using namespace std;
typedef long long ll;

char str[105];

int main(){
	freopen("B-large.in","r",stdin);
	freopen("blarge.txt","w",stdout);
	int T,Case=1;
	for(scanf("%d",&T);Case<=T;Case++){
		scanf("%s",str);
		int len=strlen(str);
		int ans=(str[0]=='-'?1:0);
		for(int i=1;i<len;i++){
			if(str[i]!=str[i-1]){
				if(str[i]=='-')ans+=2;
			}
		}
		
		printf("Case #%d: %d\n",Case,ans);
		
	}
    return 0;
}

