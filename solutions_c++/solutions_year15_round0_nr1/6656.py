#include <iostream>
using std::cin;
using std::cout;
using std::endl;

#include <fstream>
using std::ifstream;

#include <cassert>

int main(int argc, char* argv[])
{
    // Open file
    char* filename;
    filename = argv[1];
    ifstream fs(filename);
    assert(fs.is_open());

    // Get number of cases
    int N_cases;
    fs >> N_cases;

    // Ignore trailing whitespace
    fs.ignore();

    // For every case...
    for (int i = 0; i < N_cases; ++i)
    {
        // Define and retrieve maximum shyness
        int S_max;
        fs >> S_max;

        // Define and retrieve audience string
        char S_audience[S_max + 1];
        fs >> S_audience;

        // Declare variables and run simulation
        int num_standing = 0;
        int num_invited = 0;
        for (int shyness = 0; shyness <= S_max; ++shyness)
        {
            // Number of people who have the level of shyness
            int num_shy = static_cast<int>(S_audience[shyness]) - '0';

            // If the number people currently standing just aren't enough
            // for these introverts to feel safe
            if (num_standing < shyness && num_shy != 0)
            {
                // Invite the difference
                num_invited += shyness - num_standing;
                num_standing += num_invited;
            }
            num_standing += num_shy;
        }

        // Print case number
        cout << "Case #" << i + 1 << ": ";
        cout << num_invited << endl;
    }
}
