#include<iostream>
#include<stdio.h>
#include<string>
#include<string.h>
using namespace std;
int main()
{
    int n,k,b,t;
//freopen("B-small-attempt0.in","r",stdin);
//freopen("out.txt","w",stdout);

    scanf("%d",&t);


    for(int cs=1; cs<=t; cs++)
    {
        int ans=0;
        scanf("%d %d %d",&n,&b,&k);
        for(int i=0; i<n; i++)
            for(int j=0; j<b; j++)
            {
                unsigned int temp=i&j;
//                printf("%d %d %d\n",temp,i,j);
                if(temp<k)
                {

                    ans++;
                }
            }
        printf("Case #%d: %d\n",cs,ans);
    }

}

