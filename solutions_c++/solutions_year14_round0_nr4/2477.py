#include <iostream>
#include <cmath>
#include <algorithm>
#include <fstream>
#include <string>
#include <vector>

#define getmax(a, b) ((a)>(b)) ? (a) : (b)
#define getmin(a, b) ((a)<(b)) ? (a) : (b)

using namespace std;
int n,t,dp,p;
double ken[1000], naomi[1000];

int main()
{
	ios_base::sync_with_stdio(false);

    ifstream in ("D.in");
    ofstream out ("D.out");
    in >> t;
    for (int ti=1; ti<=t; ti++)
    {
        p=0;
        dp=0;
        in >> n;
        for (int i=0; i<n; i++)
            in >> naomi[i];
        for (int i=0; i<n; i++)
            in >> ken[i];
        sort (naomi,naomi+n);
        sort (ken,ken+n);
        //Deceitful
        int j=-1,ans=0;
        for (int i=0; i<n; i++)
        {
            j++;
            while (j<n && naomi[j]<ken[i])
                j++;
            if (j<n)
                ans++;
            else
                break;
        }
        out << "Case #" << ti << ": " << ans << ' ';
        // Normal
        int i;
        ans=0,j=-1;
        for (i=0; i<n; i++)
        {
            j++;
            while (j<n && ken[j]<naomi[i])
                j++;
            if (j==n)
                break;
        }
        //if (ti==3)cout << i;
        out << n-i << '\n';
    }
}
