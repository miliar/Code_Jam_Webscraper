//
//  main.cpp
//  CodeJam
//
//  Created by Fahad Mansoor on 11/04/2015.
//
//

#include <iostream>
#include <stdlib.h>
using namespace std;

int toInt(char x)
{
    return x - 48;
}

void standingOvation(int T, int members,string sequence)
{
    int membersThatNeedHelp =0 ;
    int membersThatDontNeedHelp =0 ;
    int shynessAvailable = 0;
    int minShynessRequired = 0;
    int extraMembersRequired = 0;
    for (int i=0 ; i < sequence.length(); i++) {
        if ( toInt(sequence[i]) > 0    )
        {
            
            if ( shynessAvailable >= i)
            {
                membersThatDontNeedHelp  += toInt(sequence[i]);
                shynessAvailable += toInt(sequence[i]);
            }
            else
            {
                int shynessRequired = i - shynessAvailable;
                extraMembersRequired += shynessRequired;
                shynessAvailable += extraMembersRequired + toInt(sequence[i]) ;
                
            }
            
        }
    }
    
    
    cout<<"Case #"<<T<<": "<<extraMembersRequired<<endl;

}

int main(int argc, const char * argv[]) {
    // insert code here...
    freopen("input.txt", "r+", stdin);
    freopen("output.txt", "w+", stdout);
    int T =0,i = 0;
    
    cin >> T;
    
    while (i < T)
    {
        int members = 0;
        string sequence = "";
        cin >> members;
        cin>> sequence;
        standingOvation(i+1, members, sequence);
        
        i++;
    }
    return 0;
}
