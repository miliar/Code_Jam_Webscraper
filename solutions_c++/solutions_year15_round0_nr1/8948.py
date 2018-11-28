#include <fstream>
#include <iostream>
#include <sstream>
#include <cassert>

using namespace std;

int count_friends(int shyness, const string& audience) {
    int invite = 0;
    int total = 0;
    for (int level = 0; level <= shyness; level++) {
        int needed = audience[level] - '0';
        if (level > total) {
            invite += level - total;
            total = level;
        }
        total += needed;
    }
    return invite;
}

int main()
{
    ifstream input("A-large.in");
    ofstream output("output.txt");

    int cases = 0;
    input >> cases;

    int test = 1;
    int shyness;
    string audience;
    while (test <= cases) {
        input >> shyness >> audience;
        int count = count_friends(shyness, audience);
        output << "Case #" << test << ": " << count << endl;
        test++;
    }

    return 0;
}

