


// rishabhtw07
#include<bits/stdc++.h>

using namespace std;

#define FOR(i,a,b) for(i=a;i<b;++i)
#define FORD(i,a,b) for(i=a;i>=b;--i)
#define ll long long
#define mp make_pair
#define pb push_back
#define MOD 1000000007
#define infi 1000000007
#define s(x) scanf("%d", &x)
#define sl(x) scanf("%lld", &x)
#define sd(x) scnaf("%lf", &x)
#define fi first
#define se second
#define p(x) printf("%d",x)
#define pl(x) printf("%lld", x)
#define pd(x) printf("%lf", x)
#define pn() printf("\n")

string str;
int main()
{
    freopen("inp.txt", "r",stdin);
    freopen("out.txt", "w", stdout);

    int t, i,j , id = 1;
    cin >> t;
    char k;

    while(t--) {
        cin >> str;
        j = 0;
        k = str[0];
        FOR(i, 1, str.size()) {
            if(str[i] != k) {
                j++;
                k = str[i];
            }

        }
        if(k == '-')
            j++;
        printf("Case #%d: %d\n", id++, j);
    }
    return 0;
}
