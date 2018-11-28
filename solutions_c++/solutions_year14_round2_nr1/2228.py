#include <fstream>
#include <string>
#include <iostream>

using namespace std;
const int Nmax = 105;

int A[Nmax][Nmax];
string S[Nmax];

string base(int row, string &str)
{
    string ret = "";
    int j = -1;
    for (auto x: str)
        if (ret.size() == 0 || ret.back() != x)
        {
            ret.push_back(x);
            ++j;
            A[row][j] = 1;
        }
        else
        {
            A[row][j]++;
        }
    return ret;
}

int main()
{

    ifstream f ("A.in");
    ofstream g ("A.out");

    int T, N;
    string str;
    f >> T;
    for (int t = 0; t < T; t++)
    {
        g << "Case #" << t+1 << ": ";
        f >> N;
        for (int i = 0; i < N; i++)
            f >> S[i];
        string model = base(0, S[0]);
        int L = model.size();
        bool ok = 1;
        for (int i = 1; i < N && ok; i++)
            if (model != base(i, S[i]))
                ok = 0;
        if (!ok)
        {
            g << "Fegla Won\n";
            continue;
        }
        int answer = 0;
        for (int l = 0; l < L; l++)
        {
            int best = 1000;
            int mn = 1000, mx = 0;
            for (int row = 0; row < N; row++)
            {
                if (A[row][l] > mx) mx = A[row][l];
                if (A[row][l] < mn) mn = A[row][l];
            }
            for (int target = mn; target <= mx; target++)
            {
                int sum = 0;
                for (int row = 0; row < N; row++)
                    sum += target > A[row][l] ? target - A[row][l] : A[row][l] - target;
                if (sum < best)
                    best = sum;
            }
            answer += best;
        }
        g << answer << '\n';
    }
    return 0;
}
