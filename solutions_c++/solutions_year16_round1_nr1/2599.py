#include <bits/stdc++.h>

using namespace std;

int main(int argc, char* argv[])
{
    (void)argc; (void)argv;
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t;
    cin >> t;
    for(int caso = 1; caso <= t; caso++)
    {
        string s;
        cin >> s;
        list<char> l;
        for(char c: s)
        {
            if(l.empty())
                l.push_back(c);
            else if(c >= *l.begin())
                l.push_front(c);
            else
                l.push_back(c);
        }
        cout << "Case #" << caso << ": ";
        for(char c: l)
            cout << c;
        cout << endl;
    }
    return EXIT_SUCCESS;
}
