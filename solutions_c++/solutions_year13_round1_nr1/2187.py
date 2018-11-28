#include <fstream>
using namespace std;

int solve(long long r, long long t)
{
    int ans = 0;
    long long s = 2 * r + 1;
    do
    {
        ans++;
        r += 2;
        t -= s;
        s = 2 * r + 1;
    }
    while (t >= s);

    return ans;
}

int main()
{
    ifstream fin("A-small-attempt0.in");
    ofstream fout("output.txt");

    int n;
    long long r, t;
    fin >> n;
    for (int i = 0; i < n; i++)
    {
        fin >> r >> t;
        fout << "Case #" << i + 1 << ": " << solve(r, t) << endl;
    }

    fin.close();
    fout.close();
    return 0;
}

