#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <algorithm>

#include <sstream>
#include <string>
#include <map>
#include <vector>
#include <list>

using namespace std;

void magic_trick();
void cookie_clicker_alpha();
void deceitful_war();

int main()
{
    //magic_trick();
    //cookie_clicker_alpha();
    deceitful_war();

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

void deceitful_war()
{
    int T;
    cin >> T;

    for (int i = 1; i <= T; i++)
    {
        int N;
        cin >> N;

        // Get naomi's bricks
        list<double> naomi_bricks;
        for (int j = 1; j <= N; j++)
        {
            double brick;
            cin >> brick;
            naomi_bricks.push_back(brick);
        }
        // sort them
        naomi_bricks.sort();

        // Get ken's bricks
        list<double> ken_bricks;
        for (int j = 1; j <= N; j++)
        {
            double brick;
            cin >> brick;
            ken_bricks.push_back(brick);
        }
        // again, sort them
        ken_bricks.sort();

        list<double> naomi_bricks2 = naomi_bricks;
        list<double> ken_bricks2 = ken_bricks;

        int deceitful_win = 0;
        for (int j = 0; j < N; j++)
        {
            if (naomi_bricks.front() > ken_bricks.front())
            {
                deceitful_win++;
                naomi_bricks.pop_front();
                ken_bricks.pop_front();
            }
            else
            {
                naomi_bricks.pop_front();
                ken_bricks.pop_back();
            }
        }

        int normal_loss = 0;
        for (int j = 0; j < N && ken_bricks2.size(); j++)
        {
            if (naomi_bricks2.front() < ken_bricks2.front())
            {
                normal_loss++;
                naomi_bricks2.pop_front();
                ken_bricks2.pop_front();
            }
            else
            {
                ken_bricks2.pop_front();
            }
        }
        int normal_win = N - normal_loss;
        
        cout << "Case #" << i << ": " << deceitful_win << " " << normal_win << endl;
    }
}