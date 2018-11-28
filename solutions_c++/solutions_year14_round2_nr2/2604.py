#include <iostream>
#include <vector>
#include <algorithm>
#include <bitset>


using namespace std;
    

int solve()
{
    int a,b,c;
    int count = 0;
    
    cin >> a >> b >> c;
    
    for(int x = 0; x<a; x++)
    {
        for(int y = 0; y<b; y++)
        {            
            bitset<11> first (x);
            bitset<11> second (y);
            
            bitset<11> ans (first&second);               
            
            if(ans.to_ulong() < c) count++;
            
        }
    }
    
    
    return count;
}

int main()
{
    int t;
    int count = 1;
    cin >> t;
    while(count <= t)
    {
        cout << "Case #" << count << ": " << solve() << endl;
        count++;
    }
    
    return 0;
}
