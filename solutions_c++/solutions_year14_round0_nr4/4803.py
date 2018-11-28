#include <iostream>
#include <fstream>
#include <vector>

using namespace std;


void sortBlocks(vector<double> &b);


int main()
{
    ifstream inFile ("D-small-attempt0.in");
    ofstream outFile("D-small-attempt0.out");
    
    int     cases;
    int     blocks;
    int     dPts;
    int     hPts;
    
    bool    foundGrtr;
    
    vector<double> nBlocks;
    vector<double> kdBlocks;
    vector<double> khBlocks;
        
    if (inFile && outFile)
    {   
        inFile >> cases;
                
        for (int c = 0; c < cases; c++)
        {
            dPts    = 0;
            hPts    = 0;
            
            inFile >> blocks;
            
            nBlocks.resize (blocks);
            kdBlocks.resize(blocks);
        
            for (int i = 0; i < blocks; i++)
                inFile >> nBlocks[i];
        
            for (int i = 0; i < blocks; i++)
                inFile >> kdBlocks[i];
        
            sortBlocks(nBlocks);
            sortBlocks(kdBlocks);
            
            khBlocks = kdBlocks;
        
            while (nBlocks.size() > 0)
            {                
                if (khBlocks[khBlocks.size() - 1] < nBlocks[nBlocks.size() - 1])
                {
                    foundGrtr = false;
                    
                    for (int i = khBlocks.size() - 2; i >= 0 && !foundGrtr; i--)
                    {
                        if (khBlocks[i] > nBlocks[nBlocks.size() - 1])
                        {
                            foundGrtr = true;
                            
                            khBlocks.erase(khBlocks.begin() + i);
                            
                        }
                        
                    }
                    
                    if (!foundGrtr)
                    {
                        hPts++;
                        khBlocks.pop_back();
                    }
                }
                
                khBlocks.pop_back();
                
                if (kdBlocks[kdBlocks.size() - 1] < nBlocks[nBlocks.size() - 1])
                {
                    dPts++;
                    kdBlocks.pop_back();
                }
                else
                    kdBlocks.erase(kdBlocks.begin());
                
                nBlocks.pop_back();
                            
            }
        
            outFile << "Case #" << c + 1 << ": " << dPts << " " << hPts << endl;
            
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


void sortBlocks(vector<double>& b)
{
    double  largest;
    double  temp;
    int     swap;
    
    for (int i = 0; i < b.size(); i++)
    {
        swap    = i;
        largest = b[i];
        
        for (int ii = i + 1; ii < b.size(); ii++)
        {
            if (largest < b[ii])
            {
                largest = b[ii];
                swap    = ii;
                
            }
            
        }
        
        if (swap != i)
        {
            temp    = b[i];
            b[i]    = b[swap];
            b[swap] = temp;
            
        }
        
    }
    
}
