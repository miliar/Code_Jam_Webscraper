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
        
        int n,i,j,k;
        int ans = 0;
        map<string,int> words;
        vector<vector<int> > adjs;
        vector<int> empt;
        adjs.push_back(empt);
        string s;
        fin >> n;
        
        getline(fin,s);
        
        int m = 1;
        
        for(i=0; i<n; i++)
        {
            getline(fin,s);
            stringstream sin(s);
            string t;
            
            while( sin >> t)
            {
                j = words[t];
                if(j==0)
                {
                    words[t]=m;
                    
                    adjs.push_back(empt);
                    adjs[m].push_back(i);
                    m++;
                }
                else
                {
                    adjs[j].push_back(i);
                }
            }
        }
        
        ans = m;
        
        for(k=0; k<(1<<(n-2)); k++)
        {
            int tot = 0;
            
            for(i=1; i<m; i++)
            {
                bool is0 = false;
                bool is1 = false;
                
                for(j=0; j<adjs[i].size(); j++)
                {
                    if(adjs[i][j]==0)
                        is0=true;
                    else if(adjs[i][j]==1)
                        is1=true;
                    else{
                        if( (k&(1<<(adjs[i][j]-2)))>0)
                        {
                            is1=true;
                        }
                        else{
                            is0=true;
                        }
                    }
                }
                if(is0 && is1)
                    tot++;
            }
            if(tot<ans)
                ans=tot;
        }
        
        
        
        cout << "Case #" << ct << ": ";
        fout << "Case #" << ct << ": ";
        
        
        cout << ans;
        fout << ans;
        
        
        
        
        
        fout << endl;
        cout << endl;
        
    }
    
    
    return 0;
}

