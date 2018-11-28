#include <cstdlib>
#include <iostream>
#include <sstream>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include "set"

using namespace std;

void TRVR(string &Wrd);

int main(int argc, char *argv[])
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int T;                           
    int A;
    int B;
    int Frst;
    int Rslt;
    int Hit;
    string FwdF;
    string RvrF;
    string FwdS;
    string RvrS;
    string Ans;

    cin >> T;
    for (int I =0;I < T; I ++){
        Hit = 0;
        cin >> A;
        cin >> B;
        
        Frst = sqrt(A);
        
        
        do {
            Rslt = 0;
            
            std::ostringstream ostrFrst; 
            ostrFrst << Frst;
            
            FwdS = ostrFrst.str();
            RvrS = FwdS;
            TRVR(RvrS);
            
            Rslt = Frst * Frst;
            
            std::ostringstream ostrRslt; 
            ostrRslt << Rslt; 
                    
            FwdF = ostrRslt.str();
            RvrF = FwdF;
            TRVR(RvrF);
                    
            
            if(Rslt >= A && Rslt <= B )
            {    
                if(FwdF == RvrF)
                {
                        if(FwdS == RvrS)
                        {
                               Hit = Hit + 1;
                        }
                }
            }
            
            Frst = Frst + 1;
        } while ( Rslt < B );
        
        
        cout << "Case #" << I+1 << ": " << Hit << endl;
    };
    

    return EXIT_SUCCESS;
}


void TRVR(string &Wrd)
{
        int i;
        char tmp;
        
        for (i=0; i<Wrd.length()/2; i++)
        {
        	tmp = Wrd[i];
        	Wrd[i] = Wrd[Wrd.length()-i-1];
        	Wrd[Wrd.length()-i-1] = tmp;
        }
} 
