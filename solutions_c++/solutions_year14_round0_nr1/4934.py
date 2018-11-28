#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream inFile ("A-small-attempt0.in");
    ofstream outFile("A-small-attempt0.out");
    
    int cases;
    int ans1;
    int ans2;
    int cards1[4][4];
    int cards2[4][4];
    int inter;
    
    bool mis;
    bool found;
    
    if (inFile && outFile)
    {   
        inFile >> cases;
        
        for (int i = 0; i < cases; i++)
        {
            inter   = -1;
            mis     = false;
            
            inFile >> ans1;
            ans1   -= 1;
            
            for (int r = 0; r < 4; r++)
                for (int c = 0; c < 4; c++)
                    inFile >> cards1[r][c];
            
            inFile >> ans2;
            ans2   -= 1;
            
            for (int r = 0; r < 4; r++)
                for (int c = 0; c < 4; c++)
                    inFile >> cards2[r][c];
            
            for (int c = 0; c < 4 && !mis; c++)
            {
                found = false;
                
                for (int cc = 0; cc < 4 && !mis && !found; cc++)
                {
                    if (cards1[ans1][c] == cards2[ans2][cc])
                    {
                        found = true;
                        
                        if (inter != -1)
                            mis = true;
                        else
                            inter = cards1[ans1][c];
                        
                    }
                    
                }
                
            }
            
            outFile << "Case #" << i + 1 << ": ";
            
            if (mis)
                outFile << "Bad magician!" << endl;
            else if (inter == -1)
                outFile << "Volunteer cheated!" << endl;
            else
                outFile << inter << endl;
            
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
