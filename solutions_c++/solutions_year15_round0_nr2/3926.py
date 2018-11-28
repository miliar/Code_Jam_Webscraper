#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <set>
#include <map>
#include <queue>
#define lol long long
using namespace std;

ofstream out("output.txt");
ifstream in("input.txt");

#define cin in
#define cout out

int mul(int a, int b) // 1 = 1, i = 2, j = 3, k = 4
{
    int koko[4][4] = {{1, 2, 3, 4}, {2, -1, 4, -3}, {3, -4, -1, 2}, {4, 3, -2, -1}};
    return koko[abs(a) - 1][abs(b) - 1] * a / abs(a) * b / abs(b);
}

int main()
{
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i)
    {
        int d;
        cin >> d;
        vector<int> v(6, 1);
        for (int i = 0; i < d; ++i)
            cin >> v[i];
        int ans = 789798;
        for (int i0 = 1; i0 <= v[0]; ++i0)
            for (int i1 = 1; i1 <= v[1]; ++i1)
                for (int i2 = 1; i2 <= v[2]; ++i2)
                    for (int i3 = 1; i3 <= v[3]; ++i3)
                        for (int i4 = 1; i4 <= v[4]; ++i4)
                            for (int i5 = 1; i5 <= v[5]; ++i5)
                            {
                                int ans1 = i0 + i1 + i2 + i3 + i4 + i5 - 6;
                                int q0 = (v[0] + i0 - 1) / i0;
                                int q1 = (v[1] + i1 - 1) / i1;
                                int q2 = (v[2] + i2 - 1) / i2;
                                int q3 = (v[3] + i3 - 1) / i3;
                                int q4 = (v[4] + i4 - 1) / i4;
                                int q5 = (v[5] + i5 - 1) / i5;
                                ans1 += max(q0, max(q1, max(q2, max(q3, max(q4, q5)))));
                                ans = min(ans, ans1);
                            }
        cout << "Case #" << i << ": " << ans << endl;
    }
}


/*

int main()
{
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i)
    {
        cout << "Case #" << i << ": ";
        int d;
        cin >> d;
        cout << endl << d << endl;
        priority_queue<int> q;
        for (int i = 0; i < d; ++i)
        {
            int x;
            cin >> x;
            cout << x << " ";
            q.push(x);
        }
        int ans = q.top();
        int add = 0;
        while (q.top() != 1)
        {
            int w = q.top();
            q.pop();
            int ff = w / 2;
            int ss = w / 2 + (w & 1);
            ++add;
            int ans1 = add + ss;
            if (!q.empty())
                ans1 = max(ans1, add + q.top());
            q.push(ff);
            q.push(ss);
            ans = min(ans, ans1);
        }
        
        
        
        
            cout << endl << ans << endl;
    }
}*/