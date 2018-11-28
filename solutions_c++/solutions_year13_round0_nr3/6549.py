#include<cstdio>
#include<cmath>
using namespace std;

int ispalin(long long num)
{
    long long n = num, rev=0, dig;
    while(num>0)
    {
        dig = num-((num/10)*10);
        rev = rev * 10 + dig;
        num = num / 10;
    }
    if (n == rev) return 1;
    else return 0;
}

void getResult(long long s, long long e, int j)
{
    double start = sqrt(double(s));
    long long end = sqrt(double(e));
    int count=0;
    for(long long i=ceil(start); i<=end; i++)
    {
        if(ispalin(i) && ispalin(i*i))   count++;
    }
    printf("Case #%d: %d\n",j,count);
}
int main()
{
    int tcase, j=1;
    long long start, end;
    scanf("%d", &tcase);
    while(tcase--)
    {
        scanf("%lld %lld", &start, &end);
        getResult(start, end, j);
        j++;
    }
}
