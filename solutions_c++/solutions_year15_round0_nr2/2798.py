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

int lis[10000];

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
        
        fin >> n;
        
        int i,j,k,ans;
        
        ans = 0;
        
        for(i=0; i<n; i++)
        {
            fin >> lis[i];
            if(lis[i]>ans)
                ans=lis[i];
        }
        
        for(k=ans-1; k>=1; k--)
        {
            j = 0;
            
            for(i=0; i<n; i++)
            {
                if(lis[i]%k==0)
                {
                    j+=lis[i]/k-1;
                    
                }
                else
                {
                    j+=lis[i]/k;
                }
            }
            if(j+k < ans)
                ans=j+k;
        }
        
                // cout << endl;
        
        
        cout << "Case #" << ct << ": ";
        fout << "Case #" << ct << ": ";
        
        
        cout << ans;
        fout << ans;
        
        
        
        
        
        fout << endl;
        cout << endl;
        
    }
    
    
    return 0;
}

