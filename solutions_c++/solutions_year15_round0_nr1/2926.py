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
        
        char c;
        
        int ans = 0;
        
        int i,j;
        
        j=0;
        
        for(i=0; i<n; i++)
        {
            fin >> c;
            //cout << c << " ";
            j+=(c-'0');
            if(j<i+1)
            {
                j++;
                ans++;
            }
        }
        fin >> c;
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

