#include <iostream>
#include <vector>
#include <stdio.h>
using namespace std;

int main()
{
    int t, smax, ans;
    vector<int> v;
    
    cin >> t;
    
    for (int i=0; i<t; i++)
    {
        ans = 0;
        cin >> smax;
        int temp;
        for (int j=0; j <=smax; j++)
        {
            scanf("%1d",&temp);
            //cout << temp<<endl;
            v.push_back(temp);
            //cout << v[j] << endl;
        }
        
        int last = 0;
        int diff;
        for (int j=0; j<=smax; j++)
        {
            if (last < j)
            {
                diff = j - last;
                ans += diff;
                last += diff;
            }
            
            last += v[j];   // people hereclabed
        }
        v.clear();
        cout << "Case #" << i+1<<": "<< ans << endl;
    }
}
