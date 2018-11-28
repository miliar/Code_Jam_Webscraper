#include<bits/stdc++.h>
using namespace std;
int let[30];
int dig[15];
char str[200005];
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t,i,j,k,x;
    scanf("%d",&t);
    for(x=1;x<=t;x++)
    {
        scanf("%s",str);
        for(i=0;i<=26;i++)
            let[i]=0;
        for(i=0;i<=9;i++)
            dig[i]=0;
        int n=strlen(str);
        for(i=0;i<n;i++)
        {
            let[(int)(str[i]-'A')]++;
        }
        dig[0]=let[25];
        dig[2]=let[22];
        dig[4]=let[20];
        let[5]=let[5]-dig[4];
        dig[5]=let[5];
        dig[6]=let[23];
        let[21]=let[21]-dig[5];
        dig[7]=let[21];
        dig[8]=let[6];
        let[(int)('O'-'A')]-=dig[0]+dig[2]+dig[4];
        dig[1]=let[(int)('O'-'A')];
        let[(int)('I'-'A')]-=dig[5]+dig[6]+dig[8];
        dig[9]=let[(int)('I'-'A')];
        let[(int)('H'-'A')]-=dig[8];
        dig[3]=let[(int)('H'-'A')];
        printf("Case #%d: ",x);
        for(i=0;i<=9;i++)
        {
            while(dig[i]--)
                printf("%d",i);
        }
        printf("\n");
    }
}
