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
	freopen("A-large.in","r",stdin);
	freopen("alarge.txt","w",stdout);
	int T,Case=1;
	for(scanf("%d",&T);Case<=T;Case++){
		int r, c, w;
	    scanf("%d%d%d",&r,&c,&w);
	    printf("Case #%d: ",Case);
	    int ans=(int)ceil(c*1.0/w)+(w-1);
	    ans+=(r-1)*(c/w);
	    printf("%d\n",ans);
	}
    return 0;
}

