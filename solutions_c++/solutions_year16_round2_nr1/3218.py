#include<stdio.h>
#include<string.h>
int main()
{

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int t,i,j,k;
    scanf("%d",&t);
    for(i=0;i<t;i++)
    {
        char s[2005];
        scanf("%s",s);
        int l,p[26];
        for(j=0;j<26;j++)
            p[j]=0;
        l=strlen(s);
        for(j=0;j<l;j++)
        {
            if(s[j]=='Z')
              p[25]++;
        if(s[j]=='G')
            p[6]++;
        if(s[j]=='X')
            p[23]++;
        if(s[j]=='W')
            p[22]++;
        if(s[j]=='I')
            p[8]++;
        if(s[j]=='H')
            p[7]++;
        if(s[j]=='U')
            p[20]++;
        if(s[j]=='F')
            p[5]++;
        if(s[j]=='S')
            p[18]++;
        if(s[j]=='O')
            p[14]++;

        }
        int r[10];
        r[9]=p[8]-p[23]-p[6]-p[5]+p[20];
        r[8]=p[6];
        r[7]=p[18]-p[23];
        r[6]=p[23];
        r[5]=p[5]-p[20];
        r[4]=p[20];
        r[3]=p[7]-p[6];
        r[2]=p[22];
        r[1]=p[14]-p[25]-p[20]-p[22];
        r[0]=p[25];

        printf("Case #%d: ",i+1);
        for(k=0;k<10;k++)
        {
            for(j=0;j<r[k];j++)
                printf("%d",k);
        }

        printf("\n");
    }

     return 0;
}
