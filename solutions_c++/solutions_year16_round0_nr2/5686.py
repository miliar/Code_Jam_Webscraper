#include <stdio.h>
#include <iostream>
#include <string.h>

using namespace std;

int main(){

    freopen( "input.in", "r", stdin );
	freopen( "output.out", "w", stdout );

	int t,z;
	scanf("%d",&t);
	for(z=1;z<=t;z++){
        char s[101];
        scanf("%s",s);
        int l = strlen(s);
        int i;
        int c=0;
        for(i=0;i<l-1;i++){
            if(s[i]!=s[i+1])
                c++;
        	}
        if(s[l-1] == '-')
            c++;
       printf("Case #%d: %d\n",z,c);
    }
    return 0;
}
