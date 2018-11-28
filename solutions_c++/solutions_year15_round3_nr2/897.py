#include <bits/stdc++.h>
using namespace std;

#define fto(i,a,b) for (int i = (a), _b = (b); i <= _b; i++)
#define fdw(i,a,b) for (int i = (a), _b = (b); i >= _b; i--)
#define fill(ar, val) memset(ar, val, sizeof(ar))
#define out(x,y) cout << x << y
#define out3(x,y,z) cout << x << y << z
#define debug(a) cout << #a << " = " << a << endl
#define ooLL 1000000000000LL
#define oo 1000000000
#define maxn 20
#define eps 0.000000001

#define sz(a) int((a).size())
#define all(c) (c).begin(), (c).end()
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define mp(x,y) make_pair(x, y)

long long sum = 0, local, sl = 0, numtest, maxnum, k ,l ,s;
string target, board, tmp;
char a[maxn];
bool found;

int vet(int i) {
    fto(j,0,k-1) {
        a[i] = board[j];
      //  debug(i);  debug(j);
      //  fto(u,0,s-1) cout << a[i];
        //    cout << endl;
        if (i==s-1) {
            local = 0;

        //    fto(u,0,s-1) cout << a[u];
        //    cout << endl;

            fto(u,0,s-l) {
                found = true;
                fto(v,0,l-1) {
                   // debug(a[u]);
                  //  debug(target[v]);
                    if (a[u+v]!=target[v]) {
                        found = false;
                        break;
                    }
                }
                if (found==true) {
                    sum += 1;
                    local += 1;
                }
            }
         //   debug(local);
            if (local>maxnum) maxnum = local;
            sl++;
        }
        else vet(i+1);
    }
}

int main() {
    #ifndef ONLINE_JUDGE
    freopen("B-small-attempt0.in","r",stdin);
    freopen("ou.out","w",stdout);
    #endif

    cin >> numtest;
    fto(test, 1, numtest) {
        cin >> k >> l >> s;   getchar();
        getline(cin, board);
        getline(cin, target);

        maxnum =0;
        sum = 0;
        sl = 0;
        vet(0);
      //  debug(maxnum);
       // debug(sl);

        printf("Case #%d: %.6llf\n", test, (double)maxnum - (double)sum/sl);
    }

}
