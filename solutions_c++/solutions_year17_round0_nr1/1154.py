#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef double dd;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef vector<ii> vii;

#define FOR(i,a,b) for (int (i) = (a); (i) < (b); (i)++)
#define DOW(i,b,a) for (int i = (b); i >= (a); i--)
#define pb(a) push_back(a)
#define ALL(a) (a).begin(),(a).end()
#define fi first
#define se second

template<typename T>
void print_array(T* arr, int num) {
   FOR(i, 0, num) cout << arr[i] << ' ';
   cout << endl;
}

template<typename T> 
void print_vector(vector<T> vec) {
   FOR(i,0,vec.size()) cout << vec[i] << ' ';
   cout << endl;
}

int t,n;
string s;
int main() {
    ios_base::sync_with_stdio(false); cin.tie(0);
    //freopen("test.txt", "r", stdin);
    cin >> t;
    FOR(k,1,t+1) {
        cin >> s >> n;
        int ans = 0;
        FOR(i,0,s.length() - n + 1) {
            if (s[i] == '-') {
                ans++;
                FOR(j,i,i + n) {
                    if (s[j] == '-') s[j] = '+';
                    else s[j] = '-';
                }
            }
        }
        FOR(i,s.length() - n + 1, s.length()) {
            if (s[i] != '+') {
                ans = -1;
                break;
            }
        }
        printf("Case #%d: ", k);
        if (ans == -1) printf("IMPOSSIBLE\n");
        else printf("%d\n", ans);
    }
}