#include <iostream>
#include <stdio.h>
#include <map>
#include <set>
#include <vector>
#include <algorithm>
#include <math.h>

using namespace std;

double m1[1100];
double m2[1100];
bool used[1100];

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for(int i = 0 ; i < t ; ++i)
    {
        cout << "Case #" << i+1 << ": ";
        
        int n;
        cin >> n;
        for(int i = 0 ; i < n ; ++i)
            cin >> m1[i];
        for(int i = 0 ; i < n ; ++i)
            cin >> m2[i];
    
        sort(m1, m1+n);
        sort(m2, m2+n);
        
        int c1(0), c2(0);
        memset(used, 0, sizeof used);
        
        for(int i = 0 ; i < n ; ++i)
        {
            bool fl = 0;
            for(int j = 0 ; j < n ; ++j)
            if(!used[j] && m1[i] < m2[j])
            {
                used[j] = 1;
                fl = 1;
                break;
            }
            if(!fl)
                ++c2;
        }
        
        memset(used, 0, sizeof used);
        for(int i = 0 ; i < n ; ++i)
        {
            int t = 0;
            int k = n-1, j = n-1;
            while(k >= i)
            {
                while(j >=0)
                {
                    if(!used[j] && m1[k] > m2[j]) break;
                    --j;
                }
                if(j < 0) break;
                
                ++t;
                --k, --j;
            }
            
            for(int j = n-1 ; j >= 0 ; --j)
            if(!used[j] && m1[i] < m2[j])
            {
                used[j] = 1;
                break;
            }
            
            c1 = max(c1, t);
        }
        
        cout << c1 << " " << c2 << "\n";
    }
    return 0;
}
