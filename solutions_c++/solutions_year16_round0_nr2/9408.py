#include <bits/stdc++.h>


using namespace std;

int main ()
{
    freopen ("in.txt","r",stdin);
    freopen ("out.txt","w",stdout);

    int t,kase=0;

    cin >> t;

    string str;

    while (t--) {
        cin >> str;

        int cost =0;

        int sz = str.size ()-1;

        while (str[sz]=='+' && sz>-1) sz--;

        for (int i=0;i<=sz;i++) {
            while (str[i]==str[i+1] && i<str.size ()) {
                i++;
            }
            cost++;
        }
        printf ("Case #%d: %d\n",++kase,cost);

    }
    return 0;
}
