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

int r,n,m,k,num;
struct node
{
    int x,y,z;
    bool can[700];
}p[1000];
int v[1000];

int main()
{
    freopen("c.in","r",stdin);
    freopen("c.out","w",stdout);
    int T;
    cin >> T;
    rep(test,1,T)
	{
	    cin >> r >> n >> m >> k;
	    rep(i,2,5) rep(j,2,5) rep(k,2,5)
		{
		    ++num;
		    p[num].x = i;
		    p[num].y = j;
		    p[num].z = k;
		    p[num].can[1] = true;
		    p[num].can[i] = true;
		    p[num].can[j] = true;
		    p[num].can[k] = true;
		    p[num].can[i*j] = true;
		    p[num].can[i*k] = true;
		    p[num].can[j*k] = true;
		    p[num].can[i*j*k] = true;
		}
	    cout << "Case #" << test << ": " << endl;
	    rep(i,1,r)
		{
		    rep(i,1,k) cin >> v[i];
		    rep(i,1,num)
			{
			    bool yes = true;
			    rep(j,1,k)
				{
				    if (!p[i].can[v[j]])
					{
					    yes = false;
					    break;
					}
				}
			    if (yes)
				{
				    cout << p[i].x << p[i].y << p[i].z << endl;
				    break;
				}
			}
		}
	}
    return 0;
}
