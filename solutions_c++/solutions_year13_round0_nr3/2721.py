#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <fstream>
#include <algorithm>
#define rep(i,j,k) for (int i=j;i<=k;++i)
#define rrep(i,j,k) for (int i=j;i>=k;--i)

using namespace std;

typedef long long LL;
int T,w[111];
LL a,b,ans;

bool is_palindrome(LL k)
{
    w[0] = 0;
    while (k>0)
	{
	    w[++w[0]] = k % 10;
	    k /= 10;
	}
    bool ret = true;
    rep(i,1,w[0]/2) if (w[i] != w[w[0]-i+1]) {ret = false;break;}
    return ret;
}

int main()
{
    /*
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    */
    ios::sync_with_stdio(false);
    cin >> T;
    rep(test_case,1,T)
	{
	    ans = 0;
	    cin >> a >> b;
	    rep(i,sqrt(a),sqrt(b))
		{
		    LL c = i;
		    LL d = i * i;
		    if (d >= a && d <= b)
			{
			    if (is_palindrome(c) && is_palindrome(d))
				ans++;
			}
		}
	    cout << "Case #" << test_case << ": " << ans << endl;
	}
    return 0;
}
