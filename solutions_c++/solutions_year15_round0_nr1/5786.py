#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main(int argc, char const *argv[])
{
    int tests, num_case = 0;
    ifstream input ("A-large.in");
    input >> tests;
    while (tests--)
    {
        int max, standing = 0, total_audience = 0, friends = 0, tmp = 0;
        string audience;
        input >> max >> audience;
        standing = audience[0] - '0';
        for (int i = 0; i <= max; i++)
            total_audience += audience[i] - '0';

        for (int i = 1; i <= max; i++)
        {
            if ( i > standing && audience[i] > 0 )
            {
                // cout << "i - standing " << i - standing << endl;
                tmp = i - standing;
                friends += tmp;
                standing += tmp;
            }
            standing += audience[i] - '0';
            // cout << "i " << i << " standing " << standing << " friends " << friends << " audience " << audience[i] << endl;
        }
        
        cout << "Case #" << ++num_case << ": " << friends << endl;
    }
    input.close();
    return 0;
}