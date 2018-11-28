#include<iostream>
#include<cstdio>
#include<cstring>

using namespace std;

int main()
{
    int t,i,fri,sMax;
    char str1[1010];
    //freopen("A-large.in","r",stdin);
    //freopen("A-large.out","w",stdout);
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        scanf("%d %s",&sMax,str1);
        //cout<<sMax<<"   "<<str1<<endl;
        fri=0;
        int total=str1[0]-48;
        int diff;
        for(int k=1;k<=sMax;k++)
        {
            if(total>=k)
                total=total+(str1[k]-48);
            else if((str1[k]-48)!=0)
            {
                diff=k-total;
                total=total+diff+(str1[k]-48);
                fri=fri+diff;
            }
        }
        printf("Case #%d: %d\n",i,fri);
    }
    return 0;
}
