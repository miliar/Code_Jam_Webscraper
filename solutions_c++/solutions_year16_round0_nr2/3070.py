/*
TASK: Revenge of the Pancakes
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
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int i,j,k;
    cin >> T;
    int tt=0,Mc,Me;
    string s;
    while(T--)
    {
        tt++;
        cin >> s;
        Mc=0;   Me=1;
        for(i=0;i<s.size();i++)
            if(s[i]=='-')   Mc=1,s[i]='+';
            else    break;
        for(i=1;i<s.size();i++)
            if(s[i]!=s[i-1])
                Me++;
        Me/=2;
        printf("Case #%d: %d\n",tt,Mc+Me*2);
    }
}
