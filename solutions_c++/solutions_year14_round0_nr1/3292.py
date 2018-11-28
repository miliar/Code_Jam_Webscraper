#include<iostream>
#include<cstdlib>
#include<cstdio>
using namespace std;
int first[4];
int main()
{
    int T;
    int C=0;
    freopen("A-small-attempt1.in","r",stdin);
    freopen("A-small-attempt1.out","w",stdout);
    scanf("%d",&T);
    while(T--)
    {
        int i,j,k,ans,t,Ans,p=0;
        scanf("%d",&ans);
        for(i=1;i<=4;i++)
        {
            for(j=0;j<4;j++)
            {
                scanf("%d",&t);
                if(i==ans)first[j]=t;
            }
        }
        scanf("%d",&ans);
        for(i=1;i<=4;i++)
        {
            for(j=0;j<4;j++)
            {
                scanf("%d",&t);
                if(i==ans){
                for(k=0;k<4;k++)
                    if(first[k]==t)
                    {
                        Ans=t;
                        p++;
                        //cout<<"---"<<Ans<<"---";
                    }
                }
            }
        }
        printf("Case #%d: ",++C);
        switch(p)
        {
            case 0:puts("Volunteer cheated!");break;
            case 1:printf("%d\n",Ans);break;
            default:puts("Bad magician!");
        }
    }
}
