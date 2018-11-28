#include <iostream>
using namespace std;

int r,n,m,k;
int prod[20];
int a[3];

bool check(int x,int y,int z)
{
     for (int i=0;i<k;i++)
     {
         if (prod[i] == 1)
            continue;
         if (prod[i]%x)
            return false;
         if (prod[i]%y)
            return false;
         if (prod[i]%z)
            return false;
     }
     return true;
}

int dfs(int d, int p, int ref)
{
    if (d>=n)
    {
        if (p==ref)
           return 1;
        else
            return 0;
    }
    int res = 0;
    res += dfs(d+1,p*a[d],ref);
    res += dfs(d+1,p,ref);
    return res;
}

double calcprob(int x,int y,int z)
{
    double res = 1;
    for (int i=0;i<k;i++)
    {
        int total = dfs(0,1,prod[i]);
        res *= (double)total/8.0;
    }
    return res;
}
 
int main()
{
    freopen("C-small-1-attempt0.in","r",stdin);
    freopen("c_small.out","w",stdout);
    
    cin >> r;
    cin >> r >> n >> m >> k;
    int i,j;
            
    cout << "Case #1:" << endl;
    for (i=0;i<r;i++)
    {
        for (j=0;j<k;j++)
            cin >> prod[j];
        
        int ans[3];
        double res = 0;
        for (a[0]=2;a[0]<=m;a[0]++)
            for (a[1]=2;a[1]<=m;a[1]++)
                for (a[2]=2;a[2]<=m;a[2]++)
                {
                    //if (!check(a[0],a[1],a[2]))
                    //   continue;
                    double tmp = calcprob(a[0],a[1],a[2]);
                    if (tmp > res)
                    {
                        memcpy(ans, a, sizeof a);
                        res = tmp;
                    }
                }

        for (j=0;j<n;j++)
            cout << (char)(ans[j]+'0');
        cout << endl;
    }
}
