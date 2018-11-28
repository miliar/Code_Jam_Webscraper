#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int cases;
    
    cin >> cases;
    
    for(int i =0; i<cases; ++i)
    {
        vector<int> possibleCards;
        vector<int> matches;
        int row, count=0;
        int a[4][4];
        cin >> row;
        cin >> a[0][0] >> a[0][1] >> a[0][2] >> a[0][3];
        cin >> a[1][0] >> a[1][1] >> a[1][2] >> a[1][3];
        cin >> a[2][0] >> a[2][1] >> a[2][2] >> a[2][3];
        cin >> a[3][0] >> a[3][1] >> a[3][2] >> a[3][3];
        
        for(int j=0; j<4; ++j)
        {
            possibleCards.push_back(a[row-1][j]);
        }
        
        cin >> row;
        cin >> a[0][0] >> a[0][1] >> a[0][2] >> a[0][3];
        cin >> a[1][0] >> a[1][1] >> a[1][2] >> a[1][3];
        cin >> a[2][0] >> a[2][1] >> a[2][2] >> a[2][3];
        cin >> a[3][0] >> a[3][1] >> a[3][2] >> a[3][3];
        
        for(int k=0; k<4; ++k)
        {
            if(find(possibleCards.begin(), possibleCards.end(), a[row-1][k])!=possibleCards.end())
            {
                matches.push_back(a[row-1][k]);
                count++;
            }
        }
        
        if(count >1)
        {
            cout << "Case #" << i+1 << ": Bad magician!" << endl;
        }
        
        else if(count == 0)
        {
            cout << "Case #" << i+1 << ": Volunteer cheated!" << endl;
        }
        
        else
        {
            for(int w=0; w<matches.size(); ++w)
            {
                cout << "Case #" << i+1 << ": " << matches[w] << endl;;
            }
        }
    }
}