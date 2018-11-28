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

int ret[51][51];

int main(void)
{
    int ttt=0;
    fin >> ttt;
    int ct = 0;
    
    
    cout.precision(9);
    fout.precision(9);
    
    cout << "HELLO" <<  " " << ttt << endl;
    
    
    
    while(ttt>0)
    {
        ct++;
        ttt--;
        
        int i,j,k;
        
        
        string s;
        fin >> s;
        
        int n = s.size();
        
        memset(ret,0,sizeof(ret));
        
        for(k=2; k<=n; k++)
        {
            for(i=0; i+k<=n; i++)
            {
                if(s[i]==s[i+k-1])
                {
                    ret[i][k]=ret[i+1][k-2]+1;
                }
                else{
                    ret[i][k]=ret[i+1][k-2];
                }
                for(j=2; j<k; j+=2)
                {
                    int l = ret[i][j]+ret[i+j][k-j];
                    if(l>ret[i][k])
                        ret[i][k]=l;
                }
            }
        }
        
        
        
        cout << "Case #" << ct << ": ";
        fout << "Case #" << ct << ": ";
        
        cout << 5*n-(n/2-ret[0][n])*5;
        fout << 5*n-(n/2-ret[0][n])*5;
        
        cout << endl;
        fout << endl;
        
        
        
        
        
    }
    
    
    return 0;
}

