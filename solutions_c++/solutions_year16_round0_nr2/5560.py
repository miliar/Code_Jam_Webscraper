#include <stdio.h>
#include <iostream>
#include <string.h>

using namespace std;

int main(){

    freopen( "input.in", "r", stdin );
	freopen( "output.out", "w", stdout );

	int t,p;
	scanf("%d",&t);
	for(p=1;p<=t;p++){
        char a[101];
        scanf("%s",a);
        int len = strlen(a);
        int i;
        int c=0;
        for(i=0;i<len-1;i++){
            if(a[i]!=a[i+1])
                c++;
        	}
        if(a[len-1] == '-')
            c++;
       printf("Case #%d: %d\n",p,c);
    }
    return 0;
}
