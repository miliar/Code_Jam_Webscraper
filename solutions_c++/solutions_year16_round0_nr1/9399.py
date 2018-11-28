#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main()
{
    std::ofstream outfile;
    outfile.open("output.txt", std::ofstream::out);

    int T;

    int* N = new int[T];
    std::ifstream ifs("input.txt", std::ifstream::in);

    ifs >> T;
    for (int i = 0; i < T; ++i)
    {
        ifs >> N[i];
    }

    if (outfile.good())
    {


        for (int i = 0; i < T; ++i)
        {
            int j = 1;
            string str = "ffffffffff";
            while (true) {

                if (N[i] == 0)
                {
                    outfile << "Case #" << i + 1 << ": INSOMNIA" << endl;
                    break;
                }
                string s = to_string(j * N[i]);

                for (int k = 0; k < s.length(); ++k)
                {
                    str[s[k] - '0'] = 't';
                }

                if (str == "tttttttttt")
                {
                    outfile << "Case #" << i + 1 << ": " << s << endl;
                    break;
                }
                ++j;
            }
        }
    }
    outfile.close();
    return 0;
}
