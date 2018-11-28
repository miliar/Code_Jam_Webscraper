#include <iostream>
#include <fstream>
#include <sstream>
#include <cmath>

using namespace std;

int check_palindrome(int n)
{
    ostringstream os;
    os << n;
    string digits = os.str();
    for (int i=0, j=digits.length()-1;i<digits.length()/2;++i, --j)
    {
        if (digits[i] != digits[j])
        {
            return 0;
        }
    }
    return 1;
}

int main()
{
    ifstream fin;
    fin.open("C-small-attempt0.in");
    if (!fin.is_open())
    {
        cout << "Error in Opening Input file ";
        return -1;
    }
    ofstream fout;
    fout.open("C-small-attempt0.out");

    int num_cases, a, b;
    fin >> num_cases;

    for (int i=0;i<num_cases;++i)
    {
        fout << "Case #" << i+1 << ": ";

        fin >> a >> b;

        int total = 0;
        int sq,  flag;
        for (int i=a; i<= b; ++i)
        {
            flag = check_palindrome(i);

            if (flag == 0)
                continue;
            else
            {
                sq = static_cast<int>(sqrt(i));
                if (sq*sq != i)
                    continue;
                else
                {
                    flag = check_palindrome(sq);
                    if (flag == 1)
                        total++;
                }
            }
        }

        fout << total;
        fout << endl;
    }
    return 0;
}
