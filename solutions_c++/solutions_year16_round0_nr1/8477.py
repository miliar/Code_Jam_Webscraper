#include <iostream>
#include<bits/stdc++.h>
using namespace std;
int main()
{
    int i,j,te;
    long n;
    long long no,ol;
    long m;
    int k=0,fl=1;
    int ct;
    bool vis[10];
    //freopen("inp.txt","r",stdin);
    //freopen("op.txt","w",stdout);
    scanf("%d",&te);
    while(--te>=0)
    {
        k++;
        ct=0;
        m=1;
        fl=1;
        scanf("%ld",&n);
        for(i=0;i<10;i++)
            vis[i]=false;
        no=n;
        if(n==0)
            printf("Case #%d: INSOMNIA\n",k);
        else
        {
            while(fl==1)
            {
                no=n*m;
                ol=no;
                m++;
                while(no>0)
                {
                    int dig=no%10;
                    if(vis[dig]==false)
                    {
                        vis[dig]=true;
                        ct++;
                    }
                    no=no/10;
                }
                if(ct==10)
                    fl=0;
            }
            printf("Case #%d: %lld\n",k,ol);
        }
    }
    return 0;
}
