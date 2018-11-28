#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool is_possible(const vector<int>& pancakes, int normal_minutes, int special_minutes)
{
    /*
    cout << normal_minutes << " " << special_minutes << " #";
    for(int i=0; i<pancakes.size();i++)
    {
        cout << pancakes[i] << " ";
    }
    cout << endl;
    */

    auto max_pancakes_iter = max_element(pancakes.begin(), pancakes.end());
    if(*max_pancakes_iter <= normal_minutes)
        return true;

    if(special_minutes >= 1)
    {
        /*
        for(int j=0; j<pancakes.size(); j++)        //which table
        {
            for(int k=1; k<pancakes[j]; k++)        //how many pancakes
            {
                vector<int> pancakes_copy(pancakes);
                pancakes_copy[j] -= k;
                pancakes_copy.push_back(k);
                if(is_possible(pancakes_copy, normal_minutes, special_minutes-1))
                    return true;
            }
        }
        */
        int max_index = distance(pancakes.begin(), max_pancakes_iter);
        //for(int j=0; j<pancakes.size(); j++)        //which table
        {
            //for(int k=1; k<pancakes[j]; k++)        //how many pancakes
            int k = pancakes[max_index]-normal_minutes;
            {
                vector<int> pancakes_copy(pancakes);
                pancakes_copy[max_index] -= k;
                pancakes_copy.push_back(k);
                if(is_possible(pancakes_copy, normal_minutes, special_minutes-1))
                    return true;
            }
        }
    }
    return false;
}

bool is_possible(const vector<int>& pancakes, int minutes)
{
    for(int i=0; i<minutes; i++)
    {
        if(is_possible(pancakes, minutes-i, i))
            return true;
    }
    return false;
}

int binary_search_min_possible(const vector<int>& pancakes, int max_pancakes)
{
    int possible = max_pancakes;
    int impossible = 0;
    int delta = possible - impossible;
    while(delta > 1)
    {
        int n_to_check = impossible + delta/2;
        if(is_possible(pancakes, n_to_check))
        {
            possible = n_to_check;
//            cout << "   possible: " << n_to_check << endl;
        }
        else
        {
            impossible = n_to_check;
//            cout << "   impossible: " << n_to_check << endl;
        }

        delta = possible-impossible;
    }

    return possible;
}

int main()
{
    int n_cases;
    cin >> n_cases;
    for(int i=1; i<=n_cases; i++)
    {
        int n_non_empty_plates;
        int max_pancakes = 0;
        cin >> n_non_empty_plates;
        int min_n_minutes;
        vector<int>  n_pancakes(n_non_empty_plates);
        for(int i=0; i<n_non_empty_plates; i++)
        {
            int current_n_pancakes;
            cin >> current_n_pancakes;
            n_pancakes[i] = current_n_pancakes;
            if(current_n_pancakes > max_pancakes)
            {
                max_pancakes = current_n_pancakes;
            }
        }
        min_n_minutes = binary_search_min_possible(n_pancakes, max_pancakes);
        cout << "Case #" << i << ": "  << min_n_minutes << endl;
    }
}
