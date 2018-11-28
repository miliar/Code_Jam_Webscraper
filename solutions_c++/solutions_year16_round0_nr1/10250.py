#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <cmath>
const long long mod=1e9+7;
#define maxn 20000005
#include <vector>
#include<set>;
typedef long long LL;
using namespace std;
long long dir[30];

int main() {
    //freopen("d:\\in.txt", "r", stdin);
    //freopen("d:\\inn.txt", "w", stdout);
    long long cnt=1;
    for(int i=1;i<=30;i++)
    {
        dir[i]=cnt;
        cnt*=10;
    }
    int T;
    scanf("%d",&T);
    for(int i=1;i<=T;i++)
    {
        long long a,b;
        bool f[10];
        memset(f,false,sizeof(f));
        scanf("%lld",&a);
        if(a==0)
            printf("Case #%d: INSOMNIA\n",i);
        else
        {
            for(int k=1;;k++)
            {
                long long aa;
                aa=a*k;
                //printf("%d  %lld\n",i,aa);
                int t=30;
                while(aa/dir[t]==0)
                    t--;
                while(t)
                {
                    int b=aa/dir[t];
                    aa=aa-b*dir[t];
                    f[b]=true;
                    t--;
                }
                bool flag=true;
                for(int l=0;l<=9;l++)
                {
                    if(f[l]==false)
                        flag=false;
                }
                if(flag==true)
                {
                    printf("Case #%d: %lld\n",i,a*k);
                    break;
                }
            }
        }
    }
    return 0;
}