/**
     Programmer: S. Roy(CSE'12).
     ----------- HSTU, Dinajpur.
     Online Judge:
     Problem name:
     Imp. Algorithm:
**/
using namespace std;
#include<bits/stdc++.h>

#define sf scanf
#define pf printf

#define DEBUG1(x) cout << "> " << #x << ": " << x << endl
#define DEBUG2(x, y) cout << "> " << #x << ": " << x << " > " << #y << ": " << y << endl
#define DEBUG3(x, y, z) cout << "> " << #x << ": " << x << " > " << #y << ": " << y << " > " << #z << ": " << z << endl

/**--------------- Direction Arrays ------------------*/
//int dx[]={1,0,-1,0}; int dy[]={0,1,0,-1}; //4 Direction
//int dx[]={1,1,0,-1,-1,-1,0,1}; int dy[]={0,1,1,1,0,-1,-1,-1};//8 direction
//int dx[]={2,1,-1,-2,-2,-1,1,2}; int dy[]={1,2,2,1,-1,-2,-2,-1};//Knight Direction
/**--------------- Direction Arrays ------------------**/

int tot;
bitset<10> bs;
bool set_val(int n)
{
    int mod;
    while (n)
    {
        mod = n % 10;
        if (bs[mod] == 0)
        {
            tot++;
            bs[mod] = 1;
        }
        n = n / 10;
    }
    return (tot == 10);
}
int main()
{
//#ifndef ONLINE_JUDGE
//    freopen("A.txt", "r", stdin);
//    freopen("A_out.txt", "w", stdout);
//#endif // ONLINE_JUDGE

    int cnum, n;
    sf ("%d", &cnum);
    for (int cs = 1; cs <= cnum; cs++)
    {
        sf ("%d", &n);

        if (n == 0)
        {
            pf ("Case #%d: INSOMNIA\n", cs);
            continue;
        }

        tot = 0;
        bs.reset();
        int res = n;
        bool found = false;
        for (int i = 1; !found; i++)
        {
            res = n * i;
            found = set_val(res);
        }
        pf ("Case #%d: %d\n", cs, res);
    }

    return 0;
}
