/*
    Just For You 97116:)
*/

#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
    //freopen("12A-small-attempt0.txt", "w", stdout);
    //freopen("A-large.in", "r", stdin);
    freopen("12A-large.txt", "w", stdout);
    int t,i,j,k,b[10];
    char s[2005];
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        int a[92]={0};
        scanf("%s",s);
        for(j=0;j<strlen(s);j++)
        {
            a[s[j]]++;
        }
        b[2]=a[87];
        b[4]=a[85];
        b[6]=a[88];
        b[8]=a[71];
        b[0]=a[90];
        b[1]=a[79]-(a[90]+a[85]+a[87]);
        b[3]=a[72]-a[71];
        b[7]=a[83]-a[88];
        b[5]=a[86]-b[7];
        b[9]=a[73]-(a[88]+a[71]+b[5]);
        
        
        printf("Case #%d: ",i);
        
        
        for(k=0;k<b[0];k++)
            printf("0");
        for(k=0;k<b[1];k++)
            printf("1");
        for(k=0;k<b[2];k++)
            printf("2");
        for(k=0;k<b[3];k++)
            printf("3");
        for(k=0;k<b[4];k++)
            printf("4");
        for(k=0;k<b[5];k++)
            printf("5");
        for(k=0;k<b[6];k++)
            printf("6");
        for(k=0;k<b[7];k++)
            printf("7");
        for(k=0;k<b[8];k++)
            printf("8");
        for(k=0;k<b[9];k++)
            printf("9");
        
        printf("\n");
    }
	return 0;
}