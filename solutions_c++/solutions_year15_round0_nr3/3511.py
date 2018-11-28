#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

const int QUAT_1 = 1;
const int QUAT_I = 2;
const int QUAT_J = 3;
const int QUAT_K = 4;

int quat_mul(int a, int b)
{
    int s = (a * b) < 0 ? -1 : 1;
    int r = QUAT_1;
    a = abs(a);
    b = abs(b);
    switch (a)
    {
    case QUAT_1: return s * b;
    case QUAT_I:
        switch (b)
        {
        case QUAT_1: return s * a;
        case QUAT_I: return s * -QUAT_1;
        case QUAT_J: return s * QUAT_K;
        default:     return s * -QUAT_J;
        }
        break;
    case QUAT_J:
        switch(b)
        {
        case QUAT_1: return s * a;
        case QUAT_I: return s * -QUAT_K;
        case QUAT_J: return s * -QUAT_1;
        default:     return s * QUAT_I;
        }
        break;
    default:
        switch(b)
        {
        case QUAT_1: return s * a;
        case QUAT_I: return s * QUAT_J;
        case QUAT_J: return s * -QUAT_I;
        default:     return s * -QUAT_1;
        }
    }
}

int quat_next(int q)
{
    switch (q)
    {
    case QUAT_I:
        return QUAT_J;
    case QUAT_J:
        return QUAT_K;
    default:
        return QUAT_K;
    }
}

typedef vector<int> vi;
typedef vector<bool> vb;

bool is_dijkstra_recursive(const vi &t, int i, int target, vb &M)
{
    int p = i * 3 + (target - 2);
    if (!M[p])
    {
        return false;
    }

    int a = QUAT_1;
    for (int N = (int) t.size(); i < N; ++i)
    {
        a = quat_mul(a, t[i]);
        if (a == target)
        {
            if (target == QUAT_K)
            {
                if (i == N - 1)
                {
                    return true;
                }
            }
            else if (is_dijkstra_recursive(t, i + 1, quat_next(target), M))
            {
                return true;
            }
        }
    }

    M[p] = false;
    return false;
}

bool is_dijkstra(const vi &t)
{
    vb M((t.size() + 1) * 3, true);
    return is_dijkstra_recursive(t, 0, QUAT_I, M);
}

int main()
{
    int T; cin >> T;
    for (int i = 0; i < T; ++i)
    {
        int L, X; cin >> L >> X;
        string s; cin >> s;

        int ci = 0, cj = 0, ck = 0;
        for (char c : s)
        {
            if (c == 'i')
            {
                ci = 1;
            }
            else if (c == 'j')
            {
                cj = 1;
            }
            else
            {
                ck = 1;
            }
        }

        cout << "Case #" << i + 1 << ": ";
        if (ci + cj + ck > 1)
        {
            vi inp;
            for (int j = 0; j < X; ++j)
            {
                for (char c : s)
                {
                    inp.push_back(c - 'i' + 2);
                }
            }

            if (is_dijkstra(inp))
            {
                cout << "YES";
            }
            else
            {
                cout << "NO";
            }
        }
        else
        {
            cout << "NO";
        }

        cout << "\n";
    }

    return 0;
}
