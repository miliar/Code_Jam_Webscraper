


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

bool has[15];

bool check()
{
    int i;
    FOR(i, 0, 10) {
        if(!has[i])
            return 0;
    }
    return 1;
}

ll fnc(int x)
{
    memset(has, 0, sizeof(has));
    ll num;
    ll base = x;
    ll id = 1;
    ll ret;
    int tmp;
    while(1) {
        num = base * id;
        ret = num;
        id++;
        //cout << " "<<num<<endl;
        while(num) {
            tmp = num % 10;
            has[tmp] = 1;
            num /= 10;
        }
        if(check())
            return ret;
    }
}

int main()
{

    freopen("inp.txt", "r",stdin);
    freopen("out.txt", "w", stdout);
    int i, j, k;

    int t;
    ll n;
    int id = 1;
    ll ans;

    cin >> t;
    while(t--) {
        cin >> n;
        if(n != 0)
            printf("Case #%d: %lld\n", id++, fnc(n));
        else
            printf("Case #%d: INSOMNIA\n", id++);
    }
    return 0;

}
