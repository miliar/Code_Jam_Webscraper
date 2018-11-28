#include<bits/stdc++.h>

#define MOD 1000000007
#define EPS 1e-7
#define N 100010
#define PB push_back
#define MP make_pair
#define sa(x) scanf("%d", &x)

using namespace std;

typedef pair<int,int> pii;
typedef long long int ll;
int p[1010];

int process(int m)
{
    for(int i = m; i > 0; i--) {
        if(p[i] == 0) continue;
        int min = i;
        for (int j=1; j <= i/2; j++) {
            p[j] += p[i];
            p[i-j] += p[i];
            int t = process(i-1);
            //printf("%d-%d %d\n", j, i-j, t);
            if((p[i] + t) < min) min = p[i] + t;
            p[j] -= p[i];
            p[i-j] -= p[i];
        }
        return min;
    }
    return 0;
}

int main()
{
    int i,j,n,t,k,m,x,y,test,cases;
    scanf("%d",&cases);
    for(test=1; test<=cases; test++) {
        memset(p, 0, sizeof(p));
        scanf("%d", &n);
        for (i = 0; i < n; i++) {
            scanf("%d", &x);
            p[x]++;
        }
        printf("Case #%d: %d\n", test, process(10));
    }
    return 0;
}
