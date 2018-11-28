#include <fstream>
#include <string>
#include <iostream>
#include <queue>
#include <list>
#include <algorithm>
#include <vector>
#include <stdio.h>
#include <deque>

using namespace std;


int main ()
{
    int t;
    
    freopen("A-small.txt","r",stdin);   
    freopen("Aoutput.txt","w",stdout);
    
    cin>>t;
    
    int firstAns = 0;
    int secAns = 0;
    int grid [4][4];
    bool firstPart [16];
    bool secPart [16];
    
    for (int trial=1;trial<=t;++trial)
    {
        for (int i=0;i<16;i++)
        {
            firstPart [i] = false;
            secPart [i] = false;
        }
        
        cin>>firstAns;
        firstAns--;
        for (int row=0;row<4;row++)
        {
            for (int col=0;col<4;col++)
            {
                cin>>grid[col][row];
            }    
        }
        
        //Set the booleans for all the numbers in the row of the first Ans as true
        for (int i=0;i<4;i++)
        {
            firstPart[grid[i][firstAns]-1] = true;    
            //cout<<"Set "<<grid[i][firstAns]<<"\n";
        }
        
        //Same for second part of trick
        cin>>secAns;
        secAns--;
        for (int row=0;row<4;row++)
        {
            for (int col=0;col<4;col++)
            {
                cin>>grid[col][row];
            }    
        }
        for (int i=0;i<4;i++)
        {
            secPart[grid[i][secAns]-1] = true;    
            //cout<<"Set "<<grid[i][secAns]<<"\n";
        }
        
        //Count number of possible final cards, and also get the final card
        int numCards = 0;
        int cardNum = 0;
        for (int i=0;i<16;i++)
        {
            if (firstPart[i] && secPart[i])
            {
             //cout<<"Here "<<i<<"\n";
             numCards++;
             cardNum = i+1;                 
            }    
        }
        
        if (numCards==0)
           cout<<"Case #"<<trial<<": Volunteer cheated!\n";
        else if (numCards>1)
             cout<<"Case #"<<trial<<": Bad magician!\n";
        else
            cout<<"Case #"<<trial<<": "<<cardNum<<"\n";
    }
    return 0;
}
