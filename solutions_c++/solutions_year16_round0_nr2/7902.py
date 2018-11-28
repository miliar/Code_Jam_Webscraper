//uva 12425
#include<bits/stdc++.h>

using namespace std;

#define PF           printf
#define SF(n)        scanf("%d", &n)
#define SFF(a,b)     scanf("%d %d", &a, &b)
#define SFFF(a,b,c)  scanf("%d %d %d", &a, &b, &c)
#define INF_I        2147483647    //max limit
#define INF          1999999999
#define PB           push_back
#define MEM(n, val)  memset((n), val, sizeof(n))
#define F            first
#define S            second
#define FOR(i, a, b) for(int i = a; i <= b; i++)
#define ROF(i, a, b) for(int i = a; i >= b; i--)
#define ALL(c)       c.begin(), c.end()
#define BOOST        std::ios_base::sync_with_stdio(false);
#define INP          freopen("in.txt", "r", stdin);
#define OUT          freopen("out.txt", "w", stdout);
#define MP           make_pair
#define INIT_RAND    srand(time(NULL))
#define MOD          1000000007
#define MX           10010
#define PI           acos(-1.0)

typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int, int> PII;
typedef pair<long long, long long> PLL;
typedef priority_queue<int> P_Q;
typedef queue<int> Q;
typedef stringstream SS;

/*dir array
//8 moves
int fx[]={+0,+0,+1,-1,-1,+1,-1,+1};
int fy[]={-1,+1,+0,+0,+1,+1,-1,-1};
//4 moves
int fx[]={+1,-1,+0,+0};
int fy[]={+0,+0,+1,-1};
#define valid(nx,ny)  ((nx >= 0) && (nx < row) && (ny >= 0) && (ny < col))
*/

int func(string str)  {
    int len = str.size();
    /*
    if(len == 1)    {
        if(str[0] == '-')    {
            return 1;
        }
        return 0;
    }
    */
    int ans = 0;
    int i = 0;
    char past;
    for(i = 0; i < len; i++)   {
        past = str[i];
        bool chk = 0;
        while((past == str[i] && (i < len))) {
            i++;
            chk = 1;
        }
        //i--;
        if(i == len)    {
            ///*
            if(past == '-') {
                ans++;
            }
            //*/
            break;
        }
        /*
        if(past == '+') {
            ans += 2;
        }
        else    {
            ans++;
        }
        */
        ans++;
        if(chk) {
            i--;
        }
    }
    return ans;
}

int main() {

    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int tc;
    cin >> tc;
    FOR(tt, 1, tc)  {
        string str;
        cin >> str;
        cout << "Case #" << tt << ": " << func(str) << "\n";
    }
    //*/
    return 0;
}
/*
5
-
-+
+-
+++
--+-

10
*/
