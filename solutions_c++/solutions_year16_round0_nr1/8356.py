#include <bits/stdc++.h>

using namespace std;

#define openfile {freopen("input.txt","r",stdin); freopen("output.txt","w",stdout);}
#define debug 01

int t;
long long n;
int res;

void calc(int x) {
    while (x>0) {
        res|=(1<<(x%10));
        x/=10;
    }
}

void solve() {
    if (n==0) {
        puts("INSOMNIA");
        return;
    }
    res=0;
    int i=1;
    while (res!=1023) {
        calc(n*i);
        i++;
    }
    printf("%d\n", n*(i-1));
}

int main() {
    openfile;
    scanf("%d", &t);
    for (int i=0; i<t; i++) {
        scanf("%d",&n);
        printf("Case #%d: ",i+1);
        solve();
    }
    return 0;
}
