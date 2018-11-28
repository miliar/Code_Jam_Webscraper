
#include <iostream>
#include <fstream>
#include <vector>
#include <string>

int main(int argc, char** argv)
{
    using namespace std;

    string fileNameIn(argv[1]);

    string fileNameOut = fileNameIn.substr(0, fileNameIn.find('.')) + ".out";

    ifstream in(fileNameIn.c_str());
    ofstream out(fileNameOut.c_str());

    int N = 0;
    in >> N; //Number of test cases
    for (int i = 0; i < N; ++i) 
    {
        //now just "in >> bla" as many times as you need to
        //do your calculation on the test case
        int s_max = 0;
        std::string digits;
        in >> s_max >> digits;

        int standing = 0;
        int fake = 0;
        for (int index = 0; index <= s_max; ++index) {
            char d = digits[index];
            int cur_count = static_cast<int>(d - '0');

            if (cur_count > 0) {
                if (standing < index) {
                    fake += index - standing;
                    standing = index;
                }
                standing += cur_count;
            }
        }

        out << "Case #" << i+1 << ": " << fake << endl;

    }
}
