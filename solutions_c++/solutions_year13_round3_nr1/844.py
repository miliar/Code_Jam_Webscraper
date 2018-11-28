#include<iostream>
#include<string>
#include<vector>
using namespace std;

typedef long long LL;

void print( int t, LL ans)
{
    cout << "Case #" << t << ": " << ans << endl;
}

#define dbg(x) cerr << #x << " = " << x << " "

int main()
{
    int T;
    cin >> T;
    for (int t=0;t<T;++t)
    {
        string str;
        int n;
        cin >> str >> n;
        int l=0, r=0;
        int cur_cons=0;
        LL ans = 0;
        for (l=0;l<str.size();++l)
        {
            while ( cur_cons < n && r <str.size())
            {
                if ( str[r] != 'a' && str[r] != 'e' 
                     && str[r] != 'i' && str[r] != 'o' 
                     && str[r] != 'u')
                {
                    cur_cons++;
                } else
                {
                    cur_cons=0;
                }
                r++;
            }

            if ( cur_cons < n)
            {
                break;
            }
#if 0
            dbg( l);
            dbg( r);
            dbg(cur_cons);
            dbg(str.substr(l,r-l)) << endl;
#endif
            ans += str.size()-r+1;
            if ( r-l == cur_cons)
            {
                cur_cons--;
            }
        }

        print(t+1, ans);
    }
}
