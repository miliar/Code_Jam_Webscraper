#include<cstdio>
#include<cmath>
#include<string>

using namespace std;

const int MAXN = 107;
int tab[MAXN];

bool palindrom(long long a)
{
    string tmp;
    long long ta = a;
    while(ta)
    {
        tmp += ta%10;
        ta /= 10;
    }
    int dl = tmp.size();
    int i = 0;
    while(i<=dl/2)
    {
        if(tmp[i]!=tmp[dl-i-1])
            return 0;
        i++;
    }
    return 1;
}

int main()
{
    int n;
    long long a, b;
    for(int i=1; i<=MAXN; i++)
        if(palindrom(i) && palindrom((long long)(i*i)))
            tab[i] = 1;
    for(int i=2; i<=MAXN; i++)
        tab[i] += tab[i-1];
    scanf("%d", &n);
    for(int i=1; i<=n; i++)
    {
        scanf("%lld%lld", &a, &b);
        int pa = sqrt(a), pb = sqrt(b);
        if((long long)(pa*pa)==a)           
            pa--;
        int wyn = tab[pb]-tab[pa];
        printf("Case #%d: %d\n", i, wyn);
    }
    return 0;
}
