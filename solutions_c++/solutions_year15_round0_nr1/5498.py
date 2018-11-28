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
    char s[1010];
    scanf("%d",&cases);
    for(test=1; test<=cases; test++) {
        scanf("%d %s", &k, s);
        int len = strlen(s);
        int sum = 0;
        int required = 0;
        for (i = 0; i < len; i++) {
            if (sum < i && s[i] != '0') {
                required += i - sum;
                sum += i - sum;
            }
            sum += s[i] - '0';
        }
        printf("Case #%d: %d\n", test, required);
    }
    return 0;
}
