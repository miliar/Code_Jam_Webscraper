#include<cassert>
#include<queue>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<iostream>
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
#define f(i,x,y) for(int i = x; i<y; i++)
#define FOR(it,A) for(typeof A.begin() it = A.begin(); it!= A.end(); it++)
#define quad(x) (x) * (x)
#define mp make_pair
#define clr(x, y) memset(x, y, sizeof x)
#define fst first
#define snd second
typedef pair<int, int> pii;
typedef long long ll;
typedef long long ld;
int mat[100][100];
int row[100];
int col[100];
bool puede(int n, int m){
    f(i, 0, n){
        row[i] = mat[i][0];
        f(j, 0, m) row[i] = max(row[i], mat[i][j]);
    }
    f(j, 0, m){
        col[j] = mat[0][j];
        f(i, 0, n) col[j] = max(col[j], mat[i][j]);
    }
    f(i, 0, n) f(j, 0, m){
       if(row[i] > mat[i][j] && col[j] > mat[i][j]) return false; 
    }
    return true;
}

int main(){
    int t; cin >> t;
    f(tt, 1, t + 1){
        int n, m; cin >> n >> m;
        f(i, 0, n) f(j, 0, m) cin >> mat[i][j];

        printf("Case #%d: %s\n", tt, puede(n, m) ? "YES" : "NO");
    }
}
