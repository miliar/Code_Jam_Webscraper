#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <set>
#define rep(i,j,k) for (int i=j;i<=k;++i)
#define rrep(i,j,k) for (int i=j;i>=k;--i)

using namespace std;

int T,n,m,a[111][111],b[111][111];
set<int> s;

int main()
{
    /*
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    */
    ios::sync_with_stdio(false);
    cin >> T;
    rep(test_case,1,T)
	{
	    bool yes = true;
	    cin >> n >> m;
	    rep(i,1,n) rep(j,1,m) cin >> a[i][j],s.insert(a[i][j]),b[i][j] = a[i][j];
	    cout << "Case #" << test_case << ": ";
	    for (set<int>::iterator it = s.begin(); it != s.end(); ++ it)
		{
		    int now = *it;
		    rep(i,1,n) 
			{
			    bool check = true;
			    rep(j,1,m) if (now < a[i][j])
				{
				    check = false;
				    break;
				}
			    if (check)
				rep(j,1,m) b[i][j] = now+1;
			}
		    rep(j,1,m)
			{
			    bool check = true;
			    rep(i,1,n) if (now < a[i][j])
				{
				    check = false;
				    break;
				}
			    if (check) 
				rep(i,1,n) b[i][j] = now+1;
			}
		    rep(i,1,n) 
			{
			    rep(j,1,m) if (b[i][j] == now) 
				{
				    cout << "NO" << endl;
				    yes = false;
				    goto down;
				}
			}
		}
		down:if (yes) cout << "YES" << endl;
	}
    return 0;
}
