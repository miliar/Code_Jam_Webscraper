#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>

using namespace std;

int compare_to(vector <int> a, vector <int> b)
{
    int cont = 0, pos = -1;
    for(int i = 0; i < 4; i ++)
    {
        for(int j = 0; j < 4; j ++)
        {
            if(a[i] == b[j])
            {
                cont ++;
                pos = i;
            }
        }
    }
    if(cont == 1) return pos + 1;
    else if(cont == 0) return pos;
    else return 0;
}

int main()
{
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);
    int t; cin >> t;
    for(int i = 0; i < t; i ++)
    {
        int first, seconds, nums;
        vector <int> grid1, grid2;
        //primera lectura
        cin >> first;
        for(int j = 0; j < 4; j ++)
        {
            for(int z = 0; z < 4; z ++)
            {
                cin >> nums;
                if(j == first - 1) grid1.push_back(nums);
            }
        }
        //segunda lectura
        cin >> seconds;
        for(int j = 0; j < 4; j ++)
        {
            for(int z = 0; z < 4; z ++)
            {
                cin >> nums;
                if(j == seconds - 1) grid2.push_back(nums);
            }
        }
        int res = compare_to(grid1, grid2);
        if(res > 0) cout << "Case #" << i + 1 << ": " << grid1[res - 1] << endl;
        else if(res == 0)cout << "Case #" << i + 1 << ": Bad magician!" << endl;
        else cout << "Case #" << i + 1 << ": Volunteer cheated!" << endl;
    }

    return 0;
}
