#include <iostream>
#include <string>
#include <fstream>
#include <set>

using namespace std;

typedef long long ll;

int main()
{
    ifstream fin("in.in");
    ofstream fout("out.out");

    int times;
    fin >> times;
    for (int i = 0; i < times; i++)
    {
        ll m, n;
        fin >> n;
        m = n;

        //go until filled with digits
        set<char> digits = { '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' };
        while (true)
        {
            if (n == 0)
            {
                fout << "Case #" << i + 1 << ": INSOMNIA" << endl;
                break;
            }

            string str = to_string(n);

            for (int i = 0; i < str.length(); i++)
                digits.erase(str.at(i));
            
            if (digits.empty())
            {
                fout << "Case #" << i + 1 << ": " << n << endl;
                break;
            }

            n += m;
        }
    }

    cin.get();

    fout.close();
    fin.close();
}