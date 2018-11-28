#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
#include <queue>
using namespace std;
int NUM[20];
int Check(long long n)
{
    int i,j,k,cnt;
    for (cnt=0;n;n/=10,cnt++)
        NUM[cnt]=n%10;
    for (i=0;i<cnt/2;i++)
        if (NUM[i]!=NUM[cnt-i-1])
            return 0;
    return 1;
}

long long aa[1000];
int main()
{
    int i,j,h,tt,tab,cal=0, cnt=1;
    long long a,b;
    freopen("C-large-1.in","r",stdin);
    //freopen("A-large.out","w",stdout);
    freopen("1.txt","w",stdout);
    aa[0] = 0;
    for (a=1LL;a<=10000000;a++){
        if (b=a*a,Check(a) && Check(b))
            aa[cnt++] = b;
    }
    sort(aa,aa+cnt);
    scanf("%d",&tt);
    while(tt--){
        cin >> a >> b;
        printf("Case #%d: %d\n",++cal,upper_bound(aa,aa+cnt,b)-upper_bound(aa,aa+cnt,a-1));
    }
    return 0;
}
