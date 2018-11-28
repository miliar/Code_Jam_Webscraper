#include <iostream>
#include <cmath>
#include <algorithm>
#include <fstream>
#include <string>
#include <vector>
#include <map>

#define getmax(a, b) ((a)>(b)) ? (a) : (b)
#define getmin(a, b) ((a)<(b)) ? (a) : (b)

using namespace std;

int t,k,a,b,ans;

int main()
{
	ios_base::sync_with_stdio(false);

    ifstream in ("b.in");
    ofstream out ("b.out");

    in >> t;
    for (int ti=1; ti<=t; ti++)
    {
        bool hasht[1000]={0};
        ans=0;
        in >> a >> b >> k;
        for (int i=0; i<a; i++)
            for (int j=0; j<b; j++)
            {
                ans+=((i&j)<k);
                if (i==j)
                {
                    if (hasht[i])
                        ans-=((i&j)<k);
                    else
                        hasht[i]=1;
                }
            }
        out << "Case #" << ti << ": " << ans << '\n';

    }

    in.close();
    out.close();
}
