#include <cstdio>
#include <algorithm>
#include <bitset>
#include <iostream>

using namespace std;

const int BIT = 16;
const int J = 50;

const int MAXN = 10000000;
bool iscom[MAXN];
int prime[MAXN];
int primecnt;

void build(void)
{
    primecnt = 0;
    for(int i=0;i<MAXN;++i) iscom[i] = false;
    for(int i=2;i<MAXN;++i) {
        if(!iscom[i]) {
            prime[primecnt++] = i;
            for(int j=i*2;j<MAXN;j+=i)
                iscom[j] = true;
        }
    }
    primecnt = min(100000,primecnt);
}

bool check(int x)
{
    for(int base=2;base<=10;++base) {
        bool found = false;
        for(int i=0;i<primecnt;++i) {
            int p = prime[i];
            if(p==x) return false;
            int rem = 0;
            for(int bit=15;bit>=0;--bit) {
                rem = (rem*base)%p;
                if(x&(1<<bit)) rem = (rem+1)%p;
            }
            if(rem==0) {
                found = true;
                break;
            }
        }
        if(!found) return false;
    }
    return true;
}

void print(int x)
{
    // printf("%d",x);
    cout << bitset<BIT> (x);
    for(int base=2;base<=10;++base) {
        for(int i=0;i<primecnt;++i) {
            int p = prime[i];
            int rem = 0;
            for(int bit=BIT-1;bit>=0;--bit) {
                rem = (rem*base)%p;
                if(x&(1<<bit)) rem = (rem+1)%p;
            }
            if(rem==0) {
                printf(" %d",p);
                break;
            }
        }
    }
    puts("");
}

int main(void)
{
    build();
    puts("Case #1:");
    int cnt = 0;
    int now = (1<<(BIT-2));
    while(cnt<J) {
        int tmp = ((now<<1) | 1);
        if(check(tmp)) {
            ++cnt;
            print(tmp);
        }
        ++now;
    }
    return 0;
}
