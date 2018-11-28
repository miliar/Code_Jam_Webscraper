#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;
#define maxn 10000000
__int64 a[maxn + 1];
int str[20];
bool check(__int64 tmp)
{
    int tt = 0;
    while(tmp != 0)
    {
        str[tt++] = tmp % 10;
        tmp /= 10;
    }
    int kt = 0;
    int flag =0;
    while(kt < tt - kt - 1)
    {
        if(str[kt] != str[tt - kt - 1])
        {
            return false;
        }
        kt++;
    }
    return true;
}
int main()
{
    int T;
    int tp = 0;
    for(__int64 i = 0; i <= maxn; i++)
    {
        if(check(i) && check(i*i))
            a[tp++] = i * i;
    }
    // cout << tp << endl;
    //for(int i = 0; i < tp ; i++)
    //    cout << a[i] << endl;
     freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);

    while(scanf("%d",&T)!=EOF)
    {
        int csT = 1;
        while(T--)
        {
            __int64 A,B;
            scanf("%I64d%I64d",&A,&B);
            int st,ed,mid;
            st = 0;
            ed = tp - 1;
            int k1,k2;
            k1 = k2 = 0;
            while(st <= ed)
            {
                mid = (st + ed) >> 1;
                if(a[mid] < A)
                {
                    k1 = max(k1,mid);
                    st = mid + 1;
                }
                else
                {
                    ed = mid - 1;
                }
            }
            st =0;
            ed= tp - 1;
            while(st <= ed)
            {
                mid = (st + ed) >> 1;
                if(a[mid] <= B)
                {
                    k2 = max(k2,mid);
                    st = mid + 1;
                }
                else
                {
                    ed = mid - 1;
                }
            }
            printf("Case #%d: %d\n",csT++,k2 - k1);
        }
    }
    return 0;
}
