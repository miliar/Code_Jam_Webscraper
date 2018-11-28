#include <vector>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
using namespace std;

int is_par(int a)
{
    char str[20];
    sprintf(str, "%d", a);
    int i,len = ceil(log10(a));
    //printf("%d:len = %d\n", a, len);
    for(i=0;i<len/2;++i)
        if(str[i]!=str[len-1-i]) return 0;
    return 1;
}

int initialize()
{
    int i, tmp;
    for(i=1;i<=1000000000;++i)
    {
        tmp = sqrt(i);
        if(i!= tmp*tmp) continue;
        if(!is_par(i)) continue;
        printf("%d\n", i);
    }
}

int count_par(int a, int b)
{
    int i, tmp, cnt=0;
    for(i=a;i<=b;++i)
    {
        tmp = sqrt(i);
        if(i!= tmp*tmp) continue;
        if(!is_par(i)) continue;
        //printf("%d %d\n", i, tmp);
        if(is_par(tmp))
            ++cnt;
    }
    return cnt;
}

int main()
{
    int T, A, B;
    int i;
    scanf("%d", &T);
    for(i=1;i<=T;++i)
    {
        scanf("%d%d", &A, &B);
        printf("Case #%d: %d\n", i, count_par(A, B));
    }
    return 0;
}
