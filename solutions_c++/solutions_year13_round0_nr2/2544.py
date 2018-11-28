#include <algorithm>  
#include <iostream>  
#include <iomanip>  
#include <fstream>  
#include <sstream>  
#include <string>  
#include <list>  
#include <queue>  
#include <set>  
#include <map>  
#include <cstdio>  
#include <cstdlib>  
#include <cctype>  
#include <cmath>  
using namespace std;  

#define MAX(a,b) (a>b)?a:b;
#define FOR(i,a,b) for(long i=(a);i<(b);++i)  
#define REP(i,n) FOR(i,0,n)  

int lawn[150][150];
int rowMax[150];
int colMax[150];

void populateMax(int n, int m)
{
    REP(i,n)
    {
        rowMax[i] = -1;
        REP(j,m)
        {
            rowMax[i] = MAX(lawn[i][j], rowMax[i]);
        }
    }
    
    REP(i,m)
    {
        colMax[i] = -1;
        REP(j,n)
        {
            colMax[i] = MAX(lawn[j][i], colMax[i]);
        }
    }
}

void markGood(int i, int j)
{
    if(lawn[i][j] > 0 )
        lawn[i][j] = -lawn[i][j];
}

bool isGood(int i, int j)
{
    return (lawn[i][j] < 0);
}

int getHeight(int i, int j)
{
    return (isGood(i,j) ? -lawn[i][j] : lawn[i][j]);
}

void markIfGoodRow(int r, int cols)
{
    int val = getHeight(r, 0);
    FOR(i,1,cols)
        if(val != getHeight(r,i))
            return;

    REP(i,cols)
        markGood(r,i);
}

void markIfGoodCol(int c, int rows)
{
    int val = getHeight(0 , c);
    FOR(i,1,rows)
        if(val != getHeight(i,c))
            return;

    REP(i,rows)
        markGood(i,c);
}


bool solveCase(int n, int m)
{
    populateMax(n,m);
    
    REP(i,n)
        markIfGoodRow(i,m);

    REP(j,m)
        markIfGoodCol(j,n);

    REP(i,n)
    {
        REP(j,m)
        {
            if(isGood(i,j))
                continue;
            else 
            {
                int val = getHeight(i,j);
                if((val >= rowMax[i]) or (val >= colMax[j]))
                    continue;
                else
                    return false;
            }
        }
    }
    return true;
}

int main(int argc, char** argv)
{
    if(argc < 3)
    {
        cout << "Args\n";
        return 1;
    }
    ifstream in;
    cout << "Reading " << argv[1] << endl;
    cout << "Writing " << argv[2] << endl;
    in.open(argv[1],ios::in);
    ofstream out;
    out.open(argv[2],ios::out);
    int N = 0;
    in>>N;
    cout << " Total  " << N <<endl;
    REP(caseN,N)
    {
        cout<<"solving case "<<caseN+1<<endl;
        int n = 0;
        int m = 0;
        in >> n >> m;
        
        REP(i,n)
            REP(j,m)
                in >> lawn[i][j];


        bool res = solveCase(n , m);

        out << "Case #"<<caseN+1<<": ";
        out << (res?"YES":"NO");
        
        out << endl;
    }
        
    in.close();
    out.close();
    return 0;
}
