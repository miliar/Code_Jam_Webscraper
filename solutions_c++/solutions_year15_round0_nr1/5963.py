#include <fstream>
#include <string>

using namespace std;

int main()
{
    ifstream fin("in.txt");
    ofstream fout("out.txt");

    int t;
    fin >> t;
    for (int i = 0; i < t; i++)
    {
        int Smax;
        string str;
        fin >> Smax >> str;

        int max_diff = 0, sum = (str[0] - '0');
        for (int j = 1; j < str.length(); j++)
        {
            max_diff = max(max_diff, j - sum);
            sum += (str[j] - '0');
        }

        fout << "Case #" << (i + 1) << ": " << max_diff << endl;
    }
    return 0;
}
