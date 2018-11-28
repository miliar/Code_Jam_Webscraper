#include<bits/stdc++.h>

    using namespace std;
    #define ll long long
    #define MOD 1000000007
    #define infi (int)1e9
    #define FOR(i,a,b) for(i = a; i < b; i++)
    #define FORD(i,a,b) for(i = a; i >= b; i--)
    #define REP(i,a) for(i = 0;i <= a; i++)
    #define REPD(i,a) for(i = a; i >= 0; i--)
    #define s(n)  scanf("%d",&n)
    #define sc(n)  scanf("%c", &n)
    #define sl(n) scanf("%lld", &n)
    #define sf(n) scanf("%f", &n)
    #define ss(n) scanf("%s", n);
    #define all(a) a.begin(), a.end()
    #define fi first
    #define se second
    #define pb push_back
    #define mp make_pair
    #define fill(a, v) memset(a, v, sizeof(a))
    #define PI 3.1415926535897932384626


int n, len;
int main()
{
    freopen("inp.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t, i, cc = 1;
    s(t);
    while(t--) {

      string str;
      s(len);
      cin >> str;
     // cout << str<<endl;
      int ans = 0;
      int peo = 0;
      FOR(i, 0, len + 1) {
            if(peo < i) {
                ans += (i - peo);
                peo += (i - peo);
            }
             peo +=(str[i] - '0');
        //    cout <<"  "<<peo <<endl;
      }
      printf("Case #%d: %d\n", cc++, ans);
      //cout << ans <<endl;
    }
    return 0;
}
