// RCC_A.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <string>
#include <vector>
#include <math.h>
#include <set>
#include <map>
#include <algorithm>
#include <time.h>

using namespace std;

int main(int argc, char* argv[])
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    for (int t = 0; t < T; ++t)
    {
        int n;
        cin >> n;
        vector <int> s;
        for (int i = 0; i <= n; ++i)
        {
            char c;
            cin >> c;
            s.push_back(c - '0');
        }
        int answer = 0;
        int sum = s[0];
        for (int i = 1; i <= n; ++i)
        {
            if (sum < i)
            {
                answer += i - sum;
                sum = i;
            }
            sum += s[i];
        }
        cout << "Case #" << t + 1 << ": " << answer << endl;
    }
	return 0;
}

