#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

int main()
{
    freopen("A-small-practice.in", "r", stdin);
    freopen("A-small-practice.out", "w", stdout);

    int T;
    char *resultStr[2]={"Bad magician!","Volunteer cheated!"};
    bool hash[17];
    int row,tmp,cnt,val;
    while(scanf("%d",&T)!=EOF)
    {
        for(int k=1;k<=T;k++)
        {
            memset(hash,0,sizeof(hash));
            cnt=0;
            scanf("%d",&row);
            for(int i=1;i<=4;i++)
            {
                for(int j=1;j<=4;j++)
                {
                    scanf("%d",&tmp);
                    if(row==i)
                    {
                        hash[tmp]=true;
                    }
                }
            }
            scanf("%d",&row);
            for(int i=1;i<=4;i++)
            {
                for(int j=1;j<=4;j++)
                {
                    scanf("%d",&tmp);
                    if(row==i)
                    {
                        if(hash[tmp]){cnt++;val=tmp;}
                    }
                }
            }
            if(cnt==1)printf("Case #%d: %d\n",k,val);
            else if(cnt==0)printf("Case #%d: %s\n",k,resultStr[1]);
            else printf("Case #%d: %s\n",k,resultStr[0]);
        }
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
