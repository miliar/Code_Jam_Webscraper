#include <vector>
#include <string>
#include <stdlib.h>
#include <math.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <sstream>
#include <map>
#include <ctime>
#include <cassert>

using namespace std;

ofstream fout("../../../output.txt");
ifstream fin("../../../input.txt");

int px[4] = {1,0,-1,0};
int py[4] = {0,1,0,-1};

int board[100][100];

int main(void)
{
    int ttt;
    fin >> ttt;
    int ct = 0;
    string s;
    
    cout.precision(9);
    fout.precision(9);
    
    cout << "HELLO" <<  " " << ttt << endl;
    
    
    
    while(ttt>0)
    {
        ct++;
        ttt--;
        
        double f,x;
        int n;
        int r,c;
        
        fin >> r >> c;
        
        int i,j,k;
        
        int ans = 0;
        
        bool isok = true;
        
        for(i=0; i<r; i++)
        {
            for(j=0; j<c; j++)
            {
                char cc;
                fin >> cc;
                if(cc=='^')
                {
                    board[i][j]=2;
                }
                else if(cc=='v')
                    board[i][j]=0;
                else if(cc=='<')
                    board[i][j]=3;
                else if(cc=='>')
                    board[i][j]=1;
                else
                    board[i][j]=4;
            }
        }
        
        for(i=0;i<r; i++)
        {
            for(j=0; j<c; j++)
            {
                if(board[i][j]==4)
                    continue;
                
                int tot1,tot2;
                tot1=tot2=0;
                
                for(k=0; k<4; k++)
                {
                    
                    int cx=i+px[k];
                    int cy=j+py[k];
                    
                    while(cx>=0 && cx<r && cy>=0 && cy<c)
                    {
                        if(board[cx][cy]==4)
                        {
                            cx+=px[k];
                            cy+=py[k];
                        }
                        else
                            break;
                    }
                    
                    if(cx>=0 && cx<r && cy>=0 && cy<c)
                    {
                        tot1++;
                        if(k==board[i][j])
                            tot2++;
                    }
                    
                    
                }
                
                if(tot1==0)
                    isok=false;
                else if(tot1>0 && tot2==0)
                    ans++;
                
                
                //cout << i << " " << j << " " << tot1 << " " << tot2 << " " << ans << endl;
            }
        }
        
        
        cout << "Case #" << ct << ": ";
        fout << "Case #" << ct << ": ";
        
        if(isok)
        {
            cout << ans;
            fout << ans;
        }
        else{
            cout << "IMPOSSIBLE";
            fout << "IMPOSSIBLE";
        }
        
        
        
        
        fout << endl;
        cout << endl;
        
    }
    
    
    return 0;
}

