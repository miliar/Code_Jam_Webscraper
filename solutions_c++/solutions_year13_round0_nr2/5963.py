#include <iostream>
#include <fstream>

using namespace std;

int N,M;
int lawn[100][100];
bool posbileR(int n,int row);
bool possibleC(int n,int col);
bool posbileR2(int n,int row);
bool possibleC2(int n,int col);
int main()
{
    ifstream fin("B-small-attempt1.in");
    ofstream fout("B-small-attempt1.out");
    int T;
    bool posb=true;
    fin >> T;
    
    for(int j=0;j<T;j++)
    {
            for(int i=0;i<100;i++)
            {
                    for(int j=0;j<100;j++)
                    {
                             lawn[i][j]=0;;
                    }
            }
            //cout << ">>>>>>>>" << j << " <<<<<<<<<<<<" << endl;
            posb = true;
            
            fin >> N >> M;
            
            for(int i=0;i<N;i++)
            {
                    for(int j=0;j<M;j++)
                    {
                            fin >> lawn[i][j];
                    }
            }
            
            for(int i=0;i<N;i++)
            {
                    for(int j=0;j<M;j++)
                    {//cout << lawn[i][j] << " " ;
                            if(!(posbileR(lawn[i][j],i) || possibleC(lawn[i][j],j))){posb = false; break;}
                    }
                    //cout << endl;
                    if(!posb)break;
            }
            
            if(posb)fout << "Case #" << j+1 << ": YES" << endl;
            else fout << "Case #" << j+1 << ": NO"<< endl;
            
    }
    return 0;
}

bool posbileR(int n,int row)
{
     if(N==1)return true;
     for(int i=0;i<N;i++)
     {
             if(lawn[row][i] > n)return false;
     }
     return true;
}

bool possibleC(int n,int col)
{
     if(M==1)return true;
     for(int i=0;i<M;i++)
     {
             if(lawn[i][col] > n)return false;
     }
     return true;
}

