#include <bits/stdc++.h>
using namespace std;
#define forn(i,n) for(int i=0 ;i < (int)(n); i++)
#define forni(i,n) for(int i=1 ;i <= (int)(n); i++)
#define dforn(i, n) for( tint i=(int) (n)-1 ;i >= 0; i--)
typedef long long tint;
const int MAXN=500100, inf=1e9;

int n, ans, k, sz;
char s[1005];
bool sepudrio;

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("Output_Problem_1.txt", "w", stdout);
    int t;
    cin >> t;
    forn(cs, t){
    //while(cin >> n){
        cin >> s >> k;
        printf("Case #%d: ", cs+1);
        sz = strlen(s);
        ans = 0;
        sepudrio = false;
        forn(i, sz){
            if(s[i] == '+')continue;
            if(i+k > sz){sepudrio=true; break;}
            ans++;
            forn(j, k){
                switch(s[i+j]){
                    case '+': s[i+j]='-'; break;
                    case '-': s[i+j]='+'; break;
                }
            }
        }
        if(sepudrio)printf("IMPOSSIBLE\n");
        else printf("%d\n", ans);
    }
    return 0;
}

