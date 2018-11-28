#include <fstream>
#include <sstream>
#include <vector>

using namespace std;

int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    int tests;
    fin >> tests;
    int numbers[17];
    for (int t = 1; t <= tests; t++)
    {
        memset(numbers, 0, sizeof(numbers));
        int r1, r2;
        fin >> r1;
        for (int i = 0; i < 16; i++)
        {
            int tmp;
            fin >> tmp;
            if (i / 4 + 1 == r1)
            {
                numbers[tmp]++;
            }
        }
        fin >> r2;
        for (int i = 0; i < 16; i++)
        {
            int tmp;
            fin >> tmp;
            if (i / 4 + 1 == r2)
            {
                numbers[tmp]++;
            }
        }
        int k = 0;
        int answer = 0;
        for (int i = 1; i <= 16; i++)
        {
            if (numbers[i] == 2)
            {
                k++;
                answer = i;
            }
        }
        stringstream ss;
        ss << answer;
        string answer_string;
        ss >> answer_string;
        fout << "Case #" << t << ": " << ((k == 1) ? answer_string : (k > 1) ? "Bad magician!" : "Volunteer cheated!") << endl;
    }
    fin.close();
    fout.close();
    return 0;
}