#include <iterator>
#include <fstream>
#include <iostream>
#include <set>

using namespace std;

int main()
{
    ifstream in("A-small-attempt0.in");

    int tests;
    in >> tests;

    for (int test = 0; test != tests; ++test)
    {
        set <int> first, second;
        int answer, curr;
        
        in >> answer;

        for (int i = 0; i != 4; ++i)
            for (int j = 0; j != 4; ++j)
            {
                in >> curr;
                if (i + 1 == answer)
                    first.insert(curr);
            }

        in >> answer;
        for (int i = 0; i != 4; ++i)
            for (int j = 0; j != 4; ++j)
            {
                in >> curr;
                if ((i + 1 == answer) && (first.find(curr) != first.end()))
                    second.insert(curr);
            }

        cout << "Case #" << test + 1 << ": ";

        if (second.empty())
            cout << "Volunteer cheated!\n";
        else if (second.size() != 1)
            cout << "Bad magician!\n";
        else
            cout << *second.begin() << "\n";
    }

    in.close();

    return 0;
}