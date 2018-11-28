#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;
int i,j,n,m,T,a[200],kol;
int main()
{
    freopen("2.in","r",stdin);
    freopen("2.out","w",stdout);
    cin >> T;
    for (int cas=1;cas<=T;cas++)
    {
        cout << "Case #" << cas << ": ";
        kol=0;
        cin >> n >> m;
        for (i=0;i<m;i++)
            cin >> a[i];
        sort(a,a+m);
        for (i=0;i<m;i++)
            if (a[i]<n)
                n+=a[i];
            else
            {
                for (j=0;j<m-i;j++)
                {
                    kol++;
                    n+=(n-1);
                  //  cout << j << " " << n << " " << a[i] << endl;
                    if (n>a[i])
                    {
                        n+=a[i];
                        break;
                    }
                }
                if (j==m-i)
                {

                    break;
                }
            }
        cout << kol << endl;
    }
    return 0;
}

