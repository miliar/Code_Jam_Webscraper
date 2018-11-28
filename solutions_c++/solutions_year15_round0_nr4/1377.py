/*
TASK: Problem D. Ominous Omino
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
    freopen("D-small-attempt0.in","r",stdin);
    freopen("xxx.out","w",stdout);
    int i,j,k;
    cin >> T;
    int tt=0,X,R,C;
    while(T--)
    {
        cin >> X >> R >> C;
        tt++;
        if(R>C) swap(R,C);
        k=0;
        if(X==1)    k=1;
        else if(X==2)
        {
            if((R*C)%2==0)  k=1;
        }
        else if(X==3)
        {
            if(R>=2 && (R*C)%3==0)
                k=1;
        }
        else if(X==4)
        {
            if(R>=3 && (R*C)%4==0)
                k=1;
        }

        printf("Case #%d: %s\n",tt,k? "GABRIEL":"RICHARD");
    }
}
