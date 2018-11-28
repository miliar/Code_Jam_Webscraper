#include <iostream>
#include <fstream>
#include <list>
#include <vector>
#include <map>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

int main()
{
    ifstream in("small-practice.in");
    //ifstream in("large-practice.in");
    ofstream out("output.out");

    int T;
    in >> T;

    for( int t = 1; t <= T; t++ )
    {
        out << "Case #" << t << ": ";

        std::map<char,int> amount;
        string str;
        in >> str;
        for ( int i = 0 ; i < str.length(); i++)
        {
            amount[str.at(i)]++;
        }

        int digits[10] = {0};
        digits[0] = amount['Z'];
        digits[2] = amount['W'];
        digits[4] = amount['U'];
        digits[6] = amount['X'];
        digits[8] = amount['G'];

        amount['T'] -= amount['W'] + amount['G'];
        amount['F'] -= amount['U'];
        amount['S'] -= amount['X'];
        amount['I'] -= amount['X'] + amount['G'] + amount['F'];
        amount['O'] -= amount['Z'] + amount['W'] + amount['U'];

        digits[1] = amount['O'];
        digits[3] = amount['T'];
        digits[5] = amount['F'];
        digits[7] = amount['S'];
        digits[9] = amount['I'];

        for(int i = 0; i<10; i++)
        {
            for(int j = 1; j <= digits[i]; j++ )
            {
                out << i;
            }
        }

        out << endl;
    }

    return 0;
}
