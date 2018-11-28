#include <iostream>
#include <string>
#include <cmath>
#include <algorithm>
#include <map>
#include <fstream>
#include <vector>

using namespace std;

ifstream in;
ofstream out;

void Solve(vector <vector<int> > A, int Num, int maxn, int minn, int N, int M)
{
    for (int i = 0; i < N; ++i)
    {
        for (int j = 0; j < M; ++j)
        {
            bool q = 0;
            for (int k = 0; k < M; ++k)
            {
                if (A[i][k] > A[i][j])
                {
                    q = 1;
                }
            }
            if (q == 1)
            {
                q = 0;
                for (int k = 0; k < N; ++k)
                {
                    if (A[k][j] > A[i][j])
                    {
                        q = 1;
                    }
                }
            }
            if (q == 1)
            {
                out << "Case #" << Num << ": NO" << endl;
                return;
            }
        }
    }
    out << "Case #" << Num << ": YES" << endl;
    return;
}

int main()
{
    in.open("input.in");
    out.open("output.txt");
    long long T;
    int N, M, a, maxn = 0, minn = 100;
    char c;
    in >> T;
    for (long long i = 0; i < T; ++i)
    {
        in >> N >> M;
        vector <vector<int> > A(N);
        for (int j = 0; j < N; ++j)
        {
            for (int k = 0; k < M; ++k)
            {
                in >> a;
                minn = min(minn, a);
                maxn = max(maxn, a);
                A[j].push_back(a);
            }
        }
        Solve(A, i + 1, maxn, minn, N, M);
    }
    return 0;
}
