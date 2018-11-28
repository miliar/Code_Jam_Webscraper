
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
    int t = 1, tc, R, C, n;
    scan(tc);
    while(tc--){
        scan(n);
        scanf("%d%d", &R, &C);
        if(R < C) swap(R, C);
        bool f = true;
        if(R * C % n != 0){
            f = true;
        }
        else if(n == 1){
            f = false;
        }
        else if(n == 2){
            f = false;
        }
        else if(n == 3){
            if(R > 2 & C > 1) f = false;
        }
        else if(n == 4){
            if(C >= 3) f = false;
        }

        printf("Case #%d: ", t++);
        if(f == false){
            printf("GABRIEL\n");
        }
        else printf("RICHARD\n");
    }
    return 0;
}
