#include <iostream>
#include <cstdio>
#include <vector>
#include <string>

using namespace std;

int main()
{
    int t;
    int n,m,q;
    
    scanf("%d", &t);
    bool w;
    int e;
    for (e=1; e<=t; ++e)
    {
        scanf("%d %d", &n, &m);
        vector <vector <int> > v(n);
        
        for (int i=0; i<n; ++i)
        {
            for (int j=0; j<m; ++j)
            {
                scanf("%d", &q);
                v[i].push_back(q);
            }
        }
        w=1;
        vector <int> y(n), x(m);
        
        for (int i=0; i<n; ++i)
        {
            for (int j=0; j<m; ++j)
            {
                y[i]=max(y[i], v[i][j]);
                x[j]=max(x[j], v[i][j]);
            }
        }
        
        for (int i=0; i<n; ++i)
        {
            for (int j=0; j<m; ++j)
            {
                if (v[i][j] < x[j] && v[i][j] < y[i]) w=0;
            }
        }
        
        if (w) printf("Case #%d: YES\n", e);
        else printf("Case #%d: NO\n", e);
    }
    
    

	return 0;
}