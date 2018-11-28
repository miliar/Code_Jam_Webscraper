#include <stdio.h>
#include <string.h>

int main(){

    freopen("input.in", "r", stdin );
    freopen( "output.out", "w", stdout );

    int t,z;
    scanf("%d",&t);
    char s[1001];
    for(z=0;z<t;z++){
        scanf("%s",s);
        int l,i,j;
        l=strlen(s);
        char q[l];
        q[0]=s[0];
        for(i=1;i<l;i++){
            if(s[i]<q[0])
                q[i]=s[i];
            else{
                for(j=i;j>0;j--)
                    q[j]=q[j-1];
                q[0]=s[i];
            }
        }
        printf("Case #%d: ",z+1);
        for(i=0;i<l;i++)
        	printf("%c",q[i]);
        printf("\n");
    }
    return 0;
}
