
/*
** Author:       rd4tta95
** DateTime:     142909042016(IST)
** Problem Code: GCJ2016_Qualifier_B
*/

#include <bits/stdc++.h>

using namespace std;

#define fastio ios::sync_with_stdio(false);
#define N NULL
#define MOD 1000000007
#define DEL 0.000000001
#define INF numeric_limits<int>::max();
#define endl '\n'
#define FOR(i,a,b) for(int i=(int)a; i<(int)b; ++i)
// #define fill(ptr, item) memset(ptr, item, sizeof(item))
#define print(i,n) cout<<"Case #"<<(int)(i+1)<<": "<<n<<endl;

typedef long l;
typedef long long ll;

int main(int argc, char const *argv[])
{
    fastio;
    cin.tie(0);
    cout.tie(0);
    int tCase, currentCase, index;
    cin>>tCase;
    FOR(currentCase,0,tCase)
    {
        string sides;
        cin>>sides;
        int l=sides.length(), swaps=0;
        for(index=l-1; index>=0; index--)
        {
            if(sides[index]=='-' && swaps%2==0)
                swaps++;
            else if(sides[index]=='+' && swaps%2==1)
                swaps++;
        }
        print(currentCase,swaps);
    }
    return 0;
}