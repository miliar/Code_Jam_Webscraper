///*********************************
///***Author: Nguyen The Thong
///***Email: nguyenthethong1996@gmail.com
///*********************************

#include <bits/stdc++.h>
using namespace std;

#define fto(i,a,b) for (int i = (a), _b = (b); i <= _b; i++)
#define fdw(i,a,b) for (int i = (a), _b = (b); i >= _b; i--)
#define read(a) scanf("%d", &a)
#define write(a) printf("%d", a)
#define read64(a) scanf("%I64d", &a);
#define write64(a) printf("%I64d", a);
#define debug(a) cout << #a << " = " << a << endl
#define ooLL 1000000000000LL
#define oo 1000000000
#define maxn 100005
#define eps 0.000000001

#define sz(a) int((a).size())
#define all(c) (c).begin(), (c).end()
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define pb push_back
#define mp make_pair

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
typedef long long ll;

int GCD(int a, int b){return(b==0?a:GCD(b,a%b));}
int LCM(int a, int b){return a*(b/GCD(a,b));}

map<long long, int> m;
long long numtest, x, n;
bool check[20];

bool checkOK(long long t) {
    int k;

    while (t > 0) {
        k = t % 10;
        check[k] = true;
        t /= 10;
    }

    for(int i = 0; i <= 9; i++)
        if (check[i] == false) return false;

    return true;
}

int main() {
    freopen("A-large.in","r",stdin);
    freopen("ou.out","w",stdout);

    scanf("%d", &numtest);
    for(int test = 1; test <= numtest; test++) {
        scanf("%d", &x); //  debug(x);

        m.clear();
        for(int i = 0; i <= 9; i++) check[i] = false;
        n = x;

        while (1) {

            if (checkOK(n)) {
                printf("Case #%d: %lld\n", test, n);
                break;
            }
            if (m.find(n) != m.end()) {
                printf("Case #%d: INSOMNIA\n", test);
                break;
            }
            else m[n] = 1;

            n += x;
        }
    }
}

///Copyright by NguyenTheThong
