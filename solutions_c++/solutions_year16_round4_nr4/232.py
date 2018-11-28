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

bool adj[5][5];
bool done[5];
int origins[5];
int nn;

bool bpm(int x)
{
    if(done[x])
        return false;
    done[x]=true;
    for(int i=0; i<nn; i++)
    {
        if(adj[x][i])
        {
            if(origins[i]==-1)
            {
                origins[i]=x;
                return true;
            }
            else if(bpm(origins[i]))
            {
                origins[i]=x;
                return true;
                
            }
        }
    }
    return false;
}

int runBPM(int _n)
{
    nn=_n;
    int ans = 0;
    memset(origins,-1,sizeof(origins));
    for(int i=0; i<nn; i++)
    {
        memset(done,0,sizeof(done));
        if(bpm(i))
            ans++;
    }
    return ans;
}

int mat[4][4];

bool isok(int num, int n)
{
    int i,j,k;
    memset(adj,0,sizeof(adj));
    for(i=0; i<n; i++)
    {
        for(j=0; j<n; j++)
        {
            if( (num&(1<<(i*n+j)))>0)
            {
                mat[i][j]=1;
                
            }
            else{
                mat[i][j]=0;
            }
            adj[i][j]=mat[i][j];
        }
    }
    if(runBPM(n)<n)
        return false;
    
    for(k=0; k<n; k++)
    {
        memset(adj,0,sizeof(adj));
        int target = 0;
        for(i=0;i<n; i++)
        {
            for(j=0; j<n; j++)
            {
                if(i==k)
                {
                    if(mat[i][j]>0)
                        target++;
                    continue;
                }
                if(!mat[k][j])
                    continue;
                adj[i][j]=mat[i][j];
            }
        }
        int v = runBPM(n);
        if(v==target)
            return false;
    }
    
    
    return true;
}

bool oklis[4][65536];
int score[65536];

void init()
{
    oklis[0][1]=true;
    int i,j;
    for(i=2; i<=4; i++)
    {
        for(j=0; j<(1<<(i*i)); j++)
        {
            oklis[i-1][j]=isok(j,i);
//            if(oklis[i-1][j] && i<=3)
//            {
//                cout << i << " " << j << endl;
//            }
        }
    }
    
    for(i=1; i<65536; i++)
    {
        if(i%2==1)
        {
            score[i]=1;
        }
        score[i]+=score[i/2];
    }
    return;
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
    
    init();
    
    while(ttt>0)
    {
        ct++;
        ttt--;
        
        int n,i,j,k;
        
        fin >> n;
        
        char c;
        
        k=0;
        
        for(i=0; i<n; i++)
        {
            for(j=0; j<n; j++)
            {
                fin >> c;
                if(c=='1')
                {
                    k+=(1<<(i*n+j));
                }
            }
        }
        
        int ret = n*n;
        
        for(i=0; i<(1<<(n*n)); i++)
        {
            if(oklis[n-1][i] && (k&i)==k)
            {
                if(score[i]-score[k]<ret)
                    ret=score[i]-score[k];
            }
        }
        
        
        cout << "Case #" << ct << ": ";
        fout << "Case #" << ct << ": ";
        
        
        cout << ret;
        fout << ret;
        
        
        fout << endl;
        cout << endl;
        
    }
    
    
    return 0;
}

