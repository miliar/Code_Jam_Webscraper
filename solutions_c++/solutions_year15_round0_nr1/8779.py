// JoD attempt for round 1, problem a

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(){
    
    ifstream infile;
    ofstream outfile;
    
    int nCases, currCase, Smax, NatS; 
    int nStanding, nRequired, nFriends, newFriends;
    string  Sdist;
    
    int i,j;
    
    infile.open ("A-large.in");
    outfile.open ("A-large.out");
    
    infile >> nCases;
    
    // Case loop
    for(currCase = 0; currCase < nCases; currCase++ )
    {
        // Grab the max shyness
        infile >> Smax;
        // Grab the string of S's
        infile >> Sdist;
    
    		//Reset numbers
    		nStanding = 0;
    		nFriends = 0;
    		
        for(nRequired = 0; nRequired <= Smax; nRequired++)
        {
        
        	NatS = Sdist[nRequired] - '0';
										        	
        	if(nStanding >= nRequired)
        	{
        		nStanding += NatS;
        	}
        	else
        	{
        		newFriends = nRequired - nStanding;
        		nFriends += newFriends;
        		nStanding += NatS + newFriends;
        	}
        }
    
    
    // Output to file
    outfile << "Case #" << currCase + 1 << ": " << nFriends  << endl;
    
        
    }
    
    infile.close();
    outfile.close();
    return 0;
}

