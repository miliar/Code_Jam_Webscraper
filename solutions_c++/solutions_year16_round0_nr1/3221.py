#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    long long n;
    bool digit[15];
    int ans=0;
    int tt;
    scanf("%d",&tt);
    for (int turn=1; turn<=tt; turn++)
    {
        scanf("%lld",&n)==1;
        if (n==0)
        {
            printf("Case #%d: INSOMNIA\n",++ans);
            continue;
        }
        for (int i=0; i<=9; i++)
            digit[i]=false;
        long long t=n;
        int cou=0;
        while (cou<10)
        {
            long long tmp=t;
            while (tmp>0)
            {
                if (!digit[tmp%10])
                {
                    digit[tmp%10]=true;
                    cou++;
                }
                tmp=tmp/10;
            }
            if (cou==10) break;
            if (cou<10) t=t+n;
        }
        cout<<"Case #"<<++ans<<": "<<t<<endl;
    }
    return 0;
}
