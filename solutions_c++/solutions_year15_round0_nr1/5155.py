#include <iostream>
//using std::cin;
//using std::cout;
//using std::endl;
#include <string>
//using std::string;
#include <fstream>
//using std::ifstream;
#include <cassert>

using namespace std;

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
    for (int i = 1; i <= N_cases; ++i)
    {
        // get maximum shyness level & # of people with each level
        int max_shyness;
        string audience;
        fs >> max_shyness >> audience;
        //cout << "max_shyness: " << max_shyness << endl;

        // put audience #s into array
        int aud_arr[max_shyness + 1];
        for (int j = 0; j <= max_shyness; ++j)
        {
            aud_arr[j] = static_cast<int>(audience.at(j)) - '0';
            //cout << "aud_arr[" << j << "]: " << aud_arr[j] << endl;
        }
        //cout << "aud_arr size: " << sizeof(aud_arr)/sizeof(*aud_arr) << endl;
        assert(sizeof(aud_arr)/sizeof(*aud_arr) == (max_shyness + 1));

        // check how many more people need to be invited
        int num_aud = 0;
        int num_add = 0;
        for (int j = 0; j < max_shyness; ++j)
        {
            num_aud += aud_arr[j];
            /*if (j < max_shyness)
            {
                // if there are not enough people to make S_(i+1) stand up
                // and there is at least one person of S_(i+1)
                while (num_aud < (j+1) && aud_arr[j+1] > 0)
                {
                    //cout << "another loop entered" << endl;
                    //cout << "num_add: " << num_add << endl;
                    ++num_add;
                    ++num_aud;
                }
            }*/
            // if there are not enough people to make S_(i+1) stand up
            // and there is at least one person of S_(i+1)
            while (num_aud < (j+1) && aud_arr[j+1] > 0)
            {
                //cout << "another loop entered" << endl;
                //cout << "num_add: " << num_add << endl;
                ++num_add;
                ++num_aud;
            }
            //cout << "num_add: " << num_add << endl;
        }
        //cout << "num_aud: " << num_aud << endl;
        // Print case number & result
        cout << "Case #" << i << ": ";
        cout << num_add << endl;
    }
}
