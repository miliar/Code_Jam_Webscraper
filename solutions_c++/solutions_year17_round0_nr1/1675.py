#include <bits/stdc++.h>
using namespace std;

#define sz(v)        ((int)v.size())
#define ll           long long
#define all(v)       (v.begin()) , (v.end())
#define rall(v)      (v.rbegin()) , (v.rend())
#define SetTo(v, a)  memset(v,a,sizeof(v))

char str[1005];

int main ()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int tc, k, n, ans;
    scanf("%d\n", &tc);
    for(int test=1;test <= tc ;test++)
    {
        printf("Case #%d:", test);
        scanf("%s %d\n", str, &k);
        n = strlen(str);
        ans = 0;
        for(int i=0;i<=n-k;i++){
            if(str[i] == '-'){
                ans++;
                for(int j=i;j<i+k;j++){
                    if(str[j] == '+')
                        str[j] = '-';
                    else
                        str[j] = '+';
                }
            }
        }

        bool ok = 1;
        for(int i=0;i<n;i++){
            if(str[i] == '-'){
                ok = 0;
                break;
            }
        }

        if(!ok){
            puts(" IMPOSSIBLE");
        }
        else{
            printf(" %d\n", ans);
        }

    }
    return 0;
}
