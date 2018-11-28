#include<bits/stdc++.h>
#define rep(i, a, b) for(int i = (int)a; i < (int)b; i++)
#define red(i, a, b) for(int i = (int)a; i > (int)b; i--)
#define RED true
#define BLACK false
#define pb push_back
#define mk make_pair
#define fi first
#define se second
using namespace std;
typedef pair<int, int> ii;
typedef long long ll;
typedef pair<ii, int> iii;
typedef pair< pair<double, double>, double>  ddd;
typedef vector<int> vi;
const int N = 100 + 7;
const int M = N * 3;
const int inf = 1e9 + 7;
const int base = 1e9 + 9;
const double pi = acos(-1);
const double ep = 1e-15;

int n, v0, temp0;
int V[N], X[N];
int test;

int main(){
    freopen("B-small-attempt0 (1).in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int query;
    cin >> query;
    rep(tt, 1 , query + 1){
        int u, v;
        scanf("%d %d.%d %d.%d", &n, &v0, &v, &temp0, &u);
        v0 = v0 * 10000 + v;
        temp0 = temp0 * 10000 + u;
        rep(i, 0, n){
            scanf("%d.%d %d.%d", &V[i], &v, &X[i], &u);
            V[i] = V[i] * 10000 + v;
            X[i] = X[i] * 10000 + u;
            //cout<<V[i]<<" "<<X[i]<<endl;
        }
        //continue;
        printf("Case #%d: ", tt);
        if (n == 1){
            if (X[0] == temp0){
                printf("%.9lf\n", (double)v0 / V[0]);
            }else cout<<"IMPOSSIBLE\n";
        }else{
            if (X[0] == X[1]){
                if (X[0] == temp0){
                    printf("%.9lf\n", (double)v0 / (V[0] + V[1]));
                }else cout<<"IMPOSSIBLE\n";
            }else{
                double b = (((double)v0 * X[0] - (double)v0 * temp0) / ((double)X[0] - X[1]));
                b /= V[1];
                double a = ((double)v0 - b * V[1]) / V[0];
                if (a < 0 || b < 0) cout<<"IMPOSSIBLE\n";
                else
                printf("%.9lf\n", max(a, b));
            }
        }
    }

}
