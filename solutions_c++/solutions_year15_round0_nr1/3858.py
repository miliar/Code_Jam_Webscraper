#include<algorithm>
#include<cstdio>
#include<sstream>
#include<cstdlib>
#include<cctype>
#include<cmath>
#include<set>
#include<queue>
#include<stack>
#include<list>
#include<iostream>
#include<fstream>
#include<numeric>
#include<string>
#include<vector>
#include<cstring>
using namespace std;
int T;
int main()
{
   freopen("D:/A-large.IN","r",stdin);
   freopen("G:/out.txt","w",stdout);
    while(~scanf("%d",&T))
    {
        int __=0;
        while(T--)
        {
            int n;
            scanf("%d",&n);
            int total=0;
            int invite=0;
            for(int i=0;i<=n;i++)
            {
                int k;
                scanf("%1d",&k);
                if(total<i)
                {
                    invite+=i-total;
                    total=i;
                }
                total+=k;
            }

            printf("Case #%d: %d\n",++__,invite);
        }
    }
    return 0;
}
