#include<bits/stdc++.h>
using namespace std;

int main()
{
    //Place the Input File in the same directory as that of the cpp file.
    //Write the code normally as you take input from keyboard using scanf..
    //Just Place freopen() as the first statement in main();
    freopen("A-large.in","r",stdin);
    freopen("Output.txt","w",stdout);
    int t,i,j;
    long long int n,n1,n2;
    scanf("%d",&t);
    for(i=1;i<=t;++i)
    {
        int c[11]={0},flag,it=2;
        scanf("%lld",&n);
        n1=n;
        while(true)
        {
            n2=n1;
            flag=1;
            while(n1)
            {
                ++c[n1%10];
                n1/=10;
            }
            if(n==0){
                printf("Case #%d: INSOMNIA\n",i);
                break;
            }
            for(j=0;j<10;++j)
            {
                if(c[j]<1)
                {
                    flag=0;
                    break;
                }
            }
            if(flag==0)
            {
                n1=n*(it++);
            }
            else
            {
                printf("Case #%d: %lld\n",i,n2);
                break;
            }
        }
    }
    return 0;
}
