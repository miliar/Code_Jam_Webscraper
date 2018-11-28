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

bool cmp(pair<double,double> a, pair<double,double> b)
{
    if(a.first==b.first)
        return (a.second>b.second);
    return (a.first>b.first);
}

double ret[501][501][2];

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
        
        fin >> x >>  n;
        
        
        
        double ans = 0.0;
        
        int i,j,k;
        
        memset(ret,0,sizeof(ret));
        
        vector<pair<double,double> > lis1;
        vector<pair<double,double> > lis2;
        
        vector<double> p;
        vector<double> s;
        for(k=0; k<n; k++)
        {
            double y;
            fin >> y;
            p.push_back(y);
        }
        for(k=0; k<n; k++)
        {
            double y;
            fin >> y;
            s.push_back(y);
        }
        
        for(k=0; k<n; k++)
        {
            double y,z;
            
            y=p[k];
            z=s[k];
            if(y>0)
            {
                lis1.push_back(make_pair(z,y));
            }
            else{
                lis2.push_back(make_pair(z,-y));
            }
        }
        
        sort(lis1.begin(),lis1.end(),cmp);
        sort(lis2.begin(),lis2.end(),cmp);
        
        if(lis1.size()>0)
           ret[0][0][0] = (lis1[0].second)/(x-lis1[0].first);
        if(lis2.size()>0)
            ret[0][0][1] = (lis2[0].second)/(x-lis2[0].first);
        
        for(i=0; i<=lis1.size(); i++)
        {
            for(j=0; j<=lis2.size(); j++)
            {
                //cout << i << " " << j << " " << ret[i][j][0] << " " << ret[i][j][1] << endl;
                if(i==lis1.size() || ret[i][j][0]==0.0)
                {
                    ;
                }
                else{
                //case 0
                double d = ret[i][j][0]*lis1[i].first+lis1[i].second;
                double tm = ret[i][j][0];
                
                int c1 = i+1;
                
                while(c1<lis1.size() && lis1[c1].first*tm+lis1[c1].second<=d)
                    c1++;
                //c1 is next to catch
                if(c1<lis1.size())
                {
                    double dist = ((lis1[c1].first*tm + lis1[c1].second)-d)/(x-lis1[c1].first)+tm;
                    if(dist < ret[c1][j][0] || ret[c1][j][0]==0.0)
                    {
                        ret[c1][j][0]=dist;
                    }
                }
                else if(c1==lis1.size() && j==lis2.size())
                {
                    if(ret[i][j][0]<ans || ans==0.)
                        ans=ret[i][j][0];
                }
                if(j < lis2.size())
                {
                    double dist = (d + lis2[j].first*tm + lis2[j].second)/(x-lis2[j].first)+tm;
                    if(dist < ret[c1][j][1] || ret[c1][j][1]==0.)
                    {
                        ret[c1][j][1]=dist;
                    }
                }
                //swap
                }
                
                if(j==lis2.size() || ret[i][j][1]==0.0)
                    continue;
                //cout << "TEST " << endl;
                //case 1
                double d = ret[i][j][1]*lis2[j].first+lis2[j].second;
                double tm = ret[i][j][1];
                
                int c2 = j+1;
                
                while(c2<lis2.size() && lis2[c2].first*tm+lis2[c2].second<=d)
                    c2++;
                //cout << c2 << endl;
                //c2 is next to catch
                if(c2<lis2.size())
                {
                    double dist = ((lis2[c2].first*tm + lis2[c2].second)-d)/(x-lis2[c2].first)+tm;
                    if(dist < ret[i][c2][1] || ret[i][c2][1]==0.0)
                    {
                        ret[i][c2][1]=dist;
                    }
                }
                else if(c2==lis2.size() && i==lis1.size())
                {
                    if(ret[i][j][1]<ans || ans==0.)
                        ans=ret[i][j][1];
                }
                if(i < lis1.size())
                {
                    double dist = (d + lis1[i].first*tm + lis1[i].second)/(x-lis1[i].first)+tm;
                    if(dist < ret[i][c2][0] || ret[i][c2][0]==0.)
                    {
                        ret[i][c2][0]=dist;
                    }
                }
            }
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

