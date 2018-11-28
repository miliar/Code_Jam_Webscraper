#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;
int a[20];
int b[20];
int t ;
int haha[16][16];
int heihei[16][16];
int main()
{
    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    scanf("%d",&t);
    int cas = 0 ;
    while(cas!=t)
    {
        cas++;
        int na , nb;
        scanf("%d",&na);
        for(int i = 0 ; i < 4 ; i ++ )
        {
            if(i+1==na)
            {
                for(int j = 0 ; j < 4 ; j++ )
                    scanf("%d",&a[j]);
            }
            else
            {
                for(int j = 0 ; j < 4 ; j++ )
                {

                int tt;
                scanf("%d",&tt);
                //cout<<tt;
                }
            }
        }
        scanf("%d",&nb);
        for(int i = 0 ; i < 4 ; i ++ )
        {
            if(i+1==nb)
            {
                for(int j = 0 ; j < 4 ; j++ )
                    scanf("%d",&b[j]);
            }
            else
            {
                for(int j = 0 ; j < 4 ; j++ )
                {

                int tt;
                scanf("%d",&tt);
                //cout<<tt;
                }
            }
        }
        int ansnum=0;
        int ans=-1;
        int flag=0;
        for(int i = 0 ; i < 4 ; i ++)
        {
            for(int j = 0 ; j < 4 ; j ++ )
            {
                if(a[i]==b[j])
                {
                    if(ansnum==0)
                    {
                        ansnum++;
                        ans=a[i];
                    }
                    else
                    {
                        flag=1;
                    }
                }
            }
        }
        if(ans==-1)
            flag=2;
        if(flag==0)
        {
            printf("Case #%d: %d\n",cas,ans);
        }
        else if(flag==1)
        {
            printf("Case #%d: Bad magician!\n",cas);
        }
        else if(flag==2)
        {
            printf("Case #%d: Volunteer cheated!\n",cas);
        }
    }
    return 0;
}
