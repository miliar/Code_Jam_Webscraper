#include <iostream>
#include <vector>
#include <cstring>
#include <algorithm>
#include <string>
#include <cmath>
#include <cstdlib>
#include <map>
#include <set>

using namespace std;


int main()
{
    int cases, n, cnt = 1;
    
    cin >> cases;
    while(cases--)
    {
        cin >> n;
        double niome[n], ken[n];
        
        for(int i = 0; i < n ; i++)
            cin >> niome[i];
        for(int i = 0; i < n ; i++)
            cin >> ken[i];
        
        sort(niome, niome+n);
        sort(ken, ken+n);
        
        int war = 0, dwar = n, i, j, start;
        
        i = 0, j = 0;
        while(i < n)
        {
            if( niome[i] < ken[j] )
                dwar--, i++;
            else
                i++, j++;
        }
         i = n-1, j = n-1, start = 0;
         
        while(i >= 0 && j >= start )
        {
            if(niome[i] > ken[j])
                i--, war++, start++;
            else
                i--, j--;
                
        }
         
        cout << "Case #" << cnt++ << ": " << dwar << " " << war << endl;
        
    }
    return 0;
}
