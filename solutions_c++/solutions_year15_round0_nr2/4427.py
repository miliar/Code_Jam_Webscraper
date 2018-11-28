#include <bits/stdc++.h>

#define INF (1 << 29)
#define rep2(i,m,n) for(int i=(int)(m);i<(int)(n);i++)
#define rep(i,n) rep2(i,0,n)
#define EPS 1e-10

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> P;

int dx[4] = {-1,0,1,0};
int dy[4] = {0,1,0,-1};

int dish[20];

int solve(int n){
    int res = 0;
    rep(i,20){
        if(dish[i]>0) res = i;
    }
    rep2(i,max(2,n),20) if(dish[i]>0){
        dish[i]--;
        rep2(j,1,i){
            dish[j]++;
            dish[i-j]++;
            res = min(res,1+solve(n+1));
            dish[j]--;
            dish[i-j]--;
        }
        dish[i]++;
    }
    return res;
}

int main()
{
    int T;
    cin >> T;
    rep(case_num,T){
        int n;
        cin >> n;
        memset(dish,0,sizeof(dish));
        rep(i,n){
            int x;
            cin >> x;
            dish[x]++;
        }
        cout << "Case #" << case_num+1 << ": " << solve(n) << endl;
    }
    return 0;
}

