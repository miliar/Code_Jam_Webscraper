#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <math.h>
using namespace std;

int ans1,ans2;
int deck1[4][4];
int deck2[4][4];
int res;

int check()
{
    int response=0;
    
    int counter = 0;
    int number = 0;
    
    for (int i=0; i<4; i++)
    {
        for (int j=0; j<4; j++)
        {
            if (deck1[ans1][i] == deck2[ans2][j])
            {
                counter++;
                number = deck1[ans1][i];
                break;
            }
        }
    }
    
    if (counter == 0)
    {
        response = 0;
    }
    
    else if (counter == 1)
    {
        response = number;
    }
    
    else
    {
        response = -1;
    }
    
    return response;
}

int main ()
{
    vector<int> data;
    ifstream infile ("/Users/diego/Desktop/fairAndSquare/data.in");
    ofstream outFile ("/Users/diego/Desktop/fairAndSquare/data.out");
    
    int cases;
    
    if (infile.is_open() && outFile.is_open())
    {
        infile >> cases;
        
        for(int c=0;c<cases;c++)
        {
            infile >> ans1;
            for (int i=0; i<4; i++)
            {
                for (int j=0; j<4; j++)
                {
                    infile >> deck1[i][j];
                }
            }
            
            infile >> ans2;
            for (int i=0; i<4; i++)
            {
                for (int j=0; j<4; j++)
                {
                    infile >> deck2[i][j];
                }
            }
            
            ans1--;ans2--;
            
            res = check();
            
            if (res == -1)
            {
                outFile << "Case #" << c+1 << ": Bad magician!" << endl;
            }
            
            else if (res == 0)
            {
                outFile << "Case #" << c+1 << ": Volunteer cheated!" << endl;
            }
            
            else
            {
                outFile << "Case #" << c+1 << ": " << res << endl;
            }
            
            
        }
        
        infile.close();
        outFile.close();
    }
    else cout << "Unable to open file";
    
    return 0;
}














