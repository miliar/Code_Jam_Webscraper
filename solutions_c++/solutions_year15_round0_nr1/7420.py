#include<bits/stdc++.h>
#define mp make_pair
#define pb push_back
#define pii pair<int,int>
#define ll long long
#define ull unisgned long long
#define read freopen("input.txt","r",stdin)
#define write freopen("output.txt","w",stdout)
#define vi vector<int>
#define MAX 200005
#define all(v) v.begin(), v.end()
#define PI acos(-1.0)
#define mem(ara, value) memset(ara, value, sizeof(ara))
#define sf scanf
using namespace std;



int main()
{
    int testCase,x,y,m,n,k;
    read;
    write;
    cin>>testCase;
    for(int qq=1;qq<=testCase; qq++)
    {
        string z;
        cin>>x>>z;
        int extra=0,c=0;
        for(int i=0;i<=x; i++)
        {
            if(c>=x)
                break;
            if(z[i]!='0')
            {
                if(c<i)
                {
                    extra+=i-c;
                    c+=i-c;
                }
                c+=z[i]-48;
            }

        }
        printf("Case #%d: %d\n", qq, extra);
    }
    return 0;
}
