#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <queue>
#include <algorithm>
#include <cmath>
#include <string>
#include <map>
#include <cmath>
#include <set>
using namespace std;

int main()
{

    int t,j=1;
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&t);
    while(t--)
    {
        set<int> S;
        long long  n;
        scanf("%lld",&n);
        printf("Case #%d: ",j++);
        if(n==0) printf("INSOMNIA\n");
        else
        {
            long long b,cnt=1,ww,ans;
            bool flog=0;
LI:
            b=n*cnt;
            ww=b;
            while(b)
            {
                int kkk=b%10;
               // printf("%d*\n",kkk);
                S.insert(kkk);
                int l=S.size();
                if(l==10)
                {
                    flog=1;
                    ans=cnt;
                    break;
                }
                b=b/10;
            }
            cnt++;
            if(flog==0) goto  LI;
            printf("%lld\n",ww);
        }
    }
}
