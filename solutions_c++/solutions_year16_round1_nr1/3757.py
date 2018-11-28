#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define mod 1000000007
bool a[1009];
char ch[1009];
int x;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.txt","w",stdout);
	ios::sync_with_stdio(false);
	cin.tie(0);
    int t, l, i, j;
    string s;
    cin >> t;
    for(j = 1; j <= t; j++)
    {
        cin >> s;
        l = s.length();
        cout << "Case #" << j << ": ";
        for(i = 0; i < l; i++)
            a[i] = false;
        ch[0] = s[0];
        x = 0;
        a[0] = true;
        for(i = 1; i < l; i++)
        {
            if((int)s[i] >= (int)ch[x])
            {
                a[i] = true;
                ch[++x] = s[i];
            }
        }
        for(i = x; i >= 0; i--)
            cout << ch[i];
        for(i = 0; i < l; i++)
        {
            if(!a[i])
                cout << s[i];
        }
        cout << '\n';
    }
	return 0;
}
