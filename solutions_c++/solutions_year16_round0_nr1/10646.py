#include <iostream>
#include<stdio.h>
#include <set>

using namespace std;

int main()
{
    //freopen("A-large.in","r",stdin);
    //freopen("out","w",stdout);
    int t,j;
    long  n;
    long long result;
    scanf("%d",&t);
    for(j=1;j<=t;j++)
    {
        scanf("%ld",&n);
        if(n==0)
        {
            printf("case #%d: INSOMNIA\n",j);
            continue;
        }
        long long c=0,m;
        std::set<int> myset;
        while(1){
            c++;
            m=c*n;

            while(m>0)
            {
                myset.insert(m%10);
                m=m/10;
                if(myset.size()==10)
            {
                result=c*n;
                break;
            }
            }
            if(myset.size()==10)
            {
                result=c*n;
                break;
            }
        }
        printf("case #%d: %lld\n",j,result);

    }
    return 0;
}
