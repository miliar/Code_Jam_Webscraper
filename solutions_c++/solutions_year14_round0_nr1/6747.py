#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
using namespace std;

int main (void)
{
    ifstream cin ("A-small-attempt0.in");
    ofstream cout ("out.txt");
    
    int t;
    cin >> t;
    
    for (int i = 0; i < t; i++)
    {
        vector<int> r1, r2;
        
        int wr1, wr2;
        
        cin >> wr1;
        wr1--;
        
        for (int j = 0; j < 4; j++)
        {
            for (int k = 0; k < 4; k++)
            {
                int p;
                cin >> p;
                if (j == wr1)
                    r1.push_back(p);
            }
        }
        
        cin >> wr2;
        wr2--;
        
        for (int j = 0; j < 4; j++)
        {
            for (int k = 0; k < 4; k++)
            {
                int p;
                cin >> p;
                if (j == wr2)
                    r2.push_back(p);
            }
        }
        
        sort(r1.begin(), r1.end());
        sort(r2.begin(), r2.end());
        
        vector<int> inter(4);
        vector<int>::iterator it;
        it = set_intersection(r1.begin(), r1.end(), r2.begin(), r2.end(), inter.begin());
        inter.resize(it-inter.begin());
        
        cout << "Case #" << i+1 << ": ";
        if (inter.size() == 0)
            cout << "Volunteer cheated!" << endl;
        else if (inter.size() > 1)
            cout << "Bad magician!" << endl;
        else
            cout << inter[0] << endl;
    }
          
    while (true) {}  
    return 0;
}
