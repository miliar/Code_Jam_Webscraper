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

int vals[1000];
int lis[1000];
int mins[100];
int maxs[100];

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
        
        
        
        
        
        int ans = 0;
        
        int i,j,k;
        
        fin >> n >> k;
        
        
        memset(lis,0,sizeof(lis));
        memset(mins,0,sizeof(mins));
        memset(maxs,0,sizeof(maxs));
        
        for(i=0; i<n-k+1; i++)
        {
            fin >> vals[i];
            if(i>=1)
            {
                j=i-1+k;
                lis[j]=lis[i-1]+vals[i]-vals[i-1];
                if(lis[j]<mins[j%k])
                    mins[j%k]=lis[j];
                if(lis[j]>maxs[j%k])
                    maxs[j%k]=lis[j];
                //cout <<  j << " " << lis[j] << endl;
            }
        }
        
        long long totv = vals[0];
        vector<long long> diffs;
        
        for(i=0; i<k; i++)
        {
//            if(n==100 && k==50)
//                cout << mins[i] << " " << maxs[i] << endl;
            totv+=mins[i];
            diffs.push_back(maxs[i]-mins[i]);
        }
        sort(diffs.begin(),diffs.end());
        
        cout << totv <<  " " << k << endl;
        if(totv < 0)
        {
            //cout << (totv/k)*k << endl;
            totv-=(totv/k)*k;
            totv+=k;
            //cout << totv << endl;
        }
        if(totv<0)
        {
            totv+=100*k;
            cout << " ERRROR " << endl;
        }
        
        cout << diffs[0] << " " << diffs[1] << " " << diffs[k-1] << " " << totv << " " << k << endl;
        
        ans = diffs[diffs.size()-1];
        int todo = (totv%k);
        
        
        for(i=0; i<diffs.size(); i++)
        {
            while(diffs[i] < ans && todo>0)
            {
                diffs[i]++;
                todo--;
            }
        }
        
        if(todo>0)
            ans++;
        
        
        //sort(diffs.begin(),diffs.end());
        
        
        
        
        cout << "Case #" << ct << ": ";
        fout << "Case #" << ct << ": ";
        
        
        cout << ans;
        fout << ans;
        
        
        
        
        
        fout << endl;
        cout << endl;
        
    }
    
    
    return 0;
}

