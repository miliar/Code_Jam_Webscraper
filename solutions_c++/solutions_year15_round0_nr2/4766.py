#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    int T;
    cin>>T;
    
    for(int caso=1; caso<=T; caso++)
    {
        int n;
        cin>>n;
        vector <int> v(n);
        
        for(int i=0; i<n; i++)
            cin>>v[i];
        
        int maxN = v[0];
        for(int i=1; i<n; i++)
            maxN = max(maxN, v[i]);
        
        int minN = 1<<30;
        for(int x=1; x<=maxN; x++)
        {
            int cur = x;
            for(int i=0; i<n; i++)
            {
                if(v[i] > x)
                {
                    int delta = v[i] - x;
                    int need = (delta - 1) / x + 1;
                    cur += need;
                }
            }
            minN = min(minN, cur);
        }
        
        cout<<"Case #"<<caso<<": "<<minN<<endl;
    }
    
    return 0;
}
