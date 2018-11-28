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
        
        int n;
        
        fin >> n;
        
        
        
        
        cout << "Case #" << ct << ": ";
        fout << "Case #" << ct << ": ";
        
        
        if(n==0)
        {
            cout << "INSOMNIA" << endl;
            fout << "INSOMNIA" << endl;
            continue;
        }
        
        int ans = 1;
        int score = 0;
        
        while(ans<1000)
        {
            int k = ans*n;
            while(k>0)
            {
                score|=(1<<(k%10));
                k/=10;
            }
            if(score==1023)
                break;
            ans++;
        }
        if(ans==1000)
        {
            for(int i=0; i<1000; i++)
                cout << "ERROR" << endl;
        }
        
        
        cout << ans*n;
        fout << ans*n;
        
        
        
        
        
        fout << endl;
        cout << endl;
        
    }
    
    
    return 0;
}

