//#include <vector>
//#include <stdio.h>
//#include <string.h>
//#include <iostream>
//#include <algorithm>
//
//using namespace std;
//
//long long pre[] = {1,4,9,121,484,10201,
//             12321,14641,40804,44944,
//             1002001,1234321,4008004,
//             100020001,102030201,104060401,
//             121242121,123454321,125686521,
//             400080004LL,404090404LL,100000000000001};
//
//bool huiwen(int x)
//{
//    char tmp[16];
//    sprintf(tmp,"%d",x);
//    int len = strlen(tmp);
//    for(int i=0;i<len/2;i++)
//        if(tmp[i] != tmp[len-1-i])
//            return false;
//    //puts(tmp);
//    return true;
//}
//
//int cnt(long long x)
//{
////    int ans = 0;
////    for(long long i=1;i*i<=x;i++)
////        if(huiwen(i) && huiwen(i*i))
////            printf("%lld,",i*i);
//            //++ans;
//    if(x == 0)
//        return 0;
//    for(int i=0;i<21;i++)
//        if(x < pre[i])
//            return i;
//    return 21;
//
//}
//
//int main()
//{
////    freopen("C1.in","r",stdin);
////    freopen("C1.txt","w",stdout);
//    for(int i=0;i<=21;i++)
//        printf("%lld\n",pre[i]);
//    int T,ncase = 0;
//    //long long t = 100000000000000LL;
//    //printf("%d\n",cnt(t));
//    //printf("%d\n",cnt(10));
//    scanf("%d",&T);
//    while(T--)
//    {
//        long long a,b;
//        scanf("%lld%lld",&a,&b);
//        printf("**%d  %d\n",cnt(a),cnt(b));
//        printf("Case #%d: %d\n",++ncase,cnt(b)-cnt(a-1));
//    }
//    return 0;
//}



#include <stdio.h>

int n,m,a[105][105];

bool has_r(int r,int x)
{
    for(int j=0;j<m;j++)
        if(a[r][j] > x)
            return true;
    return false;
}


bool has_c(int c,int x)
{
    for(int i=0;i<n;i++)
        if(a[i][c] > x)
            return true;
    return false;
}

int main()
{
//    freopen("B1.in","r",stdin);
//    freopen("B1.txt","w",stdout);
    int T,ncase = 0;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d%d",&n,&m);
        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++)
                scanf("%d",&a[i][j]);
        bool ok = true;
        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++)
            {
                if(has_r(i,a[i][j]) && has_c(j,a[i][j]))
                    ok = false;
            }
        printf("Case #%d: %s\n",++ncase,ok?"YES":"NO");
    }
    return 0;
}
