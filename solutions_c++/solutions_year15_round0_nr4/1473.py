#include<bits/stdc++.h>

using namespace std;

#define vi vector < int >
#define pii pair < int , int >
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define foreach(it,v) for( __typeof((v).begin())it = (v).begin() ; it != (v).end() ; it++ )
#define ll long long
#define llu unsigned long long
#define MOD 1000000007
#define INF 0x3f3f3f3f
#define dbg(x) { cout<< #x << ": " << (x) << endl; }
#define dbg2(x,y) { cout<< #x << ": " << (x) << " , " << #y << ": " << (y) << endl; }
#define all(x) x.begin(),x.end()
#define mset(x,v) memset(x, v, sizeof(x))
#define sz(x) (int)x.size()

int main()
{
    freopen("D.in","r",stdin);
    freopen("D.out","w",stdout);
    int t,tc=1;
    scanf("%d",&t);
    while(t--)
    {
        int x,r,c;
        scanf("%d%d%d",&x,&r,&c);
        int f;
        if(x == 1)
            f = 0;
        else if(x == 2)
        {
            if(r*c == 1 || r*c == 3 || (r == 3 && c == 3))
                f = 1;
            else
                f = 0;
        }
        else if(x == 3)
        {
            if(r == 1 || c == 1)
                f = 1;
            else if(r == 3 || c == 3)
                f = 0;
            else
                f = 1;
        }
        else
        {
            if((r == 4 && c == 4) || (r == 4 && c == 3) || (r == 3 && c == 4))
                f = 0;
            else
                f = 1;
        }

        printf("Case #%d: ",tc++);

        if(f)
            printf("RICHARD\n");
        else
            printf("GABRIEL\n");
    }
    return 0;
}

