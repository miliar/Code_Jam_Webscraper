#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <vector>
#include <bitset>
#include <cassert>
//Because defining using namespace std is too mainstream
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int,int> pii;
typedef pair<double,double> pdd;
typedef pair<string,string> pss;
typedef pair<int,double> pid;
typedef pair<int,LL> pil;
typedef pair<LL,LL> pll;

#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define SYNC ios_base::sync_with_stdio(false)
#define TIE cin.tie(0)
#define INF 1000000000
#define INFLL 4000000000000000000LL
#define EPS 1e-9
#define MOD 1000000007LL
#define DEBUG puts("DEBUG")

#ifdef _WIN32
    #define getchar_unlocked getchar
#endif

#define g getchar_unlocked

int dx8[8]={-1,-1,0,1,1,1,0,-1},dx4[4]={-1,0,1,0};
int dy8[8]={0,-1,-1,-1,0,1,1,1},dy4[4]={0,-1,0,1};

inline void open(string name){
    freopen((name+".in").c_str(),"r",stdin);
    freopen((name+".out").c_str(),"w",stdout);
}

inline void close(){
    fclose(stdin);
    fclose(stdout);
}

inline int io(){
    register char c;
    while(1){
        c = g();
        if(c != '\n' && c != ' ') break;
    }
    int res = 0, sign = 1;
    if(c=='-') sign = -1;
    else       res = c-'0';
    while(1){
        c = g();
        if(c == ' ' || c == '\n' || c == EOF) break;
        res = (res << 3) + (res << 1) + c - '0';
    }
    return res * sign;
}

///////////////////////////////////////////////////
//////            End of Template            /////
/////////////////////////////////////////////////

const int N = 1005;

int n,tc;
int arr[N];

int main(){
    scanf("%d",&tc);
    for(int t = 1 ; t <= tc ; t++){
        scanf("%d",&n);
        int maks = -1;
        for(int i = 1 ; i <= n ; i++){
            scanf("%d",&arr[i]);
            maks = max(maks,arr[i]);
        }
        int ans = INF;
        for(int i = 1 ; i <= maks ; i++){
            int cnt = i;
            for(int j = 1 ; j <= n ; j++)
                cnt += (arr[j] - 1) / i;
            ans = min(ans,cnt);        
        }
        printf("Case #%d: %d\n",t,ans);
    }
    //puts("ganteng");
    return 0;
}

