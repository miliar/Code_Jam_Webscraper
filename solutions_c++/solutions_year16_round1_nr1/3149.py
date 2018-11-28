#include <bits/stdc++.h>
#define maxs 1000000
#define pb push_back

using namespace std;

int main ()
{
    freopen ("input.txt","r",stdin);
    freopen ("output.txt","w",stdout);

    int t,kase=0;

    cin >> t;

    while (t--) {
        string str;
        cin >> str;
        deque <char> out;

        out.pb (str[0]);

        for (int i=1;i<str.size ();i++) {
            if (str[i] >= out.front()) out.push_front(str[i]);
            else out.pb (str[i]);
        }

        printf ("Case #%d: ",++kase);

        deque <char> :: iterator it = out.begin();

        for (;it!=out.end ();it++) {
            cout << *it ;
        }
        puts ("");
    }
    return 0;
}
