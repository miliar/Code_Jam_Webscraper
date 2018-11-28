#include <iostream>
#include <fstream>
using namespace std;
int main()
{
    ifstream cin("in.txt");
    ofstream cout("out.txt");
    int t;
    cin>>t;
    for (int T=0;T<t;T++)
    {
        int n = 4;
        int dot = 0;
        char ar[5][5];
        for (int i=0;i<n;i++)
        for (int j=0;j<n;j++)
        {
            char c;
            cin>>c;
            if (c == '.') dot = 1;
            ar[i][j] = c;
        }
        cout<<"Case #"<<T+1<<": ";
        int ans = 0;
        for (int i=0;i<n;i++)
        {
            int X = 0, O = 0, add = 0;
            for (int j=0;j<n;j++)
                if (ar[i][j] == 'X') X++;
                else if (ar[i][j] == 'O') O++;
                else if (ar[i][j] == 'T') add=1;
            if (X+add == n) ans = 1;
            if (O+add == n) ans = 2;
        }
        for (int j=0;j<n;j++)
        {
            int X = 0, O = 0, add = 0;
            for (int i=0;i<n;i++)
                if (ar[i][j] == 'X') X++;
                else if (ar[i][j] == 'O') O++;
                else if (ar[i][j] == 'T') add=1;
            if (X+add == n) ans = 1;
            if (O+add == n) ans = 2;
        }
        int X = 0, O = 0, add = 0;
        for (int i=0;i<n;i++)
            if (ar[i][i] == 'X') X++;
            else if (ar[i][i] == 'O') O++;
            else if (ar[i][i] == 'T') add=1;
        if (X+add == n) ans = 1;
        if (O+add == n) ans = 2;
        X = 0, O = 0, add = 0;
        for (int i=0;i<n;i++)
            if (ar[i][n-i-1] == 'X') X++;
            else if (ar[i][n-i-1] == 'O') O++;
            else if (ar[i][n-i-1] == 'T') add=1;
        if (X+add == n) ans = 1;
        if (O+add == n) ans = 2;
        if (ans == 1)
            cout<<"X won\n";
        if (ans == 2)
            cout<<"O won\n";
        if (ans == 0 && !dot)
            cout<<"Draw\n";
        if (ans == 0 && dot)
            cout<<"Game has not completed\n";
    }
    return 0;
}
