#include<iostream>
#include<fstream>
#include<cstdio>
#include<vector>
#include<queue>
#include<algorithm>
using namespace std;
int t,n,used[10];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%lld",&t);
    //t=1000000;
    for(int o=1; o<=t; o++)
    {
        scanf("%lld",&n);
        //n=o;
        if(n==0) {printf("Case #%d: INSOMNIA\n",o); continue;}
        int p=10, l=1;

        for(int i=0; i<=9; i++) used[i]=0;
        while(1)
        {
            int k=n*l;
            while(k>0)
            {
                if(used[k%10]==0) {p--; used[k%10]=1;}
                if(p==0) break;
                k/=10;
            }
            if(p==0) break;
            l++;
        }
        printf("Case #%d: %d\n",o,n*l);
    }
    return 0;
}
