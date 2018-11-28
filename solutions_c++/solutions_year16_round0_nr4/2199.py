#include <cstdio>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <ctime>
//#include <cmath>
#include <vector>
#include <map>
using namespace std;
typedef long long LL;
typedef pair<int,int> pint;
typedef pair<LL,LL> pll;
#define fi first
#define se second
typedef map<int,int> mapint;
typedef vector<int> vint;
typedef vector<vint> vintp;
#define rep(i,j,k) for (int i = (j);i <= (k);i ++)
#define repd(i,j,k) for (int i = (j);i >= (k);i --)
#define ran2 (rand() % 32000 * 32000 + rand() % 32000)
#define pb push_back
#define mp make_pair
#define SIZE(i) ((int)(i.size()))
int m,n,j,k,l,i,o,p,__t;
char ch;
void read(int &a) {
    for (ch = getchar();(ch < '0' || ch > '9') && (ch != '-');ch = getchar());
    if (ch == '-') a = 0,__t = -1; else a = ch - '0',__t = 1;
    for (ch = getchar();ch >= '0' && ch <= '9';ch = getchar()) a = a * 10 + ch - '0';
    a *= __t;
}

int K, C, S;

int main() {
    freopen("d.in","r",stdin);
    freopen("d.out","w",stdout);

    // for (int i = 1; i <= 1000000; i ++) {
    //     solve(i);
    // }

    int cas = 1, id;
    for (cin >> id; id --; cas ++) {
        cout << "Case #" << cas << ": ";
        cin >> K >> C >> S;
        vector<LL> ans;
        for (LL i = 1; i <= K; i ++) {
            LL ind = i;
            for (LL j = 1; j < C; j ++)
                ind = (ind - 1LL) * ((LL)K) + i;
            ans.push_back(ind);
        }
        for (int i = 0; i < ans.size(); i ++) {
            cout << ans[i] << ' ';        
        }
        cout << endl;

    }


    //fclose(stdin); fclose(stdout);
}
