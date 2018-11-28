#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool checked(vector<double> kevin, vector<double> naomi)
{
    while(naomi.size() >0)
    {
        if(kevin[kevin.size()-1] > naomi[naomi.size()-1])
        {
            return false;
        }
        else
        {
           kevin.pop_back();
           naomi.pop_back(); 
        }
    }
    return true;
}

int main()
{
    int cases = 0;
    int deceit, war;
    int blockCount;
    double temp;
    double naomiLie;
    double min;
    int minpos;
    int current;
    current=1;
    vector<double> naomiW;
    vector<double> kevinW;
    vector<double> naomiC;
    vector<double> kevinC;
    
    cin >> cases;
    for(int q=0;q<cases; q++)
    {
        cin >> blockCount;
        kevinC.resize(0);
        naomiC.resize(0);
        kevinW.resize(0);
        naomiW.resize(0);
        deceit = 0;
        war = 0;
        
        for(int x=0; x<blockCount; x++)
        {
            cin >> temp;
            naomiW.push_back(temp);
            naomiC.push_back(temp);
        }
        
        for(int x=0; x<blockCount; x++)
        {
            cin >> temp;
            kevinC.push_back(temp);
            kevinW.push_back(temp);
        }
        
        sort(naomiW.begin(), naomiW.end());
        sort(naomiC.begin(), naomiC.end());
        sort(kevinW.begin(), kevinW.end());
        sort(kevinC.begin(), kevinC.end());
               
        
        //war normal
        for(int x=0; x<blockCount; x++)
        {
            min = 99;
            for(int y=0; y<kevinW.size(); y++)
            {
                if(kevinW[y] > naomiW[x] && kevinW[y] < min)
                {
                    min = kevinW[y];
                    minpos=y;
                }
            } 
            if(min != 99)
            {
                kevinW.erase(kevinW.begin()+minpos);
            }
            else
            {
                kevinW.erase(kevinW.begin());
                war++;
            }
        }
        
        
        
        
        //cheating        
        for(int x=0; x<blockCount; x++)
        {
            if(!checked(kevinC, naomiC))
            {
                naomiLie = kevinC[kevinC.size()-1] - 0.0001;
                naomiC.erase(naomiC.begin());
                kevinC.pop_back();
            }
            else
            {
                deceit = naomiC.size();
                x=blockCount+1;
            }
        }
        
        cout << "Case #" << current << ": " << deceit << " " << war << endl;
        current++;
    }
    return 0;
}
