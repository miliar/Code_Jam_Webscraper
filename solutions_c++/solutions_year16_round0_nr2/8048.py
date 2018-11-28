#include<bits/stdc++.h>
using namespace std;

int t,i,j,k,l,c,start;
char str[101];

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    scanf(" %d",&t);
    for(i=1; i<=t; i++) {
        scanf("%s",str);
        l=strlen(str);
        c=0;
        for(j=l-1; j>=0; j--) {
            if(str[j]=='-') { start=j; c++;
                for(k=start; k>=0; k--) {
                    if(str[k]=='+') str[k]='-';
                    else str[k]='+';
                }
            }
        }
        printf("Case #%d: %d\n",i,c);
    }
    return 0;
}
