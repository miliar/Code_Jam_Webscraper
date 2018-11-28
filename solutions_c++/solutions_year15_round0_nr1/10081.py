#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char *argv[])
{
    ifstream fin(argv[1]);
    ofstream fout(argv[2]);

    int test_cases = 0;
    fin >> test_cases;

    for (int t = 1; t <= test_cases; ++t)
    {
        int s_max = 0;
        fin >> s_max;

        string in;
        fin >> in;
        
        int done = 0;
        int friends = 0;
        for (int s = 0; s != in.size(); ++s)
        {
            int num = in[s] - '0';    // in[s] - '0' = number of people with shyness level s
            if (num == 0)
                continue;
            if (done >= s)
                done += num;
            else
            {
                // Call friends
                friends += (s - done);
                done += friends + num;
            }
        }

        cout << "Case #" << t << ": " << friends << endl;
        fout << "Case #" << t << ": " << friends << endl;
    }

    return 0;
}
