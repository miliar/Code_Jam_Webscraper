#include <iostream>
#include <algorithm>

using namespace std;

int main(int argc,char *argv[])
{
    int t,inp[5][5],cmp[2][5],a,n,ans;
    cin >> t;
    for(int h = 1;h <= t;h++)
    {
        n = 0;
        for(int k = 0;k < 2;k++)
        {
            cin >> a;
            for(int i = 0;i < 4;i++)
            {
                for(int j = 0;j < 4;j++)
                {
                    cin >> inp[i][j];
                }
            }
            for(int i = 0;i < 4;i++)
                cmp[k][i] = inp[a-1][i];
        }
        sort(&cmp[0][0],&cmp[0][4]);
        sort(&cmp[1][0],&cmp[1][4]);
        for(int i = 0;i < 4;i++)
        {
            if(binary_search(&cmp[0][0],&cmp[0][4],cmp[1][i]))
            {
                n++;
                ans = cmp[1][i];
            }
        }
        cout << "Case #" << h << ": ";
        if(n == 1)
            cout << ans;
        else if(n == 0)
            cout << "Volunteer cheated!";
        else
            cout << "Bad magician!";
        cout << endl;
    }

    return 0;
}
