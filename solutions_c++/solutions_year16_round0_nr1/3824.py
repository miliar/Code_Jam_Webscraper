#include <bits/stdc++.h>

using namespace std;

void check(int n, map<int,bool> &mp, int &c)
{
    while(n)
    {
        int r = n%10;
        if(!mp[r])
            c++;
        mp[r] = 1;
        n /= 10;
    }
}

int main()
{
    int T;

    freopen("in.in","r",stdin);
    freopen("out.txt","w",stdout);

    scanf("%d",&T);
    for(int t=1;t<=T;t++)
    {
        map<int,bool> mp;
        int n,c = 0;
        scanf("%d",&n);

        printf("Case #%d: ",t);

        if(n==0)
            printf("INSOMNIA\n");
        else
        {
            int m=0;
            while(c<10)
            {
                m += n;
                check(m,mp,c);
            }

            printf("%d\n",m);
        }
    }

    return 0;
}
