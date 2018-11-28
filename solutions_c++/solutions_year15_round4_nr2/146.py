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
    return (a.second<b.second);
}

double EPS = 1e-9;

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
        
        double ans = 0.0;
        
        bool isok = false;
        
        int i,j,k;
        
        double p,q;
        vector<pair<double,double> > lis;
        
        double v,x,rtot;
        
        fin >> v >> x;
        
        rtot=0.0;
        
        double eqtot = 0.0;
        
        for(i=0; i<n; i++)
        {
            fin >> p >> q;
            rtot+=p;
            lis.push_back(make_pair(p,q));
            if(q==x)
                eqtot+=p;
        }
        sort(lis.begin(),lis.end(),cmp);
        
        double mn,mx;
        
        mn = v/rtot;
        
        mx = 1e8;
        if(lis[0].second==x || lis[lis.size()-1].second==x)
        {
            isok=true;
            ans=v/eqtot;
        }
        else if(lis[0].second<=x && lis[lis.size()-1].second>=x)
        {
            isok=true;
            while(mx > mn*(1+EPS))
            {
                double curr = sqrt(mx*mn);
                
                double num,denom;
                num=denom=0.0;
                
                for(i=0; i<lis.size(); i++)
                {
                    p=0.0;
                    if(denom + curr*lis[i].first <= v)
                    {
                        p=curr;
                    }
                    else
                    {
                        p=(v-denom)/lis[i].first;
                    }
                    denom+=p*lis[i].first;
                    num+=p*lis[i].second*lis[i].first;
                }
                
                //cout << curr << " " << num << " " << denom << " " << num/denom << endl;
                
                if(num/denom > x)
                {
                    mn=curr;
                    continue;
                }
                num=denom=0.0;
                
                for(i=lis.size()-1; i>=0; i--)
                {
                    p=0.0;
                    if(denom + curr*lis[i].first <= v)
                    {
                        p=curr;
                    }
                    else
                    {
                        p=(v-denom)/lis[i].first;
                    }
                    denom+=p*lis[i].first;
                    num+=p*lis[i].second*lis[i].first;
                }
                
               // cout << curr << " " << num << " " << denom << " " << num/denom << endl;
                
                if(num/denom < x)
                {
                    mn=curr;
                    continue;
                }
                mx=curr;
                continue;
            }
            ans=sqrt(mx*mn);
        }
        
        // cout << endl;
        
        
        cout << "Case #" << ct << ": ";
        fout << "Case #" << ct << ": ";
        
        if(isok)
        {
            
        cout << ans;
        fout << ans;
        }
        else{
            cout << "IMPOSSIBLE";
            fout << "IMPOSSIBLE";
        }
        
        
        
        
        fout << endl;
        cout << endl;
        
    }
    
    
    return 0;
}

