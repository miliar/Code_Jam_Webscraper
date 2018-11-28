#include <iostream>
#include <stdio.h>
#include <math.h>
using namespace std;
int T;
bool isPali(int N)
{
    int data[20],ans=0;
    while(N)
    {
        data[ans++]=N%10;
        N=N/10;
    }
    int i=0,j=ans-1;
    while(i<=j)
    {
        if(data[i]!=data[j])return false;
        i++;j--;
    }
    return true;
}
int main()
{
    freopen("A-small-practice.in", "r", stdin);
    freopen("A-small-practice.out", "w", stdout);
    while(scanf("%d",&T)!=EOF)
    {
        for(int k=1;k<=T;k++)
        {
            int A,B,cnt=0;

            scanf("%d%d",&A,&B);
            int start=sqrt(A);
            int end=sqrt(B)+1;
            for(int i=start;i<=end;i++)
            {
                if(i*i<A)continue;
                if(i*i>B)continue;
                if(isPali(i)&&isPali(i*i)){cnt++;}
            }
            printf("Case #%d: %d\n",k,cnt);
        }


    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
