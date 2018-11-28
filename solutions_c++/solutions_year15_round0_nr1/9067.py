/*
** Coder  : Amit Tiwari
** Handle : pipipzz
*/
#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define all(v) v.begin(),v.end()
#define rep(i,n) for(int i=0;i<(int)(n);i++)
#define rep2(i,m,n) for(int i=m;i<(int)(n);i++)
#define For(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
#define INF (int)1e9
#define eps 1.0e-11

int main()
{
    int t;
    cin >> t;
    for(int x=1; x <=t; x++)
    {
        int s;
        cin >> s;
        cin.get();
        string str;
        getline(cin, str);
        int n = s+1;
        int up = str[0] - '0', needed = 0;
        rep2(i, 1, n)
        {
            if(str[i] == '0')
                continue;
            if(up >= i)
            {
                up += str[i] - '0';
            }
            else
            {
                needed += i - up;
                up += i - up + (str[i] - '0');
            }
        }
        cout << "Case #" << x << ": ";
        cout << needed << endl;
    }
    return 0;
}
