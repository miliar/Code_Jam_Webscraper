#include <bits/stdc++.h>

#define pb push_back
#define mp make_pair
#define F first
#define S second


using namespace std;

int t;

int main()
{
    freopen("input.txt", "r",stdin);
    freopen("output.txt", "w", stdout);
    cin >> t;
    for (int h=0; h<t; h++)
    {
        int n;
        cin >> n;
        cout << "Case #" << h+1 << ": ";
        vector <pair <int, int > > p;
        for (int i=0; i<n; i++)
        {
            int x;
            cin >> x;
            p.pb(mp(x, i));
        }
       sort(p.rbegin(), p.rend());
        int a = p[0].F, b = p[1].F, n1 = p[0].S, n2 = p[1].S;
        if (a > b)
        {
            for (int i=0; i<a-b; i++)
                cout << char(n1+'A');
            cout << " ";
            a -= (a-b);
        }
        if (b > a)
        {
            for (int i=0; i<b-a; i++)
                cout << char(n2+'A');
            cout << " ";
            b -= (b-a);
        }
        for (int i=2; i<p.size(); i++)
        {
           while (p[i].F > 0)
           {
               if (p[i].F >= 2)
               {
                   cout << char(p[i].S+'A') << char(p[i].S+'A') << " ";
                   p[i].F -= 2;
               }
               else
               {
                   cout << char(p[i].S+'A') << " ";
                   p[i].F --;
               }
           }
        }
        while (a>0)
        {
            cout << char(n1+'A') << char(n2+'A') << " ";
            a--;
        }
        cout << endl;
        }
    return 0;
}

