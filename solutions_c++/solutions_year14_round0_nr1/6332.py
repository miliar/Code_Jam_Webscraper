#include <iostream>
# include <cstdio>
using namespace std;

int main()
{
    //freopen("1.in","r",stdin);
    //freopen("1.out","w",stdout);

    int t;
    cin >> t;
    for(int ci = 1; ci <= t; ++ci)
    {
        int a1,a2,num1[5][5],num2[5][5];
        cin >> a1 ;
        for(int i = 1; i <= 4 ; ++i)
            for(int j = 1; j <=4 ; ++j)
                cin >> num1[i][j];

        cin >> a2 ;
        for(int i = 1; i <= 4 ;++i)
            for(int j = 1; j <=4 ; ++j)
                cin >> num2[i][j];

        int find = 0,ans;
        for(int i = 1;  i <= 4; ++i)
            for(int j = 1; j <= 4; ++j)
                if (num1[a1][i] == num2[a2][j])
                {
                    find++;
                    ans = num1[a1][i];
                }


        cout << "Case #" << ci << ": " ;
        if (find == 0) cout << "Volunteer cheated!";
        else if (find == 1) cout << ans ;
        else cout << "Bad magician!";
        cout << endl;
    }

    return 0;
}
