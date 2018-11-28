#include <iostream>
#include <string>
#include <cstdio>
#include <map>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;

void perform()
{
    int n;
    int plate[1024];    // 有k个pancake的plate数目
    int max_plate = 0;  // 最大的plate数目
    int min_plate;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> plate[i];
        max_plate = max(max_plate, plate[i]);
    }

    min_plate = max_plate;
    for(int i = 1; i <= max_plate; i++)
    {
        int sum = i;
        for (int j = 0 ; j < n ; j++)
        {
            if (plate[j] > i)
            {
                if (plate[j] % i == 0)
                    sum += (plate[j] / i - 1);
                else
                    sum += (plate[j] / i) ;
            }
        }
        min_plate = min(min_plate, sum) ;
    }
    cout << min_plate << endl;
}

void redirect(string filename)
{
    freopen((filename + ".in").c_str(), "r", stdin);
    freopen((filename + ".out").c_str(), "w", stdout);
}

int main()
{
    redirect("./q2/large");
    int total_tests;
    cin >> total_tests;
    for (int test_id = 1; test_id <= total_tests; test_id++)
    {
        cout << "Case #" << test_id << ": ";
        perform();
    }
    return 0;
}
