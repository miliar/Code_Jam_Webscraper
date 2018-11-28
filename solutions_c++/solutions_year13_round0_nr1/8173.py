#include <cstdlib>
#include <iostream>
#include "set"

using namespace std;

int main(int argc, char *argv[])
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int T;
    char chr;
    string str;
    int H=0;
    int V=0;
    int DL = 1;
    int DR = 1;
    string IH[4];
    
    string IDL[4];
    string IDR[4];
    
    string Win = "";
    int D = 0;
    
    string gtList[4][4];
        
    cin >> T;
    for (int I =0;I < T; I ++){
        
        Win = "";
        D = 0;
        
        for (int J = 0;J < 16; J ++){ 
            
            cin >> chr;
            str = chr;
            
            if(J==0)
            {
                V = 0;
                H = 0;
            }
            else
            {
                if(J%4 == 0)
                { V = V + 1; }                       
                H = J%4;
            }
            
            gtList[V][H] = str;
            
            if (str == ".")
            { D = 1; }
               
        };
        
        //H
            for (int A =0;A < 4; A ++)
            {
                for (int B =0;B < 4; B ++)
                {
                    if (gtList[A][B] != "T")
                    {
                        if(Win.empty() && B == 0)
                        {
                               if(gtList[A][B] != ".")
                               {
                                   Win = gtList[A][B];
                               }
                               
                        }
                        else
                        {
                            if(Win != gtList[A][B])                
                            {      
                                   Win = "";
                                   goto NxtH;
                                   
                            }
                        }
                    }
                    
                    if (Win != "" && B == 3)
                    {
                            goto CekWinner;
                    }
                } 
                
                NxtH:;
            } 

        //V
            for (int A =0;A < 4; A ++)
            {
                for (int B =0;B < 4; B ++)
                {
                    if (gtList[B][A] != "T")
                    {
                        if(Win.empty() && B == 0)
                        {
                               if(gtList[B][A] != ".")
                               {
                                   Win = gtList[B][A];
                               }
                               
                        }
                        else
                        {
                            if(Win != gtList[B][A])                
                            {      
                                   Win = "";
                                   goto NxtV;
                                   
                            }
                        }
                    }
                    
                    if (Win != "" && B == 3)
                    {
                            goto CekWinner;
                    }
                } 
                
                NxtV:;
            }   
            
        //L
            for (int A =0;A < 4; A ++)
            {
                if (gtList[A][A] != "T")
                    {
                        if(Win.empty() && A == 0)
                        {
                               if(gtList[A][A] != ".")
                               {
                                   Win = gtList[A][A];
                               }
                               
                        }
                        else
                        {
                            if(Win != gtList[A][A])                
                            {      
                                   Win = "";
                            }
                        }
                    }
                    
                    if(Win != "" && A == 3)
                    { goto CekWinner; } 
            }           
        
        //R
            for (int A =0;A < 4; A ++)
            {
                for (int B =0;B < 4; B ++)
                {
                    if(A+B == 3)
                    {
                           
                           if (gtList[A][B] != "T")
                            {
                           
                                if(Win.empty() && A == 0 && B == 3)
                                {
                                       if(gtList[A][B] != ".")
                                       {
                                           Win = gtList[A][B];
                                       }
                                       
                                }
                                else
                                {
                                    if(Win != gtList[A][B])                
                                    {      
                                           Win = "";
                                           goto NxtR;
                                           
                                    }
                                }
                            }
                    }
                } 
                    
                NxtR:;
            } 
        
        CekWinner:;
           
        if (Win != "")
        {
                cout << "Case #" << (I+1) << ": " << Win << " won" << endl;
        }
        else
        {
            if(D > 0)
            {
                 cout << "Case #" << (I+1) << ": Game has not completed" << endl;
            }
            else
            {
                cout << "Case #" << (I+1) << ": Draw" << endl;
            }
        }
    };

    return EXIT_SUCCESS;
}
