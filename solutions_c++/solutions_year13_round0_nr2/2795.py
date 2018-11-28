//
//  tictac.cpp
//
//
//  Created by Abdallah on 4/12/13.
//
//
#include <fstream>
#include <iostream>

using namespace std;

main()
{
    ifstream fin;
    ofstream fout;
    
    fin.open("data.in.txt");
    fout.open("data.out.txt");
    
    int T,N,M, i,j,k,x;
    
    int board[100][100];
    fin>>T;
    
    for(i=0;i<T;i++)
    {
        fin>>N>>M;
        
        for(j=0;j<N;j++)
            for(k=0;k<M;k++)
                fin>>board[j][k];

        
        if(N==1 || M==1)
        {
            fout<<"Case #"<<i+1<<": YES"<<endl;
            continue;
        }
        
        int rowsOK = 0;
        bool NOflag = false;
        for(j=0;j<N;j++) //check row by row
        {
            int count=0;
            for(k=0;k<M;k++) //check if all row same height
            {
                if(board[j][k]==board[j][0]) count++;
            }
            if(count==M)
            {
                rowsOK++;
                continue;
            }
            
            //if row is not same height
            for(k=0;k<M;k++)
            {

                if(board[j][k]<2)
                {
                    for(x=0;x<N;x++)
                    {
                        if(board[x][k]!=board[j][k])
                        {
                            NOflag=true;
                        }
                    }
                }
            }
        }
        
        if(NOflag==true)
            fout<<"Case #"<<i+1<<": NO"<<endl;
        else
            fout<<"Case #"<<i+1<<": YES"<<endl;
        
    }
    
    fin.close();
    fout.close();
    
}