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

long long calc(int st, int mod, int len, int mult)
{
    long long ret = 0;
    
    for(int i=0; i<len; i++)
    {
        ret*=mult;
        ret+=(st+i)%mod;
    }
    return ret;
}

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
        
        int k,c,s;
        
        fin >> k >> c >> s;
        cout << "Case #" << ct << ": ";
        fout << "Case #" << ct << ": ";
        
        
        int i,j,ans;
        
        if(k>c*s)
        {
            cout << "IMPOSSILE";
            fout << "IMPOSSILE";
        }
        else{
        
            for(i=0; i<s && i*c<k; i++)
            {
                long long r = calc((i*c)%k,k,c,k)+1;
                cout <<r << " ";
                fout <<r << " ";
            }
            
        }
        
        
        
        fout << endl;
        cout << endl;
        
    }
    
    
    return 0;
}

