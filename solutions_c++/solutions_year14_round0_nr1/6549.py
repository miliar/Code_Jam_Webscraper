#include <cstdio>
#include <iostream>
#include <cstdlib>

using namespace std;

int main()
{
    freopen("inputA.txt","r",stdin);
    freopen("outputA.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for(int po=0;po<T;po++)
    {
        int a1=0;
        scanf("%d",&a1);
        int pans[4];
        int garbage;
        for(int y=1;y<5;y++)
        {
            if(y==a1)
            {
                for(int h=0;h<4;h++) scanf("%d",&pans[h]);
            }
            else
            {
                for(int h=0;h<4;h++) scanf("%d",&garbage);
            }
        }
        int a2=0;
        scanf("%d",&a2);
        int ans=0;
        bool bflag=false;
        bool cflag=false;
        
        for(int y=1;y<5;y++)
        {
            if(y==a2)
            {
                for(int h=0;h<4;h++)
                {
                    scanf("%d",&garbage);
                    for(int i=0;i<4;i++)
                    {
                        if(pans[i]==garbage)
                        {
                            if(ans==0) ans=pans[i];
                            else bflag=true;
                        }
                    }
                }
            }
            else
            {
                for(int h=0;h<4;h++) scanf("%d",&garbage);
            }
        }
        printf("Case #%d: ",po+1);
        if(bflag) printf("Bad magician!\n");
        else if(ans==0) printf("Volunteer cheated!\n");
        else printf("%d\n",ans);
    }
}
