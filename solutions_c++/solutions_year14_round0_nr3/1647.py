#include<cstdio>
#include<iostream>
#include<cmath>
#include<cstring>
#include<string>
#include<algorithm>

using namespace std;

const int N = 100;
int r, c;
char a[N][N];

void print(char a[N][N])
{
    for (int i = 0; i < r; i++)
    {
        for (int j = 0; j < c; j++)
            if (i == 0 && j == 0)
                cout << "c";
            else
                cout << a[i][j];
        cout << endl;
    }
}

bool go(int r, int c, int m)
{
    int ind = r*c - m;
    for (int i = 0; i < r; i++)
        for (int j = 0; j < c; j++)
          a[i][j] = '*';
    if (ind == 1)
    {
        a[0][0] = '.';
        print(a);
        return true;
    }
    if (ind % 2 == 1 && (r == 2 || c == 2))
        return false;

    if (r == 1)
    {
        for (int i = 0; (i < c && ind > 0); i++, ind--)
        {
            a[0][i] = '.';
        }
        print(a);
        return true;
    }
    if (c == 1)
    {
        for (int i = 0; (i < r && ind > 0); i++, ind--)
        {
            a[i][0] = '.';
        }
        print(a);
        return true;
    }

    if (ind == 4)
    {
        for (int i = 0; i < 2; i++)
            for (int j = 0; j < 2; j++)
                a[i][j] = '.';
        print(a);
        return true;
    }
    if (ind < 4)
        return false;
    if (ind == 5 || ind == 7)
        return false;
    for (int i = 0; i < 2; i++)
            for (int j = 0; j < 2; j++)
                a[i][j] = '.';
    ind -= 4;
    int last = 2;
    for (; (ind >= 2 && last < c);)
    {
      a[0][last] = '.';
      a[1][last] = '.';
    //  cout << "last = " << last << endl;
      last++;
      ind -= 2;
    //  cout << "ind =  " << ind << endl;
    }
    if (ind == 0)
    {
        print(a);
        return true;
    }
    if (ind == 1)
    {
        last--;
        a[0][last] = '*';
        a[1][last] = '*';
        a[2][0] = '.';
        a[2][1] = '.';
        a[2][2] = '.';
        print(a);
        return true;
    }
    last = 2;
   // cout << "ind =  " << ind << endl;
    for (; (ind >= 2 && last < r);)
    {
        a[last][0] = '.';
        a[last][1] = '.';
        last++;
     //   cout << "last = " << last << endl;
        ind -= 2;
      //  cout << "ind = " << ind << endl;
    }
    if (ind == 1)
    {
        a[2][2] = '.';
        print(a);
        return true;
    }
    if (ind == 0)
    {
        print(a);
        return true;
    }
    for (int i = 2; (i < r && ind > 0); i++)
        for (int j = 2; (j < c && ind > 0); j++)
        {
            a[i][j] = '.';
            ind--;
        }
    print(a);
    return true;
}

int main()
{
    freopen("a.in", "r", stdin);
    freopen("a.out","w", stdout);

    int t;
    cin >> t;
    int m;
    for (int i = 0; i < t; i++)
    {
        cout << "Case #" << i + 1 << ":" << endl;
        cin >> r >> c >> m;
        if (!go(r, c, m))
            cout << "Impossible" << endl;
    }

    return 0;
}
