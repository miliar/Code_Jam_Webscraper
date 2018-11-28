/*
TASK: The Last Word
LANG: C++
*/
#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second
#define EPS 1e-9
#define ALL(x) (x).begin(),(x).end()
#define mp(x,y) make_pair((x),(y))
#define pb(x) push_back((x))
#define FOR(i,st,ed) for(int (i)=(st);(i)<(ed);(i)++)
typedef pair<int,int> PII;
typedef vector<int> vi;
typedef vector<pair<int,int> > vii;
typedef long long LL;

int N,M,T;
int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int i,j,k;
    cin >> T;
    int tt=0;
    while(T--)
    {
        string s;
        tt++;
        deque<char> Q;
        cin >> s;
        Q.push_back(s[0]);
        for(i=1;i<s.size();i++)
        {
            if(s[i]>=Q.front())
                Q.push_front(s[i]);
            else
                Q.push_back(s[i]);
        }
        printf("Case #%d: ",tt);
        while(!Q.empty())
        {
            printf("%c",Q.front());
            Q.pop_front();
        }
        printf("\n");
    }
}
