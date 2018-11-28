
#include<set>
#include<map>
#include<list>
#include<iomanip>
#include<cmath>
#include<string>
#include<vector>
#include<queue>
#include<stack>
#include<complex>
#include<sstream>
#include<iostream>
#include<fstream>
#include<algorithm>
#include<numeric>
#include<utility>
#include<functional>
#include<stdio.h>
#include<assert.h>
#include<memory.h>
#include<bitset>

using namespace std;

#define all(v)				((v).begin()), ((v).end())


vector<int> a;
int n;

bool ch()
{
    for(int i = 0; i < n; i++)
        if(a[i] == 0) return 1;
    return 0;
}
int main ()
{
    //freopen("/Users/KhalidRamadan/Desktop/input.txt","r",stdin);
    //freopen("/Users/KhalidRamadan/Desktop/output.txt","w",stdout);
    int t;
    cin >> t;
    for(int T = 1; T <= t; T++)
    {
        string s;
        cin >> s;
        a = vector<int>(s.size(), 0);
        n = (int)s.size();
        for(int i = 0; i < n; i++)
            if(s[i] == '+') a[i] = 1;
        int ans = 0;
        while (ch())
        {
            bool plus = 0;
            for(int i = 0; i < n; i++)
                if(a[i] == 1)
                {
                    a[i] = 0;
                    plus = 1;
                }
                else
                {
                    if(plus) ans ++;
                    break;
                }
            int last = 0;
            for(int i = n - 1; i >= 0; i--)
                if(a[i] == 0)
                {
                    last  = i;
                    break;
                }
            vector<int> b = a;
            for(int i = 0, j = last; i <= last; i++, j--)
            {
                b[i] = !a[j];
            }
            a = b;
            ans ++;
        }
        cout << "Case #" << T << ": ";
        cout << ans << endl;
    }
}
