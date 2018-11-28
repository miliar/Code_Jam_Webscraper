#include <fstream>
#include <vector>
using namespace std;

ofstream fileout("output.txt");

void find_answer(unsigned long long number, int t)
{
    if (number == 0)
    {
        fileout << "Case #" << t << ": INSOMNIA\n";
        return;
    }
    vector<int> digits(10);
    int k = 1;
    while ((digits[0] == 0) || (digits[1] == 0) || (digits[2] == 0) || (digits[3] == 0) || (digits[4] == 0) || (digits[5] == 0) || 
           (digits[6] == 0) || (digits[7] == 0) || (digits[8] == 0) || (digits[9] == 0))
    {
        int j = 10;
        unsigned long long smth = number * k;
        do
        {
            digits[smth % j] = 1;
            smth /= j;
        } while (smth != 0);
        k++;
    }

    fileout << "Case #" << t << ": " << number * (k - 1) << "\n";
}

int main()
{
    ifstream filein("input.txt");
    int T;
    unsigned long long N;
    filein >> T;
    for (int i = 1; i <= T; i++)
    {
        filein >> N;
        find_answer(N, i);
    }
    filein.close();
    fileout.close();
    return(0);
}