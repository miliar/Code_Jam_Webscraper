
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
    int tc, t  = 1, a[1010];
    scan(tc);
    while(tc--){
        int n;
        scan(n);

        for(int i = 0; i < n; i++){
            scan(a[i]);
        }

        int sum = 0, mx = 0;
        for(int i = 0; i < n - 1; i++){
            if(a[i] > a[i+1]) sum += (a[i] - a[i+1]);
            mx = max(mx, a[i] - a[i+1]);
        }

        int s = 0;
        for(int i = 0; i < n - 1; i++){
            int d = a[i] - a[i+1];
            if(a[i] < mx) s += a[i];
            else s += mx;
        }

        printf("Case #%d: %d %d\n", t++, sum, s);
    }
    return 0;
}
