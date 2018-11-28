#include <iostream>
#include <cstdio>
using namespace std;
int ntest;
int D;
int p[1010];

int main()
{
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    cin>>ntest;
    for (int kk =1 ;kk<=ntest; kk++)
    {
        cin>>D;
        int dmax = 0;
        for (int i = 1; i<=D; i++)
             {
                 cin>>p[i];
                 dmax = max(dmax,p[i]);
             }
        int ans = 1000000000;
        for (int i = 1; i<=dmax; i++)
        {
            int res = i;
            for (int j = 1; j<=D; j++)
            if (i <= p[j])
            {
                int l = p[j] - i;
                res = res + (l/i) + (l%i!=0);
            }
            ans = min(ans,res);
        }
        cout<<"Case #"<<kk<<": "<<ans<<"\n";
    }
    return 0;
}
