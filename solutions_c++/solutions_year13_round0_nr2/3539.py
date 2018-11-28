#include <iostream>
#include <fstream>
using namespace std;
ifstream in ("lm.in"); ofstream out ("lm.out");

int lawn[100][100];
int patt[100][100];
bool isDone[100][100];
bool hgh[101];

void dbPrintLawn(int,int);
bool eval(int,int);
int main()
{
    int t;
    in >> t;
    for(int cs = 1; cs <= t;cs++)
    {
        int n,m;
        in >> n >> m;
        cerr << "Case #" << cs << ' ' << n << ' ' << m <<'\n';
        int maxH = 0;
        for(int i = 0; i < n; i++)
            for(int j = 0; j < m; j++)
            {
                in >> patt[i][j];
                hgh[patt[i][j]]=true;
                if(patt[i][j]>maxH)maxH=patt[i][j];
            }
        for(int k = maxH; k > 0; k--)
        {
            if(!hgh[k])continue;
            //Lines
            for(int i = 0; i < n; i++)
            {
                bool canBeM=true;
                for(int j = 0; j < m; j++)
                    if(patt[i][j]>k){canBeM=false;break;}
                if(canBeM)
                {
                    for(int j = 0; j < m; j++)
                        lawn[i][j]=k;
                }
            }
            //Cols
            for(int j = 0; j < m; j++)
            {
                bool canBeM=true;
                for(int i = 0; i < n; i++)
                    if(patt[i][j]>k){canBeM=false;break;}
                if(canBeM)
                for(int i = 0; i < n; i++)lawn[i][j]=k;
            }
            //dbPrintLawn(n,m);
        }
        if(eval(n,m))
            out << "Case #" << cs << ": YES\n";
        else
            out << "Case #" << cs << ": NO\n";
        for(int i = 0; i <= maxH; i++)hgh[i]=false;
        for(int i = 0; i < n; i++)
            for(int j = 0; j < m; j++)
                lawn[i][j]=0;
    }
}

void dbPrintLawn(int n,int m)
{
    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < m; j++)
            cerr << lawn[i][j] << ' ';
        cerr << '\n';
    }
    cerr << '\n';
}
bool eval(int n, int m)
{
    for(int i = 0; i < n; i++)
        for(int j = 0; j < m; j++)
            if(lawn[i][j]!=patt[i][j])return false;
    return true;
}
