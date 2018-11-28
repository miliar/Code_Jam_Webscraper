#include<iostream>
#include<stack>
#include<queue>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<string>
#include<cstring>
#include<map>
#include<numeric>
#include<sstream>
#include<cmath>
using namespace std;
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define pb push_back
#define f(i,x,y) for(int i = x; i<y; i++ )
#define FORV(it,A) for(vector<int>::iterator it = A.begin(); it!= A.end(); it++)
#define FORS(it,A) for(set<int>::iterator it = A.begin(); it!= A.end(); it++)
#define quad(x) (x) * (x)
#define mp make_pair
#define clr(x, y) memset(x, y, sizeof x)
#define fst first
#define snd second
typedef pair<int, int> pii;
typedef long long ll;
typedef long double ld;
#define N 128

int M[N][N];
int n, m;

bool pode (int i, int j){
    int ans = 1;
    f (k, 0, m) if (M[i][k] > M[i][j]){
        ans =0;
    }
    if (ans) return 1;
    ans = 1;
    f (k, 0, n) if (M[k][j] > M[i][j]){
        ans =0;
    }
    return ans;
}

int main (){
    int t;
    cin >> t;
    f (tt, 1, t+1){
        printf("Case #%d: ", tt);
        cin >> n >> m;
        f (i, 0, n) f (j, 0, m) cin >> M[i][j];
        int ans = 1;
        f (i, 0, n) f (j, 0, m){
            if (!pode(i,j)) ans = 0;
        }        
        if (ans) printf("YES\n");
        else printf("NO\n");
    }
    return 0;
}
