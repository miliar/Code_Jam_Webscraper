// RandomUsername (Nikola Jovanovic)
// GCJ 2016 R2
// C

#include <bits/stdc++.h>
#define DBG false
#define debug(x) if(DBG) printf("(ln %d) %s = %d\n", __LINE__, #x, x);
#define lld long long
#define ff(i,a,b) for(int i=a; i<=b; i++)
#define fb(i,a,b) for(int i=a; i>=b; i--)
#define par pair<int, int>
#define fi first
#define se second
#define mid (l+r)/2
#define INF 1000000000
#define MAXN 100005

using namespace std;

int t, n;
char tmp[10];
string V = "";
bool taken[4] = {false, false, false, false};

bool possible_perm(string U, int* perm, int it)
{
    if(n == 2)
    {
       // cout<<"possible_perm "<<U<<" "<<perm[0]<<" "<<perm[1]<<" "<<it<<" "<<n<<endl;
        //cout<<"taken: "<<taken[0]<<" "<<taken[1]<<endl;
    }
    if(it == n) return true;
    bool ret = true;
    // i am it
    bool ass = false;
    ff(machine, 0, n-1)
    {
        if(!taken[machine] && U[ perm[it] * n + machine ]  == '1')
        {
           // cout<<"assigned machine "<<machine<<" to dude "<<perm[it]<<endl;
            ass = true;
            taken[machine] = true;
            ret &= possible_perm(U, perm, it+1);
            taken[machine] = false;
        }
    }
   // cout<<"assigned at all "<<ass<<endl;
    if(!ass) return false;
    return ret;
}

bool is_possible(string U)
{
    bool ret = true;
    int perm[4] = {0, 1, 2, 3};
    do
    {
        // must be possible for all perms and all pickings
     //   cout<<" perm "<<U<<" "<<perm[0]<<" "<<perm[1]<<endl;
        ret &= possible_perm(U, perm, 0);
    }while(next_permutation(perm, perm+n));
    return ret;
}

int main()
{
    freopen("C.in", "r", stdin);
    freopen("C.out", "w", stdout);
    scanf("%d", &t);
    ff(tt, 1, t)
    {
        fprintf(stderr, "cao %d\n", tt);
        V = "";
        scanf("%d", &n);
        ff(i, 0, n-1)
        {
            scanf("%s", tmp);
            V += tmp; // n^2
        }
        // try all spendings
        // validate every
        int MASKS = (1 << (n*n));
        int minSpent = 200;
        ff(MASK, 0, MASKS - 1)
        {
            // spendings?
            int spent = __builtin_popcount(MASK);
            if(minSpent < spent) continue; // we have better
            string U = V;
            bool valid = true;
            ff(bit, 0, n*n-1)
            {
                if( (MASK & (1 << bit)) != 0)
                {
                    if(U[bit] == '1')
                    {
                        valid = false;
                        break;
                    }
                    U[bit] = '1';
                    //bit set
                }
            }
            if(!valid) continue;
            // valid test it
          //  printf("Testing %s\n", U.c_str());
            bool POSS = is_possible(U);
         //   cout<<POSS<<" possible!"<<endl;
            if(POSS) minSpent = min(minSpent, spent);
        }
        printf("Case #%d: %d\n", tt, minSpent);
    }
    return 0;
}
