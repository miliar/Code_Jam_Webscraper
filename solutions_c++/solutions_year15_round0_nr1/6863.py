#include <cstdlib>  // std::atoi
#include <iostream> // std::cout
#include <fstream>
#include <stdlib.h>
#include <string>
#include <vector>
using namespace std;

const string inputfile = "A-large.in";
const string outputfile = "A-large.out";

int solve(int max_shy, vector<int> &crowd)
{
    if (max_shy == 0)
        return 0;

    int friends = 0;
    int cheering = crowd.at(0);

    for (int cheer_level = 1; cheer_level < max_shy + 1; cheer_level++) {
        // Find amount of friends needed
        int needed = cheer_level - (cheering + friends);

        // Add to friends
        if (needed > 0)
            friends += needed;

        // Add the people that are now cheering
        cheering += crowd.at(cheer_level);

        // Check if there is enough cheering
        if (cheering >= max_shy)
            return friends;
    }

    return friends;
}

int main()
{
    ifstream input;
    ofstream output;

    input.open(inputfile, ifstream::in);

    if (!input.is_open())
    {
        cerr << "file not found!\n";
        return -1;
    }

    output.open(outputfile, ofstream::trunc);

    int cases;

    input >> cases;
    cout << "total cases: " << cases << endl;

    for (int i = 0; i < cases; i++)
    {
        int max_shy;
        char temp;

        // Maximum shyness
        input >> max_shy;
        cout << max_shy << " ";
        input.get(temp); // ignore space after

        // Create the crowd
        vector<int> crowd(max_shy + 1);

        // Insert shyness of all into a vector
        for (int i = 0; i < max_shy + 1; i++)
        {
            input.get(temp);
            cout << temp;
            crowd.insert(crowd.begin() + i, temp - '0');
        }
        input.get(temp); // ignore newline after
        cout << endl;

        // Output solutions to file
        int solution = solve(max_shy, crowd);
        output << "Case #" << i + 1 << ": " << solution << endl;
        cout   << "Case #" << i + 1 << ": " << solution << endl;
    }

    input.close();
    output.close();
}

