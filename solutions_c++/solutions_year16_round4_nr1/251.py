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

bool cmp(pair<string,string> a, pair<string,string> b)
{
    return (a.second<b.second);
}

int comb(string a, string b)
{
    if(a.size()==0 || b.size()==0 || a==b)
        return 3;
    if(a!="S" && b!="S")
        return 0;
    if(a!="R" && b!="R")
        return 1;
    if(a!="P" && b!="P")
        return 2;
    cerr << "ERROR " << a << " " << b << endl;
    return 3;
}

string eval(int x)
{
    if(x==0)
    {
        return "P";
    }
    else if(x==1)
    {
        return "S";
    }
    else{
        return "R";
    }
}

bool solve(string s)
{
    if(s.size()==1)
        return true;
    string ret = "";
    for(int i=0; i<s.size(); i+=2)
    {
        if(s[i]==s[i+1])
            return false;
        if(s[i]!='P' && s[i+1]!='P')
        {
            ret+="R";
        
        }
        if(s[i]!='R' && s[i+1]!='R')
        {
            ret+="S";
        }
        if(s[i]!='S' && s[i+1]!='S')
        {
            ret+="P";
        }
    }
    return solve(ret);
}

string hack(int p, int r, int s)
{
    string curr ="";
    int i;
    for(i=0; i<p; i++)
    {
        curr+="P";
    }
    for(i=0; i<r; i++)
    {
        curr+="R";
    }
    for(i=0; i<s; i++)
    {
        curr+="S";
    }
    do
    {
        if(solve(curr))
        {
            return curr;
        }
    } while(next_permutation(curr.begin(),curr.end()));
    return "IMPOSSIBLE";
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
        
        int p,r,s;
        
        fin >> n >> r >> p >> s;
        
//        cout << "Case #" << ct << ": ";
//        cout << hack(p,r,s) << endl;
        
        vector<pair<string,string> > lis;
        
        for(i=0; i<p; i++)
        {
            lis.push_back(make_pair("P","P"));
        }
        for(i=0; i<r; i++)
        {
            lis.push_back(make_pair("R","R"));
        }
        for(i=0; i<s; i++)
        {
            lis.push_back(make_pair("S","S"));
        }
        
        string ret = "";
        
        while(lis.size()>1)
        {
            //cout << lis.size() << endl;
            p = r = s =0;
            
            sort(lis.begin(),lis.end(),cmp);
            
            for(i=0; i<lis.size(); i++)
            {
                if(lis[i].first=="P")
                    p++;
                else if(lis[i].first=="R")
                    r++;
                else
                    s++;
            }
            
            vector<pair<string,string> > lis1;
            
            if(p>r+s || r>p+s || s>p+r)
            {
                //cout << "BREAK " << p << " " << r << " " << s << endl;
                break;
            }
            
            int x = (p+r-s)/2;
            int y = (p+s-r)/2;
            int z = (r+s-p)/2;
            
            //cout << x << " " << y << " " << z << endl;
            
            int cap[4];
            cap[0]=x;
            cap[1]=y;
            cap[2]=z;
            cap[3]=0;
            
            for(i=0; i<lis.size(); i++)
            {
                if(lis[i].first=="")
                    continue;
                j=i+1;
                
                while(j<lis.size() && cap[comb(lis[i].first,lis[j].first)]<=0)
                    j++;
                
                if(j==lis.size())
                {
                    cerr << "ERROR " << j << " " << lis.size() << endl;
                }
                
                k = comb(lis[i].first,lis[j].first);
                cap[k]--;
                lis1.push_back(make_pair(eval(k),lis[i].second+lis[j].second));
                lis[j].first="";
                lis[i].first="";
            }
            lis=lis1;
            
        }
        
        if(lis.size()>1)
        {
            ret="IMPOSSIBLE";
        }
        else{
            ret=lis[0].second;
        }
        
        
        
        cout << "Case #" << ct << ": ";
        fout << "Case #" << ct << ": ";
        
        cout << ret << endl;
        fout << ret << endl;
        
        
        
        
        
    }
    
    
    return 0;
}

