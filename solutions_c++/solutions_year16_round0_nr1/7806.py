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

int func(int n)  {
    bool chk[11];
    MEM(chk, 0);
    int cnt = 0;
    int i;

    int cc = 0;

    for(i = n; ; i += n)   {
        cc++;
        int tmp = i;
        while(tmp)  {
            int kk = tmp % 10;
            if(chk[kk] == 0)    {
                cnt++;
                chk[kk] = 1;
            }
            tmp /= 10;
        }
        if(cnt >= 10)   {
            break;
        }
        /*
        if(i < n)   {
            cout << "hoinai\n";
        }
        */
        if(cc > 200)    {
            return -1;
        }
    }
    return i;
}

int main() {
    /*
    FOR(i, 1000000 - 100, 1000000)   {
        int kk = func(i);
        if(kk == -1)   {
            cout << i << "\n";
            //break;
            return 0;
        }
        if(kk < i)   {
            cout << "hoinai\n";
        }

        cout << i << " : " << func(i) << "\n";
    }
    cout << "hoise\n";
    */
    ///*
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int tc;
    cin >> tc;
    FOR(tt, 1, tc)  {
        int n;
        cin >> n;
        cout << "Case #" << tt << ": ";
        if(n == 0)  {
            cout << "INSOMNIA\n";
            continue;
        }

        cout << func(n) << "\n";
    }
    //*/
    return 0;
}
/*
5
0
1
2
11
1692
*/
