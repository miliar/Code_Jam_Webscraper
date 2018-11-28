#include<iostream>
#include<fstream>
#include<set>
using namespace std;

int main()
{
    ifstream fin ("A-large.in");
    ofstream fout ("A-large0.out");
    set<int> digits;
    int t, number, holder, holder2 = 1;
    fin >> t;
    for (int i = 0; i < t; i++)
    {
        fin >> number;
        holder = number;
        if (number == 0) fout << "Case #" << i + 1 << ": INSOMNIA" << endl;
        else
        {
            number = 0;
            holder2 = 1;
            do
            {
                number = holder2 * holder;
                holder2++;
                do
                {
                    digits.insert(number % 10);
                    number /= 10;
                }
                while (number > 0);
            }
            while (digits.size() < 10);
            fout << "Case #" << i + 1 << ": " << holder2 * holder - holder << endl;
        }
        digits.clear();
    }
}
