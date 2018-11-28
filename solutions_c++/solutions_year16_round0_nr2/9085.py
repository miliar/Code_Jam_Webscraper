#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

int main()
{
    freopen("B-large.in", "r", stdin);

    freopen("B-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    vector<int> v;
    string s;
    for (int i = 1; i <= T; i++)
    {
        int cnt = 0;
        v.clear();
        cin >> s;
        string::iterator p = s.begin();
        if (*p == '+')
            v.push_back(1);
        else
            v.push_back(0);
        for(  p = s.begin() + 1; p!= s.end() ; p++ )
        {
            if (*p == *(p-1))
                continue;
            else if (*p == '+')
                v.push_back(1);
            else v.push_back(0);
        }
        if (v[0] == 0) cnt++;
        for (vector<int>::iterator it = v.begin()+1; it != v.end(); it++)
        {
            if (*it == 0)
                cnt += 2;
        }
        printf("Case #%d: %d\n", i, cnt);
    }
}
