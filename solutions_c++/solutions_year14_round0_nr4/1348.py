#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>
#include <iterator>

using namespace std;
int main()
{
    int cases;
    cin >> cases;
    
    for(int i =0; i<cases; ++i)
    {
        int numBlocks;
        cin >> numBlocks;
        vector<double> naomiBlocks;
        vector<double> kenBlocks;
        vector<double> kenBlocks2;
        vector<double> naomiBlocks2;
        double temp;
        int cheatScore = 0;
        int realScore = 0;
        
        for(int j=0; j<numBlocks; ++j)
        {
            cin >> temp;
            naomiBlocks.push_back(temp);
        }
        
        for(int j=0; j<numBlocks; ++j)
        {
            cin >> temp;
            kenBlocks.push_back(temp);
        }
        
        sort(naomiBlocks.begin(), naomiBlocks.end());
        sort(kenBlocks.begin(), kenBlocks.end());
        
        auto it3=naomiBlocks.begin();
        auto it4 = kenBlocks.begin();
        
        naomiBlocks2 = naomiBlocks;
        kenBlocks2 = kenBlocks;
        
        while(it3!=naomiBlocks.end() && it4!=kenBlocks.end())
        {
            if(*it3 > *it4)
            {
                cheatScore++;
                it3++;
                it4++;
            }
         
            else
            {
                if(it4 == kenBlocks.begin()+kenBlocks.size()-1)
                {
                    kenBlocks.pop_back();
                    it3++;
                }
                
                else
                {
                    kenBlocks.pop_back();
                    it3++;
                }
            }
        }
        
        sort(naomiBlocks2.begin(), naomiBlocks2.end(), greater<double>());
        sort(kenBlocks2.begin(), kenBlocks2.end(), greater<double>());

        auto it5=naomiBlocks2.begin();
        auto it6 = kenBlocks2.begin();
        
        while(it5!=naomiBlocks2.end() && it6!=kenBlocks2.end())
        {
            if(*it5 > *it6)
            {
                realScore++;
                it5++;
                kenBlocks2.pop_back();
                
            }
            
            else
            {
                it5++;
                it6++;
            }
        }
        
        cout << "Case #" << i+1 << ": " << cheatScore << " " << realScore << endl;
    }
}