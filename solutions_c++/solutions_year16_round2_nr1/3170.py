#include<stdio.h>
#include<string.h>
char str[2050];
int main()
{
    freopen("F:\\asad\\Codejam\\ina.txt","r",stdin);
    freopen("F:\\asad\\Codejam\\oa2.txt","w",stdout);
    int t,i,l, a[30],b[20],x,j;
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        for(j=0;j<26;j++)
        {
            a[j]=0;
        }
        scanf("%s",str);
        l=strlen(str);
        for(j=0;j<l;j++)
        {
            a[str[j]-'A']++;
        }
        b[0]=a[25];
        a['O'-'A']-=a[25];
        b[2]=a['W'-'A'];
        a['T'-'A']-=a['W'-'A'];
        a['O'-'A']-=a['W'-'A'];
        b[4]=a['U'-'A'];
        a['F'-'A']-=a['U'-'A'];
        a['O'-'A']-=a['U'-'A'];
        b[5]=a['F'-'A'];
        a['I'-'A']-=a['F'-'A'];
        a['V'-'A']-=a['F'-'A'];
        b[6]=a['X'-'A'];
        a['I'-'A']-=a['X'-'A'];
        b[8]=a['G'-'A'];
        a['I'-'A']-=a['G'-'A'];
        a['T'-'A']-=a['G'-'A'];
        b[7]=a['V'-'A'];
        b[9]=a['I'-'A'];
        b[1]=a['O'-'A'];
        b[3]=a['T'-'A'];
        printf("Case #%d: ",i);
        for(j=0;j<10;j++)
        {

            while(b[j]--)
            {
                printf("%d",j);
            }

        }
         printf("\n");
    }
}
