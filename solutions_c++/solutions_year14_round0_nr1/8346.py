#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int main()
{
    freopen("A-small-attempt0.in" , "r" , stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    int T;
    int x;
    int common[17];
    int common_count;
    int num,comVal;
    scanf("%d",&T);

    int t=1;
    while(t<=T)
    {
        scanf("%d",&x);
        for(int i=0;i<17;i++){common[i]=-1;}
        for(int i=1;i<=4;i++)
        {
            for(int j=0;j<4;j++)
            {
                scanf("%d",&num);
                if(i==x){common[num]=0;}
            }
        }

        common_count=0;
        num=comVal=0;

        scanf("%d",&x);
        for(int i=1;i<=4;i++)
        {
            for(int j=0;j<4;j++)
            {
                scanf("%d",&num);
                if(i==x)
                {
                    if(common[num]==0)
                    {
                        common_count++;
                        comVal=num;
                    }
                }
            }
        }

        printf("Case #%d: ",t);
        if(common_count==0)
        {
            printf("Volunteer cheated!\n");
        }
        else if(common_count==1)
        {
            printf("%d\n",comVal);
        }
        else if(common_count>1)
        {
            printf("Bad magician!\n");
        }

        t++;
    }
    return 0;
}
