#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <iostream>
#include <map>
#include <set>
#include <list>
#include <vector>



using namespace std;

const int MAX = 1e5;
const int MOD = 1000000007;
const double EPS = 1e-9;
int T;
int arr[10100];
int ems[10100], ecnt = 0;

int main() 
{
    freopen("input.txt", "r", stdin);
    freopen("outpu.txt", "w", stdout);
    cin >> T;    
    
    
    for(int Ti = 1; Ti <= T; ++Ti)
    {
        int x, s;
        cin >> x >> s;
        
        for(int i = 0; i < x; ++i)
            cin >> arr[i];
        
        ecnt = 0;
        int cnt = 0;
        sort(arr, arr + x);
        for(int i = x - 1; i >= 0; --i)
        {
            int it = 0, mint = -1, mind = 1000;
            for(;it < ecnt; ++it)
            {
                if(ems[it] >= arr[i] && (ems[it] - arr[i]) < mind)
                {
                    mind = (ems[i] - arr[i]);
                    mint = it;
                }
            }
            if(mint == -1)
            {
                ++cnt;
                ems[ecnt++] = s - arr[i];
            }                
            else
            {
                ems[mint] = 0;
            }
        }
        
        cout << "Case #" << Ti << ": " << cnt << "\n";
    }

    return 0;
}

