#include <iostream>
#include <string>
#include <fstream>
#include <set>
#include <map>
#include <queue>
#define lol long long
using namespace std;

ofstream out("output2.txt");
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
        int l, k;
        cin >> l >> k;
        string s_, s;
        cin >> s_;
        for (int j = 0; j < min(k, 8 + (k & 3)); ++j)
            s += s_;
        
        int next = 0;
        int posI = -1;
        int posJ = -1;
        int val = 1;
        while (next < s.length())
        {
            val = mul(val, s[next] - 'i' + 2);
            if (val == 2)
            {
                posI = next;
                ++next;
                break;
            }
            ++next;
        }
        val = 1;
        while (next < s.length())
        {
            val = mul(val, s[next] - 'i' + 2);
            if (val == 3)
            {
                posJ = next;
                ++next;
                break;
            }
            ++next;
        }
        val = 1;
        for (int j = next; j < s.length(); ++j)
            val = mul(val, s[j] - 'i' + 2);
        if (val == 4 && posI != -1 && posJ != -1)
        {
            cout << "Case #" << i << ": YES" << endl;
        }
        else
            cout << "Case #" << i << ": NO" << endl;
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