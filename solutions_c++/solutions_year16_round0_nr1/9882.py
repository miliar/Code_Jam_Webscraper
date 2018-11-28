#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>

#define pairr pair<int, int>
#define s second
#define f first
#define pb push_back

using namespace std;

int n,i,j,a[10],t,t1,r;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>t;
    for (t1=1;t1<=t;t1++)
    {
        cin>>n;
        printf("Case #%d: ",t1);
        if (n==0) printf("INSOMNIA\n");
        else
        {
            r=0;
            for (i=n;r==0;i+=n)
            {
                j=i;
                while (j>0)
                {
                    if (a[j%10]==0) a[j%10]=1;
                    j/=10;
                }
                for (j=0;j<10;j++)
                {
                    if (a[j]==0)
                    {
                        r=0;
                        break;
                    }
                    else r=1;
                }
            }
            i-=n;
            printf("%d\n",i);
            for (i=0;i<10;i++) a[i]=0;
        }
    }
    return 0;
}
