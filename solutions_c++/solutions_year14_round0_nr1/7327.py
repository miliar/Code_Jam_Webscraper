#include <iostream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <map>
#include <cmath>

using namespace std;

int main()
{
    
    int n;
    cin>>n;
    
    for (int i=0; i<n; i++)
    {
        int ans1;
        cin>>ans1;
        
        vector<vector<int> > cards1(4,vector<int>(4,0));
        
        for (int j=0; j<4; j++)
        {
            for (int k=0; k<4; k++)
            {
                cin>>cards1[j][k];
            }
        }
        
        int ans2;
        cin>>ans2;
        
        vector<vector<int> > cards2(4,vector<int>(4,0));
        
        for (int j=0; j<4; j++)
        {
            for (int k=0; k<4; k++)
            {
                cin>>cards2[j][k];
            }
        }
        
        vector<int> possibleResults;
        
        for (int j=1; j<=16; j++)
        {
            if ( find(cards1[ans1-1].begin(),cards1[ans1-1].end(),j) != cards1[ans1-1].end() &&
                 find(cards2[ans2-1].begin(),cards2[ans2-1].end(),j) != cards2[ans2-1].end() )
            {
                possibleResults.push_back(j);                                   
            }
        }
        
        if (possibleResults.size() == 0)
        {
           cout << "Case #" << i+1 << ": Volunteer cheated!" << endl;
        }
        else if (possibleResults.size() == 1)
        {
           cout << "Case #" << i+1 << ": " << possibleResults[0] << endl;
        }
        else
        {
           cout << "Case #" << i+1 << ": Bad magician!" << endl;
        }
        
    }
};


