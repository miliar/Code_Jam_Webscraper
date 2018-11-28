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
    int cases, r1, r2, cnt = 1;
    cin >> cases;
    
    while(cases--)
    {
        set<int> s;
        int num, common = 0, res;
        cin >> r1;
        for(int i = 1; i <= 4; i++)
            for(int j = 1; j <= 4; j++)
            {
                cin >> num;
                if(i == r1)
                    s.insert(num);
            }
            
        cin >> r2;
        for(int i = 1; i <= 4; i++)
            for(int j = 1; j <= 4; j++)
            {
                cin >> num;
                
                if(i == r2 && s.find(num) != s.end())
                    common++, res = num;
            }
        
        if(common > 1)
            cout << "Case #" << cnt << ": Bad magician!\n";
        else if(common == 0)
            cout << "Case #" << cnt << ": Volunteer cheated!\n";
        else
            cout << "Case #" << cnt << ": " << res << endl;
    
        cnt++;    
    }
    
    return 0;
}
