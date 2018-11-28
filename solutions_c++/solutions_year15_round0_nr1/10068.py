/*
 * Problem: Standing Ovation
 */

#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main(int argc, char **argv)
{
    freopen("A-small-attempt1.in", "r", stdin);
    freopen("standing_ovation.out", "w", stdout);

    int testcase = 0;
    cin >> testcase;

    for (int i = 0; i < testcase; i++)
    {
        int size;
        int sum = 0;
        int friends = 0;
        string audience;

        cin >> size;
        cin >> audience;
       
        sum = audience[0] - 48;
        for (int j = 1; j <= size; j++)
        { 
            int cur = audience[j] - 48;
            if (!cur)
                continue;
            if (sum < j) {
                friends += j - sum;
                sum += cur + j - sum;
            } else {
                sum += cur;
            }
        }
        cout << "Case #" << i+1 << ": " << friends << "\n";
    }

    return 0;
}


