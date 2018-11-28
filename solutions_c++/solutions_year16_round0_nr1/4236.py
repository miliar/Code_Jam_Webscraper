
/*
** Author:       rd4tta95
** DateTime:     1157090416(ist)
** Problem Code: GCJ2016_Qualifier_A
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
#define Case(i,n) cout<<"Case #"<<(int)(i+1)<<": "<<n<<endl;
#define print(x) cout<<x<<endl;

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
        ll n;
        cin>>n;
        ll t = n;
        char arr[10]={0};
        int s = 0;
        if(n==0)
        {
            Case(currentCase,"INSOMNIA");
            continue;
        }
        while(s!=10)
        {
            ll c = n;
            while(c>0)
            {
                if(arr[c%10] == 0)
                {
                    arr[c%10] = 1;
                    s++;
                }
                c/=10;
            }
            if(s==10)
                break;
            n+=t;
        }
        Case(currentCase,n);
    }
    return 0;
}