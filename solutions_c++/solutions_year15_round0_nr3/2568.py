#include <iostream>
#include <string>
#include <vector>
#include <cstdio>

using namespace std;

enum Q
{
    ONE,
    I,
    J,
    K,
    _ONE,
    _I,
    _J,
    _K,
};

Q multTable[4][4] =
{
    {ONE, I, J, K},
    {J, _ONE, K, _J},
    {J, _K, _ONE, I},
    {K, J, _I, _ONE}
};

Q Minus(Q x)
{
    if (x <= K)
        return (Q)((int)x + 4);
    return (Q)((int)x - 4);
}

Q mult(Q a, Q b)
{
    int sign = 1;
    if (a > K)
    {
        sign *= -1;
        a = Minus(a);
    }
    if (b > K)
    {
        sign *= -1;
        b = Minus(b);
    }
    Q c = multTable[a][b];
    if (sign == -1)
        return Minus(c);
    return c;
}

Q divTable[8][8];

Q div(Q a, Q b)
{
    return divTable[a][b];
}

int main()
{
    for (Q i = ONE; i <= _K; i = (Q)((int)(i) + 1))
    {
        for (Q j = ONE; j <= _K; j = (Q)((int)(j) + 1))
        {
            for (Q k = ONE; k <= _K; k = (Q)((int)(k) + 1))
            {
                if (mult(j, k) == i)
                {
                    divTable[i][j] = k;
                }
            }
        }
    }
//     for (int i = 0; i < 8; ++i)
//     {
//         for (int j = 0; j < 8; ++j)
//             printf("%d ", divTable[i][j]);
//         printf("\n");
//     }
    int T;
    cin >> T;
    for (int z = 1; z <= T; ++z)
    {
        cout << "Case #" << z << ": ";
        int L, X;
        cin >> L >> X;
        string s;
        cin >> s;
        string t;
        for (int i = 0; i < X; ++i)
        {
            t += s;
        }
        
        vector <Q> prefix(L * X + 1, ONE);
        s = t;
        for (int i = 1; i <= L * X; ++i)
        {
            if (s[i - 1] == 'i')
                prefix[i] = mult(prefix[i - 1], I);
            else if (s[i - 1] == 'j')
                prefix[i] = mult(prefix[i - 1], J);
            else if (s[i - 1] == 'k')
                prefix[i] = mult(prefix[i - 1], K);
        }
        int firstI = -1;
        int lastK = L * X + 1;
        for (int i = 0; i <= L * X; ++i)
        {
            if (prefix[i] == I)
            {
                firstI = i;
                break;
            }
        }
        for (int i = L * X; i >= 0; --i)
        {
            if (div(prefix[L * X], prefix[i]) == K)
            {
                lastK = i;
                break;
            }
        }
        /*for (int i = 0; i <= L * X; ++i)
            cout << prefix[i] << " ";
        cout << "\n";
        */
        if (firstI != -1 && lastK != L * X + 1 && firstI <= lastK && div(prefix[lastK], prefix[firstI]) == J)
        {
            cout << "YES\n";
          //  cout << firstI << " " << lastK << "\n";
        }
        else
        {
            cout << "NO\n";
           // cout << firstI << " " << lastK << "\n";
        }
    }
    
}