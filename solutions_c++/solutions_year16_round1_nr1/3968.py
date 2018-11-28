#include <deque>
#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t;
    string s;
    deque<char> d;
    cin >> t;
    cin.ignore();
    for(int c=1; c<=t; c++)
    {
        d.clear();
        getline(cin, s);
        d.push_back(s[0]);
        for(int k=1; k<s.length(); k++)
        {
            if(s[k] >= d.front())
                d.push_front(s[k]);
            else
                d.push_back(s[k]);
        }
        printf("Case #%d: ", c);
        for(auto k:d)
            printf("%c", k);
        printf("\n");
    }
    return 0;
}
