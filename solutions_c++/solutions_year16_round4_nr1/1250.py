#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int a[5];
int ans[5000];

int N;
bool ok(int l, int r, int x)
{
    int y = (x + 1) % 3 + 1;
    //cerr<<"x="<<x<<"y="<<y<<endl;
    int mid = ((r - l + 1) >> 1) + l;
    if(!ans[l]) ans[l] = x, --a[x];
    if(!ans[mid]) ans[mid] = y, --a[y];

    //cerr<<a[1]<<" "<<a[2]<<" "<<a[3]<<" "<<mid<<" "<<r<<endl;
    for(int i = 1; i <= 3; ++i) if(a[i] < 0) return false;
    if(mid == r) return true;
    return (ok(l, mid - 1, x) && ok(mid, r, y));
}

void work(int l, int r)
{
    if(l == r) return;
    int mid = ((r - l + 1) >> 1) + l;
    work(l, mid - 1);
    work(mid, r);
    char ch1, ch2;
    for(int i = l; i < mid; ++i)
    {
        if(ans[i] == 1) ch1 = 'R';
        else if(ans[i] == 2) ch1 = 'P';
        else ch1 = 'S';
    
        if(ans[mid + i - l] == 1) ch2 = 'R';
        else if(ans[mid + i - l] == 2) ch2 = 'P';
        else ch2 = 'S';
        
        if(ch1 < ch2) return;
        if(ch1 > ch2) break;
    }
    
    for(int i = l; i < mid; ++i) swap(ans[i], ans[mid + i - l]);
}

int main()
{
    int T;
    scanf("%d", &T);
    for(int Case = 1; Case <= T; ++Case)
    {
        scanf("%d%d%d%d", &N, &a[1] ,&a[2], &a[3]);
        
        bool flag = 0;
        for(int i = 1; i <= 3; ++i)
        {
            memset(ans, 0, sizeof(ans));
            int p = a[1], q = a[2], r = a[3];
            if(ok(1, (1 << N), i))
            {
                flag = 1;
                break;
            }
            a[1] = p, a[2] = q, a[3] = r;
        }
        printf("Case #%d: ", Case);
        if(flag)
        {
            work(1, (1 << N));
            for(int i = 1; i <= (1 << N); ++i)
            {
                if(ans[i] == 1) printf("R");
                else if(ans[i] == 2) printf("P");
                else printf("S");
            }
            printf("\n");
        }
        else printf("IMPOSSIBLE\n");
    }
    return 0;
}