#include<bits/stdc++.h>

using namespace std;

#define FOR(i,a,b)   	for(int (i)=(a);(i)<(b);(i)++)
#define PB           	push_back
#define INF          	(1 << 26)
#define DEBUG(___x)     cout<<#___x<<" = ["<<___x<<"]"<<endl
#define SORT(___a)      sort(___a.begin(),___a.end())
#define RSORT(___a)     sort(___a.rbegin(),___a.rend())
#define PI           	3.141592653589793238
#define MP           	make_pair
#define PII          	pair<int,int>
#define ALL(___v)       (___v).begin(), (___v).end()
#define VS           	vector<string>
#define VI           	vector<int>
#define S            	size()
#define B				begin()
#define E				end()
#define print(___v)     {cout<<"[";if(___v.S)cout<<___v[0];FOR(___i,1,___v.S)cout<<","<<___v[___i];cout<<"]\n";}
#define clr(___x, ___v)	memset(___x, ___v , sizeof ___x);
#define tr(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)

int tu(int val) {return (1 << val);}
bool iset(int mask, int id) {if((mask & tu(id) ) != 0)return true;return false;}
void doset(int &mask, int id) {mask |= tu(id);}
void dounset(int &mask, int id) {mask = mask & (~tu(id));}

typedef long long 					bint;
template<typename T> string tos( T a ) 	{ stringstream ss; string ret; ss << a; ss >> ret; return ret;}

const int LM = 1007;

int memo[LM][LM], arr[LM];

int dp(int N, int eat) {
    if(N <= eat)return 0;    
    
    int &ret = memo[N][eat];
    if(-1 != ret)return ret;
    
    ret = INF;
    if(eat > 0)ret = min(ret, dp(N-1, eat-1));
    
    for(int i = 1; i < N; i++) {
        int va = i; int vb = N-i;
        if(va > vb)break;
        
        int ra = dp(va, eat);
        if(ra < INF) {
            int rb = dp(vb, eat);
            if(rb < INF) {
                ret = min(ret, ra+rb+1);
            }
        }
    }
    
    return ret;
}

int main() {
    
    //freopen("in.txt", "r", stdin);
    freopen("B-large.in", "r", stdin);
    freopen("out_B-large-attempt0.out", "w", stdout);
    
    int T, D;
    clr(memo, -1);
    
    scanf("%d", &T);
    FOR(t,0,T) {
        
        int boro = -1;
        scanf("%d", &D);
        FOR(i,0,D)scanf("%d", &arr[i]);
        FOR(i,0,D)boro = max(boro, arr[i]);
        
        int res = boro;
        FOR(eat,0,LM) {
            int cost = eat;
            FOR(i,0,D) {
                int va = dp(arr[i], eat);
                if(va >= INF) {
                    cost = INF; // invalid
                    break;
                }
                
                cost += va;
            }
            if(cost < res)res = cost;
        }
        printf("Case #%d: %d\n",1+t,res);
    }
    
    return 0;
}

/*                       _        _                       _           _ 
         ___  ___  _   _| |    __| | ___ _ __   __ _ _ __| |_ ___  __| |
        / __|/ _ \| | | | |   / _` |/ _ \ '_ \ / _` | '__| __/ _ \/ _` |
        \__ \ (_) | |_| | |  | (_| |  __/ |_) | (_| | |  | ||  __/ (_| |
        |___/\___/ \__,_|_|___\__,_|\___| .__/ \__,_|_|   \__\___|\__,_|
        Mukit Hasan, Jahangirnagar University.*/
