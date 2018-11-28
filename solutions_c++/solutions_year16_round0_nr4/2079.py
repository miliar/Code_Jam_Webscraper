#include <iostream>

using namespace std;
typedef unsigned long long int ullint;

int main()
{
    int T, cont = 0;
    
    cin >> T;

    while(T--)
    {
        ullint k, c, s, n = 1;
        
        cin >> k >> c >> s;
        
        // small solution s == k
        if(s < k) {
            cout << "Case #" << ++cont << ": " << "IMPOSSIBLE" << " " << endl;
            continue ;
        }
        
        for(ullint i = 0; i < c-1; i++)
            n *= k;
        
        cout << "Case #" << ++cont << ": ";
        
        for(ullint i = 0; i < s; i++)
            cout << (i*n)+1 << " ";
        
        cout << endl;
    }
        
return 0;
}
