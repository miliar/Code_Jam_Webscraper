#include <iostream>
#include <algorithm>
#include <vector>
#include <fstream>
#include <string>

using namespace std;

int maxt = 0;


int func(vector <int> A, int time)
{
    if (time > maxt)
    {
        return maxt;
    }
    stable_sort(A.begin(), A.end());
    int si = A.size();
    si -= 1;
    int ans = A[si] + time;
    for (int i = 1; i <= A[si] / 2; ++i)
    {
        A[si] -= i;
        A.push_back(i);
        ++time;
        ans = min(ans,func(A,time));
        --time;
        A.pop_back();
        A[si] += i;
    }
    return ans;
}

int main()
{
    freopen("input.txt", "r",stdin);
    freopen("output.txt", "w",stdout);
    int T;
    cin >> T;
    for (int z = 0; z < T; ++z)
    {
        int D;
        cin >> D;
        vector <int> A(D);
        for (int i = 0; i < D; ++i)
        {
            cin >> A[i];
        }
        stable_sort(A.begin(), A.end());
        maxt = A[D - 1];
        int ans = func(A,0);
        cout << "Case #" << z + 1 << ": " << ans << endl;
    }
    return 0;
}
