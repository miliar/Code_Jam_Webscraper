#include<bits/stdc++.h>
using namespace std;
int check(int has[])
{
    int flag=1;
    for(int i=0;i<10;i++)
    {
        if(has[i]==0)
        {
            flag=0;
            break;
        }
    }
    return flag;
}
void update(int has[],int n)
{
    int k;
    while(n>0)
    {
        k=n%10;
        has[k]++;
        n=n/10;
    }
}
int main()
{
    freopen( "A-large.in", "r", stdin);
    freopen( "codejam1.out", "w", stdout);
    int has[10];
    int testcases;
    cin>>testcases;
    for(int k=1;k<=testcases;k++)
    {
        memset(has,0,sizeof(has));
        int n;
        cin>>n;
        if(n==0)
            printf("Case #%d: INSOMNIA\n",k);

        else
        {
            int i=2,temp=n;
            while(!check(has))
            {
                update(has,temp);
                temp=n*i;
                i++;
            }
            printf("Case #%d: %d\n",k,temp-n);
        }
    }

}
