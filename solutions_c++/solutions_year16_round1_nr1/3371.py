
#include<bits/stdc++.h>
using namespace std;
#define D(x)        cout<<#x " = "<<(x)<<endl
#define un(x)       x.erase(unique(x.begin(),x.end()), x.end())
#define sf(n)       scanf("%d", &n)
#define sff(a,b)    scanf("%d %d", &a, &b)
#define sfff(a,b,c) scanf("%d %d %d", &a, &b, &c)
#define pb          push_back
#define mp          make_pair
#define xx          first
#define yy          second
#define hp          (LL) 999983
#define MAX         100000
typedef long long int LL;

string str, res;

int main()
{
    freopen("c:\\Users\\User\\Desktop\\in.txt", "r", stdin);
    freopen("c:\\Users\\User\\Desktop\\out.txt", "w", stdout);

    int i, j, k, cs, t, pre;
    int st;

    sf(t);
    for(cs = 1; cs <= t; cs++)
    {
        cin >> str;

        res = str[0];
        pre = 0;

        for(i = 1; i < str.size(); i++)
        {
            if(str[i] >= str[pre])
            {
                res = str[i] + res;
                pre = i;
            }
            else res += str[i];
        }

        printf("Case #%d: %s\n", cs, res.c_str());
    }
    return 0;
}




