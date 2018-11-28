#include <stdio.h>
#include <algorithm>

using namespace std;

long long num[100000]={0};
int N=0;
int rev(int d, int x)
{
    int i, ret=0;
    for (i=0;i<d;++i){
        ret=ret*10 + (x%10);
        x=x/10;
    }
    return ret;
}
bool is_valid(int x)
{
    int t = x*x;
    int d=0;
    while (t>0){
        ++d;
        t=t/10;
    }
    t = x*x;
    int r = rev(d, t);
    return (t==r);
}
void palin_even(int d, int x)
{
    int i;
    int r = rev(d, x);
    for (i=0;i<d;++i) x=x*10;
    x = x + r;
    if (is_valid(x)){
        num[N++] = x*x;
    }
}
void palin_odd(int d, int x)
{
    int i;
    int r = rev(d, x);
    int p=1, t;
    for (i=0;i<d;++i) p=p*10;
    x = x * p * 10;
    for (i=0;i<10;++i){
        t = x + i*p + r;
        if (is_valid(t)){
            num[N++] = t*t;
        }
    }
}
void rec(int d, int n)
{
    palin_even(d, n);
    palin_odd(d, n);
    if (d<3){
        int i;
        for (i=0;i<10;++i){
            rec(d+1, 10*n+i);
        }
    }
}

int Bsearch(long long key)
{
    int l = 0, r = N;
    int m;
    while (l<=r){
        m = (l+r)>>1;
        if (num[m] < key) l = m+1;
        else r = m-1;
        //else if (num[m] > key) r = m-1;
        //else return m;
    }
    //printf("[%lld] %lld [%lld]\n", num[r], key, num[l]);
    return l;
}

int cnt_digit(int x){
    int d=0;
    while (x>0){
        ++d; x=x/10;
    }
    return d;
}
int cnt(int s, int e)
{
    int i, j, d, ret=0;
    for (i=s;i<=e;++i)
    {
        d=cnt_digit(i);
        if (i==rev(d,i)){
            for (j=1;j<=i;++j){
                if (j*j == i){
                    if (rev(cnt_digit(j), j) == j){
                        ++ret;
                        //printf("%d, ", i);
                    }
                }
            }
        }
    }
    return ret;
}
int main(void)
{
    FILE *fin = fopen("input.txt", "r");
    FILE *fout = fopen("output.txt", "w");

    int i;
    for (i=1;i<10;++i){
        if (is_valid(i)) num[N++] = i*i;
        rec(1, i);
    }
    sort(num, num+N);

    int T, t;
    fscanf(fin, "%d", &T);
    for (t=1;t<=T;++t){
        long long s, e;
        fscanf(fin, "%lld %lld", &s, &e);
        int r=Bsearch(e), l=Bsearch(s);
        if (num[r] == e) ++r;
        fprintf(fout, "Case #%d: %d\n", t, r - l);
        //if (cnt((int)s, (int)e) != r-l) printf("AHHHHHH\n");
/*
        printf("[%lld,%lld] => %d\n", s, e, r-l);
        printf("%lld > ", num[l-1]);
        for (i=l;i<r;++i){
            printf("%lld, ", num[i]);
        }
        printf("<%lld", num[r]);
        printf("\n");
*/
    }

    fclose(fin);
    fclose(fout);
}
