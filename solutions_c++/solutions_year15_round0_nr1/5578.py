#include <iostream>
#include <algorithm>

using namespace std;

int num(int a)
{
    return a - '0';
}

int main()
{
    ios_base::sync_with_stdio(0);
    
    int tests;
    cin>>tests;
    
    for(int x = 1; x<=tests; x++)
    {
        int total = 0;
        int friends = 0;
        
        int smax;
        cin>>smax;
        
        string nums;
        cin>>nums;
        
        for(int i=0; i<nums.size(); i++)
        {
            int akt = num(nums[i] );
            
            if(total < i)
            {
                friends += i - total;
                total = i;
            }
            
            total += akt;
        }
        
        cout<<"Case #"<<x<<": "<<friends<<"\n";
    }
    
    
    return 0;
}