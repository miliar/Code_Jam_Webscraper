#include <iostream>
#include<stdio.h>

using namespace std;
int vis[11];
int ca;
int main()
{
    freopen("3.in","r",stdin);
    freopen("4.out","w",stdout);
    scanf("%d",&ca);
    for(int i=1;i<=ca;i++)
    {

        int n;
        int k=1;
        int count=0;
        scanf("%d",&n);
        if(n==0) printf("Case #%d: INSOMNIA\n",i);
        else{
            while(count!=10)
            {
                int temp=n*k;
                //int weishu=1;
                while(temp!=0)
                {
                    int ii=temp%10;

                   if(vis[ii]==0) {count++;vis[ii]=1;}
                    temp=temp/10;//cout<<ii<<endl;
                    //weishu++;
                }

                //cout<<weishu-1<<endl;
                k++;

            }
           // cout<<k<<endl;
            printf("Case #%d: %d\n",i,n*(k-1));
            for(int v=0;v<=10;v++)
                vis[v]=0;
        }
    }
    return 0;
}
