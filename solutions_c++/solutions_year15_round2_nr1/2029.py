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

string va, vb;
inline bint rev(bint v) {
    va = tos(v);
    vb = va;
    reverse(ALL(vb));
    
    bint ret;
    stringstream ss;
    ss << vb;
    ss >> ret;
    return ret;
}

const int LM = 1000007;
bint dp[LM];

int main() {
    
    //freopen("in.txt", "r", stdin);
    freopen("A-small-attempt2.in", "r", stdin);
    freopen("A-small-attempt2.out", "w", stdout);
    
    int T;
    
    FOR(i,0,LM)dp[i] = LM+7;
    dp[0] = 0;
    
    FOR(i,1,LM) {
        dp[i] = min(dp[i], dp[i-1]+1);
        bint rN = rev(i);
        if(rN < LM)dp[rN] = min(dp[rN], dp[i]+1);
    }
    
    bint N;
    cin >> T;
    FOR(t,0,T) {
        cin >> N;
        printf("Case #%d: ", 1+t);
        cout << dp[N] << endl;
    }
    
    return 0;
}

/*                       _        _                       _           _ 
         ___  ___  _   _| |    __| | ___ _ __   __ _ _ __| |_ ___  __| |
        / __|/ _ \| | | | |   / _` |/ _ \ '_ \ / _` | '__| __/ _ \/ _` |
        \__ \ (_) | |_| | |  | (_| |  __/ |_) | (_| | |  | ||  __/ (_| |
        |___/\___/ \__,_|_|___\__,_|\___| .__/ \__,_|_|   \__\___|\__,_|
        Mukit Hasan, Jahangirnagar University.*/
