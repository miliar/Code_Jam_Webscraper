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

int main()
{
    int i,j,n,t,k,m,x,y,test,cases;
    scanf("%d",&cases);
    for(test=1; test<=cases; test++) {
        scanf("%d", &n);
        bool a[10]={0};
        int found = 0;
        if (n==0) {
            printf("Case #%d: INSOMNIA\n", test);
            continue;
        }
        int cur = n;
        while (1) {
            int tmp = cur;
            while (tmp) {
                if (!a[tmp % 10]) {
                    a[tmp%10] = true;
                    found++;
                }
                tmp /= 10;
            }
            if (found == 10) {
                printf("Case #%d: %d\n", test, cur);
                break;
            }
            cur += n;
        }
    }
    return 0;
}
