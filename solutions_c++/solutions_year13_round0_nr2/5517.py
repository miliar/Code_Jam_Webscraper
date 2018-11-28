#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
using namespace std;

int T,n,m,Maxi=-1,a[105][105];
bool Valid_Rows[105],Valid_Cols[105];
bool check_row (int row)
{
    int temp = a[row][0];
    for (int j=1;j<m;j++)
        if (a[row][j]!=temp) return 0;
    return 1;
}
bool check_col (int col)
{
    int temp = a[0][col];
    for (int j=1;j<n;j++)
        if (a[j][col]!=temp) return 0;
    return 1;
}
int main ()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("write.txt","w",stdout);
    cin >>T ;
    int t = 1;
    while (T--)
    {
        Maxi=-1;
        cin >> n >> m;
        for (int i=0;i<n;i++)
            for (int ii=0;ii<m;ii++)
                cin >> a[i][ii],Maxi = max(Maxi,a[i][ii]);
        memset(Valid_Rows,0,sizeof Valid_Rows);
        memset(Valid_Cols,0,sizeof Valid_Cols);

        for (int i=0;i<n;i++)
            Valid_Rows[i]=check_row(i);

        for (int i=0;i<m;i++)
            Valid_Cols[i]=check_col(i);

        bool No=0;

        for (int i=0;i<n;i++)
        {
            for (int j=0 ;j<m;j++)
            {
                if (a[i][j]==Maxi) continue ;
                if (Valid_Rows[i] || Valid_Cols[j]) continue;
                No = 1;
                break;
            }
            if (No) break;
        }
        cout << "Case #" << t++ << ": ";
        No ? cout << "NO\n" : cout << "YES\n";

    }
    return 0;
}


