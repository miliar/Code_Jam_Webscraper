#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <sstream>
#include <string>
#include <map>

using namespace std;

void magic_trick();
void cookie_clicker_alpha();

int main()
{
    //magic_trick();
    cookie_clicker_alpha();

    return 0;
}

void magic_trick()
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
}

void cookie_clicker_alpha()
{
    int T;
    cin >> T;
    cout << fixed << setprecision(7);
    
    for (int i = 1; i <= T; i++)
    {
        double C, F, X;
        cin >> C >> F >> X;

        double cur_time = X / 2.0;
        int n = 1;
        double farm_time = C / (2.0 + ((n - 1) * F));
        double total_farm_time = farm_time + X / (2.0 + (n * F));
        while (cur_time > total_farm_time)
        {
            cur_time = total_farm_time;
            n++;
            farm_time += C / (2.0 + ((n - 1) * F));
            total_farm_time = farm_time + X / (2.0 + (n * F));
        }
        cout << "Case #" << i << ": " << cur_time << endl;
    }
}