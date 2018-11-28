#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(int argc, char *argv[])
{
    string param = argv[1];

    // Parse input file
    ifstream pfile(param);

    string line;
    getline(pfile, line);
    //cout << line << endl;

    // first line number of test cases only
    int num_cases = stoi(line);

    for (int t=0; t<num_cases; ++t)
    {
        getline(pfile, line);

        // split
        size_t split_pos = line.find(' ');

        string smax_s = line.substr(0, split_pos);
        string people_s = line.substr(split_pos+1, line.size());

        //cout << "smax:" << smax_s << ", people:" << people_s << endl;

        int smax = stoi(smax_s);

        int standing(0);
        int extras(0);

        for (int k=0; k<smax+1; ++k)
        {
            string people_at_shyness_s = people_s.substr(k, 1);
            int people_at_shyness = stoi(people_at_shyness_s);

            //cout << "Test case:" << t << ", people at shyness " << k << " = " << people_at_shyness << endl;

            if (people_at_shyness == 0)
            {
                // Nothing to do
            }
            else
            {
                // At least one person at this shyness level, so need to
                // have at least this many already
                if (standing < k)
                {
                    extras += (k-standing);
                    standing += (k-standing);
                }

                standing += people_at_shyness;
            }

            //cout << "standing: " << standing << ", and extras needed so far: " << extras << endl;
        }
        cout << "Case #" << t+1 << ": " << extras << endl;
    }

    return 0;
}