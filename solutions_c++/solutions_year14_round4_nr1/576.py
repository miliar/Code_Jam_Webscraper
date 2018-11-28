#include <functional>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <numeric>
#include <cstring>
#include <cstdio>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <cmath>
#include <ctime>
#include <set>
#include <map>
#include <unordered_map>
#include <unordered_set>

using namespace std;

ifstream in("a_large.in");
ofstream out("a_large.out");

int main()
{
    int number;
    in >> number;
    for (int t = 1; t <= number; ++t)
    {
        int n, X;
        in >> n >> X;
        vector <int> v(n);
        for (int i = 0; i < n; ++i)
            in >> v[i];
        sort(v.begin(), v.end());


        int start = 0, end = v.size() - 1, ans = 0;
        while (end - start + 1 > 0)
        {
            if (end - start + 1 == 1)
            {
                ans++;
                break;
            }
            if (v[start] + v[end] <= X)
            {
                ans++;
                start++;
                end--;
            }
            else
            {
                ans++;
                end--;
            }
        }
        out << "Case #" << t << ": " << ans << endl;
    }
    return 0;
}