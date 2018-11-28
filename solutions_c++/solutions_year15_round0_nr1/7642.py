#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <cstring>
#include <set>
using namespace std;

int t, sMax, aux, rez;
string s;

int main()
{
    
    cin >> t;
    
    for (int i = 1; i <= t; i++)
    {
        cin >> sMax;
        cin >> s;
        
        rez = 0;
        aux = int(s[0]) - 48;
        
        for (int j = 1; j < int(s.size()); j++)
        {
            int shyness = int(s[j]) - 48;
            if (aux < j)
                rez += (j - aux),
                aux = j;
            aux += shyness;
        }
        
        cout << "Case #" << i << ": " << rez << "\n";
    }
    
    return 0;
}