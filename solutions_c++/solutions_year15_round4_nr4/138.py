#include <iostream>
#include <string>

int a[6][6];
int cnt[6][6];
int r, c;

long long f(int i, int j)
{
    if (i == r)
    {
        int sum = 0;
        for (int i = 0 ; i < r ; ++i)
            for (int j = 0 ; j < c ; ++j)
                sum += cnt[i][j];
        if (sum == 0)
        {
            for (int i = 0 ; i < r ; ++i)
            {
                for (int j = 0 ; j < c ; ++j)
                {
                    std::cout << a[i][j];
                }
                std::cout << "\n";
            }
            std::cout << "\n";
        }
        return sum == 0 ? 1 : 0;
    }
    else if (j == c)
    {
        if (a[i][0] == a[i][c - 1])
        {
            --cnt[i][0];
            --cnt[i][c - 1];
            long long res = 0;
            if (cnt[i][0] >= 0 && cnt[i][c - 1] >= 0)
                res = f(i + 1, 0);
            ++cnt[i][0];
            ++cnt[i][c - 1];
            return res;
        }
        else
            return f(i + 1, 0);
    }
    else
    {
        long long res = 0;
        for (int t = 1 ; t <= 3 ; ++t)
        {
            cnt[i][j] = t;
            a[i][j] = t;
            bool up = false;
            bool ok = true;
            if (i > 0 && a[i][j] == a[i-1][j])
            {
                up = true;
                --cnt[i][j];
                --cnt[i-1][j];
                ok = cnt[i][j] >= 0 && cnt[i-1][j] >= 0;
            }
            bool left = false;
            if (j > 0 && a[i][j] == a[i][j-1])
            {
                left = true;
                --cnt[i][j];
                --cnt[i][j-1];
                ok = ok && cnt[i][j] >= 0 && cnt[i][j-1] >= 0;
            }
            if (ok)
                res += f(i, j + 1);
            if (up)
                ++cnt[i-1][j];
            if (left)
                ++cnt[i][j-1];
        }
        return res;
    }
}

int main()
{
    int T;
    std::cin >> T;
    for (int t = 1 ; t <= T ; ++t)
    {
        std::cin >> r >> c;
        /*for (int i = 0 ; i < r ; ++i)
            for (int j = 0 ; j < c ; ++j)
                cnt[i][j] = a[i][j] = 0;
        long long res = f(0, 0);*/
        long long res = 0;
        switch (r)
        {
        case 2:
            // 3
            res = 1;
            // sq
            if (c % 3 == 0)
                ++res;
            // m2
            if (c % 6 == 0)
                ++res;
            break;
        case 3:
            // 2/3  3/2
            res = 2;
            // m1
            if (c % 4 == 0)
                ++res;
            break;
        case 4:
            // 2/3/2
            res = 1;
            // sq/3 3/sq
            if (c % 3 == 0)
                res += 2;
            // m2/3 3/m2
            if (c % 6 == 0)
                res += 2;
            break;
        case 5:
            // 3/2/3
            res = 1;
            // sq/3/2 2/3/sq
            if (c % 3 == 0)
                res += 2;
            // m1/3 3/m1
            if (c % 4 == 0)
                res += 2;
            // m2/3/2 2/3/m2
            if (c % 6 == 0)
                res += 2;
            break;
        case 6:
            // 2/3/2/3 3/2/3/2
            res = 2;
            // sq/3/sq 3/sq/3
            if (c % 3 == 0)
                res += 1 + 3;
            // m1/3/2 2/3/m1
            if (c % 4 == 0)
                res += 2;
            // m2/3/m2 3/m2/3 sq/3/m2 m2/3/sq
            if (c % 6 == 0)
                res += 1 + 6 + 3 + 3;
            break;
        }
        std::cout << "Case #" << t << ": ";
        std::cout << res;
        std::cout << "\n";
    }
    return 0;
}

