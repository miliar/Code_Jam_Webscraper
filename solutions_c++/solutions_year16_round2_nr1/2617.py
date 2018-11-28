//
//  main.cpp
//  Problem1
//
//  Created by Tanu on 4/30/16.
//  Copyright © 2016 Tanu Singhal. All rights reserved.
//

#include <iostream>
#include <string.h>
#include <stdio.h>

using namespace std;

int main(int argc, const char * argv[]) {
    int T;
    cin>>T;
    
    for(int i=0;i<T;i++)
    {
        char s[2002];
        cin>>s;
        
        int numTwos= 0, numZeros = 0, numFours = 0, numSixes = 0, numEights = 0;
        int len = 0;
        for(int i=0; s[i]!=0;i++)
        {
            len++;
            if(s[i] == 'W')
            {
                numTwos++;
            }
            else if(s[i] == 'Z')
            {
                numZeros++;
            }
            else if (s[i] == 'U')
            {
                numFours++;
            }
            else if (s[i] == 'X')
            {
                numSixes++;
            }
            else if (s[i] == 'G')
            {
                numEights++;
            }
        }
        

        int numAs;
        
        if(numTwos > 0)
        {
            int numW =  numTwos;
            int numO = numTwos;
            int numT = numTwos;
            for(int i=0; s[i]!=0;i++)
            {
                if(s[i] == 'W' && numW > 0)
                {
                    s[i] = 'A';
                    numAs++;
                    numW --;
                }
                else if(s[i] == 'O' && numO > 0)
                {
                    s[i] = 'A';
                    numAs++;
                    numO --;
                }
                else if(s[i] == 'T' && numT > 0)
                {
                    s[i] = 'A';
                    numAs++;
                    numT --;
                }
                
                if(numT == 0 && numO == 0 && numW == 0)
                    break;
            }
        }
        
        if(numSixes > 0)
        {
            int numS =  numSixes;
            int numI = numSixes;
            int numX = numSixes;
            
            for(int i=0; s[i]!=0;i++)
            {
                if(s[i] == 'S' && numS > 0)
                {
                    s[i] = 'A';
                    numAs++;
                    numS --;
                }
                else if(s[i] == 'I' && numI > 0)
                {
                    s[i] = 'A';
                    numAs++;
                    numI --;
                }
                else if(s[i] == 'X' && numX > 0)
                {
                    s[i] = 'A';
                    numAs++;
                    numX --;
                }
                
                if(numS == 0 && numI == 0 && numX == 0)
                    break;
            }
        }
        
        if(numZeros > 0)
        {
            int numZ =  numZeros;
            int numE = numZeros;
            int numR = numZeros;
            int numO = numZeros;
            
            for(int i=0; s[i]!=0;i++)
            {
                if(s[i] == 'Z' && numZ > 0)
                {
                    s[i] = 'A';
                    numAs++;
                    numZ --;
                }
                else if(s[i] == 'E' && numE > 0)
                {
                    s[i] = 'A';
                    numAs++;
                    numE --;
                }
                else if(s[i] == 'R' && numR > 0)
                {
                    s[i] = 'A';
                    numAs++;
                    numR --;
                }
                else if(s[i] == 'O' && numO > 0)
                {
                    s[i] = 'A';
                    numAs++;
                    numO --;
                }
                
                if(numZ == 0 && numE == 0 && numR == 0 && numO == 0)
                    break;
            }
        }
        
        if(numFours > 0)
        {
            int numF =  numFours;
            int numU = numFours;
            int numR = numFours;
            int numO = numFours;
            
            for(int i=0; s[i]!=0;i++)
            {
                if(s[i] == 'F' && numF > 0)
                {
                    s[i] = 'A';
                    numAs++;
                    numF --;
                }
                else if(s[i] == 'U' && numU > 0)
                {
                    s[i] = 'A';
                    numAs++;
                    numU --;
                }
                else if(s[i] == 'R' && numR > 0)
                {
                    s[i] = 'A';
                    numAs++;
                    numR --;
                }
                else if(s[i] == 'O' && numO > 0)
                {
                    s[i] = 'A';
                    numAs++;
                    numO --;
                }
                
                if(numF == 0 && numU == 0 && numR == 0 && numO == 0)
                    break;
            }
        }
        
        if(numEights > 0)
        {
            int numE =  numEights;
            int numI = numEights;
            int numG = numEights;
            int numH = numEights;
            int numT =  numEights;
            
            for(int i=0; s[i]!=0;i++)
            {
                if(s[i] == 'E' && numE > 0)
                {
                    s[i] = 'A';
                    numAs++;
                    numE --;
                }
                else if(s[i] == 'I' && numI > 0)
                {
                    s[i] = 'A';
                    numAs++;
                    numI --;
                }
                else if(s[i] == 'G' && numG > 0)
                {
                    s[i] = 'A';
                    numAs++;
                    numG --;
                }
                else if(s[i] == 'H' && numH > 0)
                {
                    s[i] = 'A';
                    numAs++;
                    numH --;
                }
                else if(s[i] == 'T' && numT > 0)
                {
                    s[i] = 'A';
                    numAs++;
                    numT --;
                }
                
                if(numE == 0 && numI == 0 && numG == 0 && numH == 0 && numT == 0)
                    break;
            }
        }
        
        int numFives = 0, numThrees = 0, numSevens = 0, numOnes = 0;
        
        for(int i=0; s[i]!=0;i++)
        {
            if(s[i] == 'F')
            {
                numFives++;
            }
            else if(s[i] == 'H')
            {
                numThrees++;
            }
            else if(s[i] == 'S')
            {
                numSevens++;
            }
            else if(s[i] == 'O')
            {
                numOnes++;
            }
        }
        
        if(numFives > 0)
        {
            int numF =  numFives;
            int numI = numFives;
            int numV = numFives;
            int numE = numFives;
            
            for(int i=0; s[i]!=0;i++)
            {
                if(s[i] == 'F' && numF > 0)
                {
                    s[i] = 'A';
                    numAs++;
                    numF --;
                }
                else if(s[i] == 'I' && numI > 0)
                {
                    s[i] = 'A';
                    numAs++;
                    numI --;
                }
                else if(s[i] == 'R' && numV > 0)
                {
                    s[i] = 'A';
                    numAs++;
                    numV --;
                }
                else if(s[i] == 'O' && numV > 0)
                {
                    s[i] = 'A';
                    numAs++;
                    numV --;
                }
                
                if(numF == 0 && numI == 0 && numV == 0 && numE == 0)
                    break;
            }
        }
        
        int numNines = 0;
        
        for(int i=0; s[i]!=0;i++)
        {
            if(s[i] == 'I')
            {
                numNines++;
            }
        }
        
        cout<<"Case #"<<i+1<<": ";
        while(numZeros > 0)
        {
            cout<<"0";
            numZeros--;
        }
        while(numOnes > 0)
        {
            cout<<"1";
            numOnes--;
        }
        while(numTwos > 0)
        {
            cout<<"2";
            numTwos--;
        }
        while(numThrees > 0)
        {
            cout<<"3";
            numThrees--;
        }
        while(numFours > 0)
        {
            cout<<"4";
            numFours--;
        }
        while(numFives > 0)
        {
            cout<<"5";
            numFives--;
        }
        while(numSixes > 0)
        {
            cout<<"6";
            numSixes--;
        }
        while(numSevens > 0)
        {
            cout<<"7";
            numSevens--;
        }
        while(numEights > 0)
        {
            cout<<"8";
            numEights--;
        }
        while(numNines > 0)
        {
            cout<<"9";
            numNines--;
        }
        cout<<endl;
    }
    
    return 0;
}
