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
    char s[110];
    scanf("%d",&cases);
    for(test=1; test<=cases; test++) {
        scanf(" %s", s);
        int l = strlen(s);
        int flips = 0;
        char prev = s[0];
        for(int i = 0; i < l; i++) {
            if (s[i] != prev) {
                flips++;
                prev = s[i];
            }
        }
        if (s[l-1] == '-') flips++;
        printf("Case #%d: %d\n", test, flips);
    }
    return 0;
}
