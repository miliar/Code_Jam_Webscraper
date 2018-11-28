#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int solve(int B, int N, vector<int>& barbers)
{
    vector<int> now(B);
    for (int j = 0; j < B; j++)
    {
        now[j] = j+1;
        if (now[j] ==  N)
        {
            return j+1;
        }
    }
    int iter = 0;
    int next = B+1;
    while(true)
    {
        iter++;
        for (int j = 0; j < B; j++)
        {
            if (iter % barbers[j] == 0)
            {
                now[j] = next;
                if (now[j] == N)
                {
                    return j+1;
                }
                next++;
            }
        }
    }
}

int solve2(int B, int N, vector<int>& barbers)
{
    vector<int> now(B);
    for (int j = 0; j < B; j++)
    {
        now[j] = j+1;
        if (now[j] ==  N)
        {
            return j+1;
        }
    }
    int iter = 0;
    int next = B+1;
    while(true)
    {
        iter++;
        int count = 0;
        for (int j = 0; j < B; j++)
        {
            if (iter % barbers[j] == 0)
            {
                count++;
                now[j] = next;
                if (now[j] == N)
                {
                    return j+1;
                }
                next++;
            }
        }
        if (count == B)
            break;
    }
    int mod = now[0] - 1;
    int a = N % mod;
    a = a == 0 ? mod : a;
    return solve(B, a, barbers);
}

int main()
{
    int T;
    cin >> T;
    for (int i = 0; i < T; i++)
    {
        int B, N;
        cin >> B;
        cin >> N;
        vector<int> barbers(B);
        for (int j = 0; j < B; j++)
        {
            cin >> barbers[j];
        }
        cout << "Case #" << i+1 << ": " << solve2(B, N, barbers) << endl;
    }
    return 0;
}