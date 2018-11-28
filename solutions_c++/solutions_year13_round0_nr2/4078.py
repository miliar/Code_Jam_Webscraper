#include <iostream>
#include <stdio.h>

using namespace std;

int A[110][110];

bool check(int n, int m)
{
    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < m; j++)
        {
            bool exit = false;

            bool var1 = true;
            for(int i2 = n -1 ; i2 >=0; i2--)
            {
                if(A[i2][j] > A[i][j])
                {
                    var1 = false;
                    break;
                }
            }
            if(var1){
                continue;
            }

            bool var3 = true;
            for(int j2 = m-1; j2 >=0; j2--)
            {
                if(A[i][j2] > A[i][j])
                {
                    var3 = false;
                    break;
                }
            }
            if(var3){
                continue;
            }

            return false;
        }
    }
    return true;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int tests;
    cin >> tests;
    for(int i2 = 0; i2 < tests; i2++)
    {
        int n, m;
        cin >> n >> m;
        for(int i = 0; i < n; i++)
        {
            for(int j = 0; j < m; j++)
            {
                cin >> A[i][j];
            }
        }


       cout << "Case #" << i2 + 1 << ": ";
        if(check(n ,m))
        {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }
    return 0;
}

