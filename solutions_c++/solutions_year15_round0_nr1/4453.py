#include <fstream>

using namespace std;

int main()
{
    int T, Smax, i, j;
    string line;
    int totalStanding, friends;
    ifstream f("input.in");
    f >> T;
    ofstream g("output.out");
    for (i = 1; i <= T; i++)
    {
        f >> Smax >> line;
        totalStanding = friends = 0;
        for (j = 0; j < line.size(); j++)
        {
            if (line[j] != '0')
            {
                if (totalStanding < j)
                {
                    friends += j - totalStanding;
                    totalStanding += j - totalStanding + (line[j] - '0');
                }
                else
                    totalStanding += line[j] - '0';
            }
        }
        g << "Case #" << i << ": " << friends << '\n';
    }
    f.close();
    g.close();
    return 0;
}
