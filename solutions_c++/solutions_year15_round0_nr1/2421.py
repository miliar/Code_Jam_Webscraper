
/*  Towhidul Islam
    University Of Dhaka
    Problem Name :
    Algorithm Used :
*/

#include<bits/stdc++.h>

typedef long long ll;

#define SSTR(x)         dynamic_cast< ostringstream & >( \
                        (ostringstream() << dec << x )).str()
#define pb              push_back
#define mem(a, x)       memset(a, x, sizeof a)
#define PI              acos(-1)
#define all(a)          a.begin(), a.end()
#define MAX             100010
#define read(in)        freopen("in.txt", "r", stdin)
#define write(out)      freopen("out.txt", "w", stdout)
#define INF             10000000
#define eps             1e-9
#define arraysz(a)      sizeof (a)/sizeof(a[0])
#define FORN(i, n)      for(int i = 0; i < n; i++)
#define FORAB(i, x, n)  for(int i = x; i < n; i++)
#define FORD(i, x, n)   for(int i= n - 1; i >= x; i--)
#define scan(n)         scanf("%d", &n)
#define print(n)        printf("%d\n", n)
#define tor             vector
#define dbg(x)          cout<<#x<<" : "<<x<<endl
#define chkwhere        cout<<"LOL\n"
#define pii             pair<int, int>

using namespace std;

int main(){
    read(in);
    write(out);
    int tc, t = 1, smx;
    string s;
    scan(tc);
    while(tc--){
        scan(smx);
        cin>>s;

        int sum = s[0] - '0', req = 0, ans = 0;
        FORAB(i, 1, smx + 1){
            if(sum >= i){
                sum += s[i] - '0';
            }
            else if(s[i] > '0'){
                req = (i - sum);
                ans += req;
                //cout<<"i = "<<i<<" s[i] = "<<s[i]<<" sum = "<<sum<<endl;;
                sum += s[i] - '0' + req;
            }
        }
        printf("Case #%d: %d\n", t++, ans);
    }
    return 0;
}
