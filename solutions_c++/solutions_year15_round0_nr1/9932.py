#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>

using namespace std;

int main()
{
    ifstream input("A-small-attempt2.in");
    //ifstream input("input.in");
    ofstream output("output.out");

    string str = "";
    getline(input, str);

    int cases = atoi(str.c_str());
    for (int c = 0; c < cases; ++c)
    {
        getline(input, str);

        int space = str.find(" ");
        int shy_max = atoi(str.substr(0, space).c_str());
        string pattern = str.substr(space + 1);

        int total_people = 0;
        int friend_count = 0;
        for (int i = 0; i < shy_max + 1; ++i)
        {
            //cout << "T: " << total_people << endl;
            while (total_people < i)
            {
                total_people++;
                friend_count++;
            }
            total_people += pattern[i] - '0';
        }
        cout << endl;
        output << "Case #" << c + 1 << ": " << friend_count << endl;
    }
    output.close();
    input.close();
    return 0;
}