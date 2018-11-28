#include <cstdio>
#include <vector>
#include <algorithm>

#define pb push_back

using namespace std;

vector <long long> data;

bool ispalin(long long x)
{
     int l, i;
     char chr[32];
     bool valid=1;
     l=sprintf(chr, "%lld", x);
     for (i=0;i<l>>1;i++)
         valid&=(chr[i]==chr[l-i-1]);
     return valid;
}

void move(long long pow10[8], int num, int dig, int off)
{
     int i;
     for (i=(off) ? (0) : (1);i<10;i++)
         if (off<(dig-1)>>1)
            move(pow10,num+(i*pow10[dig-off-1])+(i*pow10[off]),dig,off+1);
         else
         {
            long long n, m;
            n=(dig&1) ? (num+(i*pow10[off])) : (num+(i*pow10[off])+(i*pow10[off+1]));
            if (ispalin((m=n*n)))
               data.pb(m);
         }
}

int main(void)
{
    int t, i, tc=0;
    long long a, b, pow10[8];
    pow10[0]=1;
    for (i=1;i<8;i++)
        pow10[i]=(pow10[i-1]<<3)+(pow10[i-1]<<1);
    for (i=1;i<8;i++)
        move(pow10,0,i,0);
    for (scanf("%d", &t);t--;)
    {
        scanf("%lld%lld", &a, &b);
        printf("Case #%d: %d\n", ++tc, upper_bound(data.begin(),data.end(),b)-lower_bound(data.begin(),data.end(),a));
    }
    return 0;
}
