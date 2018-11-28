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

double rv[1000000];
int rcurr=  0;

double fact[101];

double choose[101][101];

void init()
{
    cout << "HI" << endl;
    double d = 0.0;
    
    for(int i=0; i<1000000; i++)
    {
        rv[i]=((double)rand())/((double)RAND_MAX);
    }
   
    fact[0]=1.0;
    for(int i=1; i<=100; i++){
        fact[i]=((double)i)*fact[i-1];
    }
    choose[0][0]=1.0;
    
    for(int i=1; i<=100; i++)
    {
        for(int j=0; j<=i; j++)
        {
            choose[i][j]=fact[i]/fact[j]/fact[i-j];
        }
    }
}

int parent[100];
vector<vector<int> > children;
int topsort[100];
bool ison[200];
int n;
double scores[100];
int counts[100];

vector<double> calcperms()
{
    vector<double> retv(n,0.0);
    //memset(scores,0,sizeof(scores));
    //memset(counts,0,sizeof(counts));
    
    double ret = 1.0;
    int retcount = 0;
    
    for(int kk=0; kk<n; kk++)
    {
        int k = topsort[kk];
        if(ison[k])
            continue;
        
        //counts[k]=0;
        
        
        if(parent[k]==-1 || ison[parent[k]])
        {
            
            
            retv[k]=counts[k];
        }
    }
    return retv;
}

bool contain(string a, string b)
{
    int i,j,k;
    
    for(i=0; i<=a.size()-b.size(); i++)
    {
        bool isok= true;
        for(j=0; j<b.size(); j++)
        {
            if(a[i+j]!=b[j])
                isok=false;
        }
        if(isok)
            return true;
    }
    return false;
}

vector<double> getprobs()
{
    vector<double> ret(n,0.0);
    ret=calcperms();
    double d= 0.0;
    
    for(int i=0; i<n; i++)
        d+=ret[i];
    for(int i=0; i<n; i++)
    {
        ret[i]/=d;
        if(i>0)
            ret[i]+=ret[i-1];
    }
    return ret;
}

int main(void)
{
    int ttt;
    fin >> ttt;
    int ct = 0;
    
    
    cout.precision(9);
    fout.precision(9);
    
    cout << "HELLO" <<  " " << ttt << endl;
    
    init();
    
    while(ttt>0)
    {
        ct++;
        ttt--;
        
        int i,j,k;
        
        
        
        fin >> n;
        
        children.clear();
        
        for(i=0; i<n; i++)
        {
            vector<int> empt;
            children.push_back(empt);
            ison[i]=false;
        }
        
        for(i=0; i<n; i++)
        {
            fin >> parent[i];
            parent[i]--;
            if(parent[i]>=0)
            {
                children[parent[i]].push_back(i);
            }
        }
        
        string names;
        fin >> names;
        
        int m;
        
        fin >> m;
        
        vector<string> words;
        
        for(i=0; i<m; i++)
        {
            string s;
            fin >> s;
            words.push_back(s);
            cout << s << endl;
        }
        
        
        int curr = 0;
        for(k=0; k<n; k++)
        {
            for(i=0; i<n; i++)
            {
                if(ison[i])
                    continue;
                bool isok = true;
                
                counts[i]=1;
                
                for(j=0; j<children[i].size(); j++)
                {
                    if(!ison[children[i][j]])
                        isok=false;
                    counts[i]+=counts[children[i][j]];
                }
                if(isok)
                {
                    topsort[curr]=i;
                    ison[i]=true;
                    curr++;
                }
            }
        }
        
//        for(i=0; i<n; i++)
//        {
//            cout << counts[i] << endl;
//        }
//        cout << curr << endl;
        
        vector<double> scores(m,0.0);
        
        for(int trials=0; trials<2500; trials++)
        {
           
            string hat = "";
            memset(ison,0,sizeof(ison));
            
            for(i=0; i<n; i++)
            {
                vector<double> pv = getprobs();
//                for(j=0; j<n; j++)
//                {
//                    cout << pv[j] << " ";
//                    
//                }
//                cout << endl;
                double r = rv[rcurr];
                rcurr++;
                rcurr%=1000000;
                for(j=0; j<n; j++)
                {
                    if(pv[j]>=r)
                        break;
                }
                if(j==n)
                    j--;
                while(pv[j]==0.0)
                    j--;
                ison[j]=true;
                hat+=names[j];
                //cout << j << " ";
            }
//            cout << endl;
            
            for(i=0; i<m; i++)
            {
                if(contain(hat,words[i]))
                    scores[i]+=1.0;
            }
            
            //cout << hat << endl;
            
        }
        
        
        
        
        
        cout << "Case #" << ct << ": ";
        fout << "Case #" << ct << ": ";
        
        for(i=0; i<m; i++)
        {
            cout << scores[i]/2500.0 << " ";
            fout << scores[i]/2500.0 << " ";
        }
        
        
        cout << endl;
        fout << endl;
        
        
        
        
        
    }
    
    
    return 0;
}

