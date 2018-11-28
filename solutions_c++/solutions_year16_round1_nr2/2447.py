#include <iostream>
using namespace std;
int n, a[1000][1000];
struct ll {
    int b[1000];
};
ll l[1000];
int mark[2][1000], tmp1[2][1000];

bool cmp (ll l1, ll l2) {
    int i= 1;
    for (i=1; i<=n; i++) {
        if (l1.b[i] != l2.b[i])
            break;
    }
    return l1.b[i] < l2.b[i];
}

void printl (int now) {
    cout << "now: " << now << endl;
    for (int i=1; i<=n; i++) {
        for (int j=1; j<=n; j++)
            cout << a[i][j] << " ";
        cout << endl;
    }
    cout << endl;
}



bool search (int now) {
    //printl(now);

    if (now == 2*n) return true;
    if (now == 1) {
        mark[1][1] = 1;
        for (int i=1; i<=n; i++)
            a[1][i] = l[now].b[i];
        if (search (now + 1))
            return true;
        return false;
    }
    int f = 1;
    int tmp[51][51];
    for (int i=1; i<=n; i++)
        for (int j=1; j<=n; j++)
            tmp[i][j] = a[i][j];
    for (int i=1; i<=n; i++)
        if (a[1][i] == l[now].b[1] && mark[0][i] == 0 && f == 1) {
            mark[0][i] = 1;
            for (int j=1; j<=n; j++) {
                if (a[j][i] == -1)
                    a[j][i] = l[now].b[j];
                else if (a[j][i] == l[now].b[j])
                    continue;
                
                else {
                    f = 0;
                    break;
                }
            }
            if ( f == 1 && search (now+1))
                return true;
            else {
                f = 0;
                for (int i=1; i<=n; i++)
                    for (int j=1; j<=n; j++)
                        a[i][j] = tmp[i][j];
                mark[0][i] = 0;
                //printl (-now);
            }
        }

    f = 1;
    for (int i=1; i<=n; i++)
        if (mark[1][i] == 0) {
            f = 1;
            mark[1][i] = 1;
            for (int j=1; j<=n; j++) {
                if (a[i][j] == -1)
                    a[i][j] = l[now].b[j];
                else if (a[i][j] == l[now].b[j]) {
                    continue;
                }
                else {
                    f = 0;
                    break;
                }
            }
            if (f == 1 && search (now+1))
                return true;
            else {
                for (int i=1; i<=n; i++)
                    for (int j=1; j<=n; j++)
                        a[i][j] = tmp[i][j];
                mark[1][i] = 0;
            }
        }

    return false;
}
void solve () {
    cin >> n;
    int tmp;
    for (int i=1; i<=2*n-1; i++)
        for (int j=1; j<=n; j++) {
            cin >> tmp;
            l[i].b[j] = tmp;
        }
    sort (l+1, l + 2*n, cmp);
    for (int i=1; i<=n; i++)
        for (int j=1; j<=n; j++)
            a[i][j] = -1;
    memset (mark, 0, sizeof(mark));
    //cout << n << endl;

    
    search(1);

    for (int i=1; i<=n; i++) {
        if (mark[0][i] == 0) {
            for (int j=1; j<=n; j++)
                cout << a[j][i] << " ";
        }
        
    }
    for (int i=1; i<=n; i++) {
        if (mark[1][i] == 0) {
            for (int j=1; j<=n; j++)
                cout << a[i][j] << " ";
        }
      
    }
    cout << endl;

}

int main () {
    int t;
    cin >> t;
    for (int i=1; i<=t; i++) {
        cout << "Case #" << i << ": ";
        solve ();
    }
}