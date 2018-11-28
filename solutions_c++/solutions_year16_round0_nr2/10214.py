#include<bits/stdc++.h>
#define needforspeed ios::sync_with_stdio(0);cin.tie(0);
#define scan(x) do{while((x=getchar())<'0'); for(x-='0'; '0'<=(_=getchar()); x=(x<<3)+(x<<1)+_-'0');}while(0)
char _;
#define endl '\n'
#define pb push_back
#define mp make_pair
#define mp3(a,b,c) make_pair(a,make_pair(b,c))
#define mp4(a,b,c,d) make_pair(make_pair(a,b),make_pair(c,d))
#define trace1(a) cout << (a) << endl;
#define trace2(a,b) cout << (a)  << " " << (b) << endl;
#define trace3(a,b,c) cout << (a)  << " " << (b) << " " << (c) << endl;
#define trace4(a,b,c,d) cout << (a)  << " " << (b) << " " << (c) <<  " " << (d) << endl;
#define trace5(a,b,c,d,e) cout << (a)  << " " << (b) << " " << (c) <<  " " << (d) <<  " " << (e) << endl;
#define ms(a,b) memset( (a), (b), sizeof(a))
#define fi(x) freopen(x,"r",stdin)
#define fo(x) freopen(x,"w",stdout)
#define wi(x) for(int  (i) = (0); (i) < (x);(i)++)
#define wj(x) for(int  (j) = (0); (j) < (x);(j)++)
#define wk(x) for(int  (k) = (0); (k) < (x);(k)++)
#define all(x) (x).begin(),(x).end()
#define len(x) (int)(x).size()
#define xx first
#define yy second
#define ll long long
#define pii pair<int,int>
#define pll pair<ll,ll>
#define MAXN (int)1e9
#define inf 0x3f3f3f3f
#define nullptr 0
#define db 0
using namespace std;

int T;
int final_state;
string S;
int dist[1<<10];

int bfs(int start_state)
{
    queue< pair<int,int> >q;
    q.push(mp(start_state, 0));
    dist[start_state] = 0;
    while(!q.empty())
    {
        int state = q.front().xx;
        int cdist = q.front().yy;
        q.pop();
        for(int i = 0;i < len(S);i++)
        {
            state ^= (1<<i);
            if(dist[state] > cdist+1)
            {
                dist[state] = cdist+1;
                q.push(mp(state, dist[state]));
            }
        }
    }
    return dist[final_state];
}

void print(int x)
{
    for(int i = 0;i < len(S);i++)
    {
        cout << ((x & 1 <<i) ? 1:0);
    }cout << endl;
}

int main()
{
    freopen("B-input.txt","r",stdin);
    needforspeed;
    cin >> T;
    for(int t = 1;t != T+1;t++)
    {
        cin >> S;
        int state = 0;
        final_state = 0;
        ms(dist, inf);
        for(int j = 0;j != len(S);j++)
        {
            if(S[j] == '+')
            {
                state |= (1<<j);
            }
            final_state |= (1<<j);
        }
        if(db)
        {
            print(state);
            print(final_state);
        }
        int ans = bfs(state);
        cout << "Case #" << t << ": " << ans << endl;
    }
    return 0;
}