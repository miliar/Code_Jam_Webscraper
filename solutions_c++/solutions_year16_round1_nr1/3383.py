#include <iostream>
#include <cstdio>
#include <string>
#include <deque>
using namespace std;
string s;
deque <char> d;
int main()
{
    freopen("A-large.in", "rt", stdin);
    freopen("output.txt","wt", stdout);
    int n;
    cin >> n;
    for(int i = 0;i < n;i++)
    {
        cin >> s;
        d.clear();
        for(int j = 0;j < s.length();j++)
        {
            if (d.size() == 0)
                d.push_back(s[j]);
            else
            if(d.front() > s[j])
                d.push_back(s[j]);
            else
            (d.push_front(s[j]));
        }
        cout << "Case #" << i + 1 << ": ";
        for(int j = 0;j < int(d.size());j++)
        {
            cout << d[j];
        }
        cout << endl;
    }
    return 0;
}
