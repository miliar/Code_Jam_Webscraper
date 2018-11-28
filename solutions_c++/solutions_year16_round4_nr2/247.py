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


double dp[2001][2001];

double calc(vector<double> lis)
{
    memset(dp,0,sizeof(dp));
    dp[0][0]=1.0;
    
    int i,j,k;
    
    for(i=0; i<lis.size(); i++)
    {
        //cout << lis[i] << " ";
        for(j=0; j<=i; j++)
        {
            dp[i+1][j]+=(1-lis[i])*dp[i][j];
            dp[i+1][j+1]+=lis[i]*dp[i][j];
        }
    }
    //cout << dp[lis.size()][lis.size()/2] << endl;
    return dp[lis.size()][lis.size()/2];
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
        
        int n,i,j,k;
        
        vector<double> lis;
        
        fin >> n >> k;
        
        double ret = 0.0;
        
        for(i=0; i<n; i++)
        {
            double d;
            fin >> d;
            lis.push_back(d);
            
        }
        
        sort(lis.begin(),lis.end());
        
       
        
        for(i=0; i<=k; i++)
        {
            vector<double> lis1;
            for(j=0; j<i; j++)
            {
                lis1.push_back(lis[j]);
            }
            j=lis.size()-1;
            while(lis1.size()<k)
            {
                lis1.push_back(lis[j]);
                j--;
            }
            double d = calc(lis1);
            if(d>ret)
                ret=d;
        }
        
        
        cout << "Case #" << ct << ": ";
        fout << "Case #" << ct << ": ";
        
        
        cout << ret << endl;
        fout << ret << endl;
        
        
        
    }
    
    
    return 0;
}

