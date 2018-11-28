#include<bits/stdc++.h>
using namespace std;
int main()
{
    int tc;
    scanf("%d",&tc);
    for(int z=1;z<=tc;++z)
    {
        int n;
        int a[10];
        memset(a,0,sizeof a);
        scanf("%d",&n);
        if(n==0)
        {
            printf("Case #%d: INSOMNIA\n",z);
            continue;
        }
        int i=1,x;
        while(1)
        {
            x=n;
            x*=i;
            i++;
            while(x>0)
            {
                a[x%10]=1;
                x/=10;
            }
            int s=0;
            for(int j=0;j<10;++j)
            s+=a[j];
            if(s==10)
            break;
        }
        //cout<<i<<"\n";
        printf("Case #%d: %d\n",z,n*(i-1));
    }
    return 0;
}
