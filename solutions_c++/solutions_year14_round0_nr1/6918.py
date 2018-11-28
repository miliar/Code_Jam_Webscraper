#include <algorithm>
#include <iostream>
#include <vector>
#include <string>
#include <map>
using namespace std;

int main()
{
    
    int tests_count;
    cin >> tests_count;
    
    for (size_t i = 0; i < tests_count; ++i)
    {
        vector < vector <int> > m(2, vector <int>(16));
        vector <int> picks(2);
        for (size_t j = 0; j < 2; ++j)
        {
            cin >> picks[j];
            for (size_t k = 0; k < 16; ++k)
            {
                cin >> m[j][k];
            }
        }
        
        int p1 = picks[0] * 4,
            p2 = picks[1] * 4;
        map <int, int> same;
        int key = 0;
        for (size_t j = p1 - 4; j < p1; ++j)
        {
            for (size_t k = p2 - 4; k < p2; ++k)
            {
                if (m[0][j] == m[1][k])
                {
                    key = m[0][j];
                    same.insert(make_pair(key, 0));
                }
            }
        }
        
        size_t sz = same.size();
        string rs = "Case #" + to_string(i + 1) + ": ";
        if (sz == 0)
        {
            rs += "Volunteer cheated!";
        }
        else if (sz == 1)
        {
            rs += to_string(key);
        }
        else
        {
            rs += "Bad magician!";
        }
        
        cout << rs << endl;
    }
    
    return 0;
}