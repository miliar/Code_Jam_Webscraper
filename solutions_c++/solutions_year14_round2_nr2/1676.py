#include <iostream>
#include <vector>
#include <cstring>
#include <algorithm>
#include <string>
#include <cmath>
#include <cstdlib>
#include <map>
#include <stack>

using namespace std;

    
int main()
{
    int n, cases, ctr = 1, A, B, K, res;
    cin >> cases;
    
    while(cases--)
    {
        cin >> A >> B >> K;
        res = 0;
        for(int i = 0; i < A; i++)
        {
            for(int j = 0; j < B; j++)
            {
                if((i&j) >= 0 && (i&j) < K)
                    res++;
            }
        }
        cout << "Case #" << ctr++ << ": " << res << endl;
    }     
    
    return 0;
}
