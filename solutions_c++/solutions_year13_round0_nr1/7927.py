/* 
 * File:   main.cpp
 * Author: pegasus
 *
 * Created on April 13, 2013, 1:27 AM
 */

#include <cstdlib>
#include <iostream>
#include <stdio.h>
#include <vector>
#include <memory.h>
#include <math.h>
#include <algorithm>
#include <sstream>
#include <map>
#include <cmath>
using namespace std;

/*
 * 
 */
int main(int argc, char** argv) {

    freopen("input.txt","r",stdin);
    freopen("out.in","w",stdout);
   
    
    int times ;
    
    cin>>times ;
    
    for (int t= 1 ;t <= times ;t++)
    {
        
        vector <string> board ;
        board.resize(4);
        for (int i=0 ;i<4 ;i++)
        {
            cin>>board[i];
        }
        
        bool dotFound =false;
          bool wining=true;
         
        
        for (int i=0 ;i<4 ;i++)
        {
         wining=true;
         char player='N';   
            for (int j=0 ;j<3 ;j++)
        {
                
                if (board[i][j]=='.')
                {
                    dotFound =true;
                    wining =false;
                    break;
                }
                if (board[i][j]=='T')
                {
                 
                    if (player !='N' && board[i][j+1]!=player )
                    {
                        wining =false;
                        
                        break;
                    }
                    
                    continue;
                
                }
                if (board[i][j]!=board[i][j+1] &&board[i][j+1]!='T' )
                {
                    wining=false;
                    break;
                }
                player =board[i][j];
        
            }
        
            if (wining)
            {
        
                cout<<"Case #"<<t<<": "<<player<<" won"<<endl;        
                break;
            }
        
        }
        
          if (wining)continue;
          
           for (int i=0 ;i<4 ;i++)
        {
         wining=true;
         char player='N';   
            for (int j=0 ;j<3 ;j++)
        {
                
                if (board[j][i]=='.')
                {
                    dotFound =true;
                    wining =false;
                    break;
                
                }
                
                if (board[j][i]=='T')
                {
                
                    if (player !='N' && board[j][i+1]!=player )
                    {
                        wining =false;
                        
                        break;
                    }
                    
                    continue;
                
                    
                }
                    
                if (board[j][i]!=board[j+1][i]&&board[j+1][i]!='T')
                {
                    wining=false;
                    break;
                }
                player =board[j][i];
        }
        
            if (wining)
            {
        cout<<"Case #"<<t<<": "<<player<<" won"<<endl;        
        break;
            }
         
        
        }
        
          
          if (wining) continue;
          
          
        if (  (board[0][0]=='X'||board[0][0]=='T') && (board[1][1]=='X'||board[1][1]=='T') && (board[2][2]=='X'||board[2][2]=='T' ) && (board[3][3]=='X'||board[3][3]=='T')  )
        {
        cout<<"Case #"<<t<<": "<<"X"<<" won"<<endl;
        }
        else if ( (board[0][3]=='X'||board[0][3]=='T') && ( board[1][2]=='X'||board[1][2]=='T' ) &&  ( board[2][1]=='X'||board[2][1]=='T' ) && ( board[3][0]=='X'||board[3][0]=='T' )  )
        {
        cout<<"Case #"<<t<<": "<<"X"<<" won"<<endl;
            
        }
          
       
           else if (  ( board[0][3]=='O'||board[0][3]=='T' ) && (board[1][2]=='O'||board[1][2]=='T' ) && ( board[2][1]=='O'||board[2][1]=='T' )&& ( board[3][0]=='O'||board[3][0]=='T') )
        {
        cout<<"Case #"<<t<<": "<<"O"<<" won"<<endl;
            
        }
        
       
           else if ( ( board[0][0]=='O'||board[0][0]=='T' ) && ( board[1][1]=='O'||board[1][1]=='T' ) && ( board[2][2]=='O'||board[2][2]=='T' ) && ( board[3][3]=='O'||board[3][3]=='T' ) )
        {
       cout<<"Case #"<<t<<": "<<"O"<<" won"<<endl;
        }    
        
           else
           {
               if (dotFound)
               {
       cout<<"Case #"<<t<<": "<<"Game has not completed"<<endl;
                   
               }
               else
               {
       cout<<"Case #"<<t<<": "<<"Draw"<<endl;
                   
               }
           }
        
    }
    
    return 0;
}

