#include <iostream>
#include <string>
#include <cstring>
#include <cstdio>
#include <sstream>
#include <algorithm>

using namespace std;

const int MAX_PANCAKES = 1000;

bool solve(const vector<int> &diners, int num_special_mins, int target_pancakes)
{
    int n = diners.size();
    int cur_special_mins = num_special_mins;
    for(int i = 0; i < n; ++i) 
    {
        int cur_diner = diners[i];
        if(cur_diner > target_pancakes) 
        {
            int to_move = cur_diner;
            int need_mins = (to_move - 1) / target_pancakes;
            if(cur_special_mins < need_mins)
            {
                return false;
            }
            cur_special_mins -= need_mins;
        }
    }
    return true;
}

int main(int argc, char *argv[]) {
    int TC;
    cin >> TC;
    for(int tc = 1; tc <= TC; ++tc)
    {
        int D = 0;
        int max_pancakes = 0;
        int sum = 0;
        vector<int> diners;
        
        cin >> D;
        for(int i = 0; i < D; ++i)
        {
            int di;
            cin >> di;
            max_pancakes = max(max_pancakes, di);
            sum += di;
            diners.push_back(di);
        }
        
        int ans = max_pancakes;
        for(int num_special_mins = 0; num_special_mins <= MAX_PANCAKES; ++num_special_mins)
        {
            for(int target_pancakes = 1; target_pancakes <= MAX_PANCAKES; ++target_pancakes)
            {
                if(solve(diners, num_special_mins, target_pancakes))
                {
                    ans = min(ans, num_special_mins + target_pancakes);
                }                
            }
        }
        cout << "Case #" << tc << ": " << ans << '\n';
    }
    return 0;
}
