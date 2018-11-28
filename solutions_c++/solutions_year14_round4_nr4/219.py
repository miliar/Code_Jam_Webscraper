/*********************************************************************\
   |--\        ---       /\        |-----------| -----   /-------|    |
   |   \        |       /  \       |               |    /             |
   |    \       |      /    \      |               |   |              |
   |     \      |     /      \     |               |   |----|         |
   |      \     |    / ------ \    |-------|       |        |-----|   |
   |       \    |   /          \   |               |              |   |
   |        \   |  /            \  |               |              /   |
  ---        -------            ------           ----- |---------/    |
                                                                      |
    codeforces = nfssdq  ||  topcoder = nafis007                      |
    mail = nafis_sadique@yahoo.com || nfssdq@gmail.com                |
    IIT,Jahangirnagar University(41)                                  |
                                                                      |
**********************************************************************/

#include <bits/stdc++.h>

using namespace std;

#define xx         first
#define yy         second
#define pb         push_back
#define mp         make_pair
#define LL         long long
#define inf        INT_MAX/3
#define mod        1000000007ll
#define PI         2.0*acos(0.0)
#define linf       (1ll<<60)-1
#define FOR(I,A,B) for(int I = (A); I < (B); ++I)
#define REP(I,N)   FOR(I,0,N)
#define ALL(A)     ((A).begin(), (A).end())
#define set0(ar)   memset(ar,0,sizeof ar)
#define vsort(v)   sort(v.begin(),v.end())
#define setinf(ar) memset(ar,126,sizeof ar)

//cout << fixed << setprecision(20) << p << endl;

template <class T> inline T bigmod(T p,T e,T M){
    LL ret = 1;
    for(; e > 0; e >>= 1){
        if(e & 1) ret = (ret * p) % M;
        p = (p * p) % M;
    } return (T)ret;
}
template <class T> inline T gcd(T a,T b){if(b==0)return a;return gcd(b,a%b);}
template <class T> inline T modinverse(T a,T M){return bigmod(a,M-2,M);}

struct node{
    node *n[27];
    node(){
        memset(n, NULL, sizeof n);
    }
};
int insert(node *ob, char *S){
    if(S[0] == '\0') return 0;
    int c = S[0] - 'A';
    int ret = 0;
    if(ob->n[c] == NULL) {
        ob->n[c] = new node();
        ret++;
    }
    ret += insert(ob->n[c], S + 1);
    return ret;
}
void del(node *ob){
    REP(i, 27) if(ob->n[i] != NULL) del(ob->n[i]);
    delete ob;
}
int pos[10];
char pp[10][101], tmp[101];
LL mx, mc;
void bctrack(int c, int n, int k){
    if(c == n){
        LL cnt = 0;
        node *tr[5];
        REP(i, 5) tr[i] = NULL;
        REP(i, n){
            memset(tmp, '\0', sizeof tmp);
            REP(j, strlen(pp[i])) tmp[j] = pp[i][j];
            if(tr[pos[i]] == NULL){
                tr[pos[i]] = new node();
                cnt++;
            }
            cnt += insert(tr[pos[i]], tmp);
        }
        if(cnt > mx) {
            mx = cnt;
            mc = 1;
        } else if(cnt == mx) mc++;
        REP(i, 5) if(tr[i] != NULL) del(tr[i]);
        return;
    }
    REP(i, k){
        pos[c] = i;
        bctrack(c + 1, n, k);
    }
}
main(){
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    ios_base::sync_with_stdio(0); cin.tie(0);
    LL a,b,c,d = 0,e = 0,f = 0,g,h = 0,x = 0,y,z;
    cin >> a;
    FOR(ts, 1, a + 1){
        cout << "Case #" << ts << ": ";
        cerr << "Case #" << ts << ": ";
        mx = mc = 0;
        cin >> b >> c;
        REP(i, b) cin >> pp[i];
        bctrack(0, b, c);
        cout << mx << " " << mc << endl;
        cerr << mx << " " << mc << endl;
     }
}

