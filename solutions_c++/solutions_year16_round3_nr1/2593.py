#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
    freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
    int n,i,j,k,t;
    scanf("%d",&t);
    for(i=0;i<t;i++)
    {
        scanf("%d",&n);
        int pos[n],num=0;
        for(j=0;j<n;j++)
        {
            scanf("%d",&pos[j]);
            num+= pos[j];
        }
        printf("Case #%d:",i+1);
        int high,highpos,k=0;
        bool odd = false;
        if(num%2!=0)
        {
            odd = true;
        }
        while(num)
        {
            high = 0;
            highpos = 0;
            for(j=0;j<n;j++)
            {
                if(high<pos[j])
                {
                    high = pos[j];
                    highpos = j;
                }
            }
            if(k%2==0)
            {
                printf(" ");
            }
            else if(odd&&num==2)
            {
                printf(" ");
                k--;
            }
            printf("%c",highpos+65);
            k++;
            pos[highpos]--;
            num--;
        }
        printf("\n");
    }
}
