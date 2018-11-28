#include <iostream>
#include <fstream>
#include <set>
using namespace std;

#define MAX 1000000

int main() {

    int numCase = 0;
    long num = 0;
    long tempNum = 0;
    set<int> myset;

    ifstream fin("A-large.in");
    ofstream fout("A-large.out");

    if (!fin.is_open()) cout << "input.in was not open successfully" << endl;
    if (!fout.is_open()) cout << "output.out was not open successfully" << endl;

    fin >> numCase;

    for (int j = 0; j < numCase; j++)
    {
        for (int i=0; i<10; i++) myset.insert(i);

        fin >> num;
        tempNum = num;
        if(num <= 0)
        {
            fout << "Case #" << (j + 1) << ": INSOMNIA" << endl;
        }
        else
        {
            for(int i = 2; i <= MAX; i++ )
            {
                while (tempNum != 0 && !myset.empty())
                {
                    int last = tempNum % 10;
                    myset.erase(last);
                    tempNum = (tempNum - last) / 10;
                }
                if (!myset.empty())
                    tempNum = num *i;
                else
                {
                    fout << "Case #" << (j + 1) << ": " << num *(i-1) << endl;
                    break;
                }
            }

        }
    }

    fin.close();
    fout.close();
    return 0;
}
