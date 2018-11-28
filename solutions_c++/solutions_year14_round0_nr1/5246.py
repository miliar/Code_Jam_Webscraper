#include<cstdio>
#include<cstring>
#include<iostream>
using namespace std;
int main()
{
//    freopen("in.txt","r",stdin);
//    freopen("out.txt","w",stdout);
    int t,a[5][5],b[5][5],cnt,num1,num2,num,mark=0,v[19];
    scanf("%d",&t);
    while(t--)
    {
        memset(v,0,sizeof(v));
        cnt=0;
        mark++;
        scanf("%d",&num1);
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                scanf("%d",&a[i][j]);
        scanf("%d",&num2);
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                scanf("%d",&b[i][j]);
        for(int i=0;i<4;i++)
            v[a[num1-1][i]]=1;
        for(int i=0;i<4;i++)
        {
            if(v[b[num2-1][i]]==1)
            {
                cnt++;
                num=b[num2-1][i];
            }
        }
        if(cnt==1)
            printf("Case #%d: %d\n",mark,num);
        else if(cnt>1)
            printf("Case #%d: Bad magician!\n",mark);
        else if(cnt==0)
            printf("Case #%d: Volunteer cheated!\n",mark);
    }
    return 0;
}
