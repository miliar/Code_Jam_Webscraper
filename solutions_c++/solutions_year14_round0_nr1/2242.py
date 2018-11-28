#include <iostream>
#include <cstdlib>
#include <sstream>
#include <string>
#include <map>

using namespace std;

int main()
{
    int T;
    string input;
    getline(cin, input);
    T = atoi(input.c_str());
    
    for (int i = 0; i < T; i++)
    {
        // Get row the number is in and grab the numbers
        int row;
        getline(cin, input);
        row = atoi(input.c_str());

        stringstream ss;
        for (int j = 1; j <= 4; j++)
        {
            getline(cin, input);
            if (j == row)
            {
                ss << input;
            }
        }
        map<int, int> num_map;
        int num;
        
        for (int j = 0; j < 4; j++)
        {
            ss >> num;
            num_map[num]++;
        }
        ss.str("");
        ss.clear();

        // Grab the numbers a second time
        getline(cin, input);
        row = atoi(input.c_str());

        for (int j = 1; j <= 4; j++)
        {
            getline(cin, input);
            if (j == row)
            {
                ss << input;
            }
        }
        
        int answer = 0;
        int possible_nums = 0;
        for (int j = 0; j < 4; j++)
        {
            ss >> num;
            num_map[num]++;
            if (num_map[num] == 2)
            {
                possible_nums++;
                answer = num;
            }
        }

        // Print case #:
        cout << "Case #" << i + 1 << ": ";

        // Process answers
        if (possible_nums == 1)
        {
            cout << answer;
        }
        else if (possible_nums > 1)
        {
            cout << "Bad magician!";
        }
        else
        {
            cout << "Volunteer cheated!";
        }
        cout << endl;
    }
    
    return 0;
}