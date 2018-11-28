#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
    int t,j;
    int n,i,c=0;
    char a[1005];
    scanf("%d", &t);

    for(j=1; j<=t; j++) {
        int c=0;

        scanf("%d", &n);
        scanf("%s", a);
        int sum=a[0]-48,ans=-1;

        for(i=1; i<=n; i++) {
        	if(a[i]!='0') {
        		c += i-sum;
        		sum+=(a[i]-48);
        		if(ans<c) {
        			ans=c;
        		}
        		c=0;
        	}
        }
        if(ans<0) {
        	ans=0;
        }
        printf("Case #%d: %d\n", j,ans);
    }

    return 0;
}
