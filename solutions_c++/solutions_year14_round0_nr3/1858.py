#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int DX[8] = {-1, -1, -1, 0, 0, 1, 1, 1};
int DY[8] = {-1, 0, 1, -1, 1, -1, 0, 1};


bool empty(vector<int> & A, int R, int C, int x, int y)
{
    return A[x * C + y] == 0;
}

int mines(vector<int> & A, int R, int C, int x, int y)
{
    int ans = 0;
    for (int i = 0; i < 8; ++i)
    {
        int x1 = x + DX[i];
        int y1 = y + DY[i];
        if (0 <= x1 && x1 < R && 0 <= y1 && y1 < C && A[x1 * C + y1] == 1)
            ans++;
    }
    return ans;
}

void DFS(vector<int> & A, int R, int C, int r, int c)
{
    A[r * C + c] = 2;
    for (int i = 0; i < 8; ++i)
    {
        int r1 = r + DX[i];
        int c1 = c + DY[i];
        if (0 <= r1 && r1 < R && 0 <= c1 && c1 < C)
        {
            if(mines(A, R, C, r1, c1) == 0 && A[r1 * C + c1] == 0)
                DFS(A, R, C, r1, c1);
            A[r1 * C + c1] = 2;
        }
    }
}

bool check(vector<int> A, int R, int C, int & ra, int & ca)
{
    for (int r = 0; r < R; r++)
        for(int c = 0; c < C; c++)
            if (empty(A, R, C, r, c) && mines(A, R, C, r, c) == 0)
            {
                DFS(A, R, C, r, c);
                for (int r1 = 0; r1 < R; r1++)
                    for(int c1 = 0; c1 < C; c1++)
                        if (A[r1 * C + c1] == 0)
                            return false;
                ra = r;
                ca = c;
                return true;
            }
}

void solve()
{
    int R, C, M, i, ra, ca;
    cin >> R >> C >> M;
    if (M == R * C - 1)
    {
        for(int r = 0; r < R; ++r)
        {
            for(int c = 0; c < C; ++c)
            {
                if (r == 0 && c == 0)
                    cout << "c";
                else
                    cout << "*";
            }
            cout << endl;
        }
        return;
    }
    vector<int> A(R * C, 0);
    for(i = R * C - M; i < R * C; ++i)
        A[i] = 1;
    vector<int> B = A;
    while (!check(B, R, C, ra, ca))
    {
        if(!next_permutation(A.begin(), A.end()))
        {
            cout << "Impossible" << endl;
            return;
        }
        B = A;
    }
    for(int r = 0; r < R; ++r)
    {
        for(int c = 0; c < C; ++c)
        {
            if (r == ra && c == ca)
                cout << "c";
            else if (B[r * C + c] == 1)
                cout << "*";
            else
                cout << ".";
        }
        cout << endl;
    }
}

int main()
{
    int T, num;
    cin >> T;
    for (num = 1; num <= T; ++num)
    {
        cout << "Case #" << num << ":" << endl;
        solve();
    }
}
