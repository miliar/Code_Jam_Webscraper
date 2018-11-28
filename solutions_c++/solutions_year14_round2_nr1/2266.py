#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;
char line[200];
int T,TST_CASE;
int N;
vector<pair<char,int> > A[105];
vector<int> DP[105];

void read()
{
    int len;
    scanf("%d",&N);
    for(int i = 1; i <= N; ++i)
    {
        scanf("%s",line);
        len = strlen(line);
        int ap = 1;
        for(int j = 1; j <= len; ++j)
        {
            if(line[j] == line[j-1]) ++ ap;
            else{
                A[i].push_back(make_pair(line[j-1],ap));
                ap = 1;
            }
        }
    }
}

int abso(int k)
{
    if(k < 0) return -k;
    return k;
}

void solve()
{
    int x = A[1].size();
    for(int i = 2; i <= N; ++i)
        if(x != A[i].size())
        {
            printf("Case #%d: Fegla Won\n",TST_CASE);
            return;
        }
    for(int j = 0; j < A[1].size(); ++j)
        for(int i = 2; i <= N; ++i)
        {
            if(A[i][j].first != A[i-1][j].first)
            {
                printf("Case #%d: Fegla Won\n",TST_CASE);
                return;
            }
        }
    int medi;
    long long ans = 0;
    for(int j = 0; j < A[1].size(); ++j)
    {
        for(int i = 1; i <= N; ++i)
            DP[j].push_back(A[i][j].second);
        sort(DP[j].begin(),DP[j].end());
        medi = DP[j][(int)DP[1].size()/2];
        for(int k = 0; k < DP[j].size(); ++k)
        ans += abso(medi-DP[j][k]);
    }
    printf("Case #%d: %lld\n",TST_CASE,ans);
}

void init()
{
    for(int i = 0; i <= N; ++i)
        A[i].clear();
    for(int i = 0; i <= 101; ++i )
        DP[i].clear();
}

int main()
{
    freopen("repeat.in","r",stdin);
    ///freopen("repeat.out","w",stdout);
    freopen("repeat.txt","w",stdout);

    scanf("%d",&T);
    while(T--){
        ++TST_CASE;
        read();
        solve();
        init();
    }
    return 0;
}
