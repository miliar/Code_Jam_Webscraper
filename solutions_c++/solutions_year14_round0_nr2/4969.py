#include <iostream>
#include <iomanip>
#include <fstream>

using namespace std;

int main()
{
    ifstream inFile ("B-large.in");
    ofstream outFile("B-large.out");
    
    int     cases;
    double  farmCost;
    double  farmProf;
    double  winCost;
    double  winTime;
    double  gain;
    
    if (inFile && outFile)
    {   
        inFile >> cases;
        
        for (int i = 0; i < cases; i++)
        {
            inFile >> farmCost;
            inFile >> farmProf;
            inFile >> winCost;
            
            winTime = 0.d;
            gain    = 2.d;
            
            while (winCost / gain > (winCost / (gain + farmProf)) + (farmCost / gain))
            {
                winTime += farmCost / gain;
                gain += farmProf;
                
            }
            
            winTime += winCost / gain;
            
            outFile << "Case #" << i + 1 << ": " << setprecision(7) << fixed << winTime << endl;
            
        }
        
    }
    else
    {
        cout << "Failed to open files" << endl;
        
        return -1;
        
    }
    
    inFile.close();
    outFile.close();
    
    return 0;
    
}
