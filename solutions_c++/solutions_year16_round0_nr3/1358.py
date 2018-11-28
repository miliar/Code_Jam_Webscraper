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

vector<int> plist;

int mods[32][11][10000]; //exponent,root, mod
int vals[32];
int witnesses[32];

int main(void)
{
    int ct = 1;
    cout << "Case #" << ct << ": ";
    fout << "Case #" << ct << ": ";
        
    cout << endl;
    fout << endl;
    
    int n = 32;
    int target=  500;
    
    int i,j,k;
    
    plist.push_back(2);
    
    for(i=3; i<1000; i++)
    {
        bool isok = true;
        for(j=0; j<plist.size(); j++)
        {
            if(i%plist[j]==0)
                isok=false;
        }
        if(isok)
            plist.push_back(i);
    }
    for(i=0; i<plist.size(); i++)
    {
        cout << i << " " << plist[i] << endl;
        for(j=2; j<=10; j++)
        {
            int curr = 1;
            for(k=0; k<n; k++)
            {
                mods[k][j][i]=curr;
                curr*=j;
                curr%=plist[i];
            }
        }
    }
    
    vals[0]=vals[n-1]=1;
    
    int found = 0;
    while(found<target)
    {
        bool isok = true;
        for(k=2; k<=10; k++)
        {
            bool gotwitness = false;
            for(i=0; i<plist.size(); i++)
            {
                int tot  =0;
                for(j=0; j<n; j++)
                {
                    tot+=vals[j]*mods[j][k][i];
                }
                if(tot%plist[i]==0)
                {
                    gotwitness=true;
                    witnesses[k]=plist[i];
                    break;
                }
            }
            if(!gotwitness)
            {
                isok=false;
                break;
            }
        }
        if(isok)
        {
            found++;
            for(i=n-1; i>=0; i--)
            {
                cout << vals[i];
                fout << vals[i];
            }
            cout << " ";
            fout << " ";
            for(i=2; i<=10; i++)
            {
                cout << witnesses[i] << " ";
                fout << witnesses[i] << " ";
            }
            cout << endl;
            fout << endl;
        }
        vals[1]++;
        i=1;
        while(vals[i]==2)
        {
            vals[i]=0;
            vals[i+1]++;
            i++;
        }
        
    }
    
    
    
    
    
    return 0;
}

