#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int T;

int main()
{
    ifstream in("in.txt");
    ofstream out("out.txt");
    in >> T;

    for (int t = 0; t < T; ++t)
    {
        int N;
        in >> N;

        vector<int> cnt(2501, 0);
        vector<int> res;

        for (int i = 0; i < 2 * N - 1; ++i)
        {
            for (int j = 0; j < N; ++j)
            {
                int sol;
                in >> sol;
                cnt[sol]++;
            }
        }

        for (int i = 1; i < cnt.size(); ++i)
        {
            if (cnt[i] != 0 && cnt[i] % 2 == 1)
                res.push_back(i);
        }

        out << "Case #" << t + 1 << ": ";

        for (int i = 0; i < res.size(); ++i) out << res[i] << " ";
        out << endl;
    }

    in.close();
    out.close();

    return 0;
}