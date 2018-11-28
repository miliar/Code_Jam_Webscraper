/* https://code.google.com/codejam/contest/6224486/dashboard#s=p3 */

#include<bits/stdc++.h>

using namespace std;

typedef unsigned long long ull;
typedef long long ll;
#define rep(i,a,n) for(__typeof(n) i = a; i < n; ++i)
#define repe(i,a,n) for(__typeof(n) i = a; i <= n; ++i)
#define mfill(a,b) memset(a, b, sizeof(a))
#define all(a) a.begin(), a.end()
#define pb(a) push_back(a)
#define dbg(x) {cout<<__LINE__ <<"::" << #x << ": " << (x) << endl; }


int main()
{
    ios_base::sync_with_stdio(false);
//  freopen("t_case.txt","r",stdin);
    int t;
    cin>> t;
    string g = "GABRIEL";
    string r = "RICHARD";
    repe(_cases, 1, t)
    {
        int x,r,c;
        cin >> x >> r >> c;
        cout << "Case #" << _cases <<": ";
        if(x == 1)
           {
               cout << g <<"\n";
               continue;
           }
        if(x == 2)
        {
            if( (r == 1 and c == 1) or (r == 1 and c == 3) or (r == 3 and c == 1) or(r == 3 and c == 3) )
                {
                    cout << r <<"\n";
                continue;
                }
            else
            {
                cout << g <<"\n";
                continue;
            }
        }
        if(x == 3)
        {
            if( (r == 1 or c == 1) or (r == 2 and c== 2) or (r == 4 and c == 4) or (r == 2 and c == 4) or (r == 4 or c == 2) )
            {
                cout << r  << "\n";
                continue;
            }
            else
            {
                cout << g << "\n";
                continue;
            }
        }
        if(x == 4)
        {
            if( (r== 4 and c==3) or (r==3 and  c==4) or (r == 4 and c == 4) )
            {
                cout << g <<"\n";
                continue;
            }
            else
                cout << r << "\n";

        }


    }
    return 0;
}
