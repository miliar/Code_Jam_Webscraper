#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T, cases = 0;
    cin >> T;
    while (T--)
    {
        cases ++;
        int n, m;
        int a[105][105];
        cin >> n >> m;
        for (int i = 0 ; i < n ; i++)
            for (int j = 0 ; j < m ; j++)
                cin >> a[i][j];
        bool flag = true;
        for (int i = 0 ; i < n ; i++)
            for (int j = 0 ; j < m ; j++)
            {
                int tot1 = 0, tot2 = 0;
                for (int k = 0 ; k < i ; k++)
                    if (a[k][j] > a[i][j])
                    {
                        tot1 ++;
                        break;
                    }
                for (int k = 0 ; k < j ; k++)
                    if (a[i][k] > a[i][j])
                    {
                        tot2 ++;
                        break;
                    }
                for (int k = i+1 ; k < n ; k++)
                    if (a[k][j] > a[i][j])
                    {
                        tot1 ++;
                        break;
                    }
                for (int k = j+1 ; k < m ; k++)
                    if (a[i][k] > a[i][j])
                    {
                        tot2 ++;
                        break;
                    }
                    //cout << i <<" "<<j<<" "<<tot1 << " and " << tot2 << endl;
                if (tot1 && tot2)
                {
                    flag = false;
                    break;
                }
            }
        cout << "Case #" << cases << ": ";
        if (flag) cout << "YES" << endl;
        else cout << "NO" << endl;
    }
}