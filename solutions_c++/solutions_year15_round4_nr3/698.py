#include <cstdlib>
#include <algorithm>
#include <vector>
#include <map>
#include <stack>
#include <queue>
#include <limits>
#include <iostream>
#include <set>
#include <cmath>
#include <iomanip>
#include <fstream>
#include <cstring>
#include <string>
using namespace std;
#define MAXN 4010
int T;
int N,conta;
vector<int> adj[MAXN],riga[MAXN];
map<string,int> compr;
int sol;
bool inglese[MAXN],francese[MAXN],rigab[MAXN];
ifstream fin("input.in");
ofstream fout("output.txt");

void parse(int i,bool ing, bool fra)
{
    string word="";
    string att="";
    getline(fin,att);

    int pos=0;
    while(pos<=att.size())
    {
        if(pos==att.size() || att[pos]==' ')
        {
            int idx;
            if(compr.count(word)==0) compr[word]=conta , idx=conta++;
            else idx=compr[word];
            //err<<word<<" "<<idx<<endl;
            riga[i].push_back(idx);
            adj[idx].push_back(i);
            inglese[idx]|=ing;
            francese[idx]|=fra;
            word="";
        }
        else word.push_back(att[pos]);

        pos++;
    }
}

/*void provaing(int i)
{
    for(auto r:adj[i])
        for(auto idx:riga[r])
    {
        if(idx==i || inglese[idx]) continue;
        inglese[idx]=true;
        provaing(idx);
    }
}

void provafra(int i)
{
    for(auto r:adj[i])
        for(auto idx:riga[r])
    {
        if(idx==i || francese[idx]) continue;
        francese[idx]=true;
        provafra(idx);
    }
}*/

void calcola(int pos)
{
    if(pos==N)
    {
        int parz=0;
        for(int i=0;i<conta;++i)
        {
            bool ing=false,fra=false;
            for(auto r:adj[i])
                if(rigab[r]) ing=true;
                else fra=true;
            if(fra && ing) parz++;
            //if(fra && ing) cerr<<i<<" ";
        }
        //cerr<<endl;
        sol=min(sol,parz);
        return;
    }
    if(pos==0) rigab[pos]=true , calcola(pos+1);
    else if(pos==1) rigab[pos]=false , calcola(pos+1);
    else
    {
        rigab[pos]=true;
        calcola(pos+1);
        rigab[pos]=false;
        calcola(pos+1);
    }
}

int main()
{


    fin>>T;
    for(int t=1;t<=T;++t)
    {

        fin>>N;
        conta=0;
        compr.clear();
        for(int i=0;i<MAXN;++i) adj[i].clear() , riga[i].clear();
        memset(inglese,false,sizeof inglese);
        memset(francese,false,sizeof francese);
        fin.ignore();
        parse(0,true,false);
        parse(1,false,true);

        for(int i=2;i<N;++i) parse(i,false,false);
        memset(rigab,false,sizeof rigab);
        /*for(int i=0;i<conta;++i)
        {
            for(auto a:adj[i]) cerr<<a<<" ";
            cerr<<endl;
        }*/
        /*for(int i=0;i<conta+1;++i)
        {
            if(inglese[i]) provaing(i);
            if(francese[i]) provafra(i);
        }*/

        sol=1000000000;
        calcola(0);

        fout<<"Case #"<<t<<": "<<sol<<"\n";

    }

}
