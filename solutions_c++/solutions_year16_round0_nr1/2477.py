#include <bits/stdc++.h>
using namespace std;
#define DB(v) cerr << #v << ' ' << v << endl
#define sz(v) int(v.size())

vector <bool> used;
int counter;

void modify(int x) {
    while(x != 0) {
        int cur = x % 10;
        if(!used[cur]) {
            used[cur] = true;
            counter++;
        }
        x /= 10;
    }
}

const int A = 1e3;
int T;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w", stdout);
    ios::sync_with_stdio(NULL);cin.tie(NULL);
    cin >> T;
    int n;
    bool is;
    for(int t = 1;t <= T; ++t) {
        is = false;
        counter = 0;
        used.assign(10, false);

        cin >> n;
        cout << "Case #" << t << ": ";
        int cur = 0;
        for(int i = 1;i <= A; ++i) {
            cur += n;
            modify(cur);
            if(counter == 10) {
                is = true;
                cout << cur;
                break;
            }
        }
        if(!is) {
            cout << "INSOMNIA";
        }
        cout << '\n';
    }
    return 0;
}
