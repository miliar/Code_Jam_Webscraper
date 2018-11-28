#include <fstream>

using namespace std;

int main()
{
    ifstream f("input.in");
    ofstream g("output.out");
    int T, i, j;
    string S, result;
    f >> T;
    for (i = 1; i <= T; i++)
    {
        f >> S;
        result = S[0];
        for (j = 1; j < S.size(); j++)
            if (S[j] >= result[0])
                result = S[j] + result;
            else
                result = result + S[j];

        g << "Case #" << i << ": " << result << '\n';

    }
    f.close();
    g.close();
    return 0;
}
