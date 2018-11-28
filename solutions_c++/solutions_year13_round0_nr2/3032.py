#include <iostream>
#include <fstream>
using namespace std;

int lawn[100][100];

bool checkPoint(int N,int M,int n,int m)
{
    bool flag = true;
    for(int i=0;i<M;i++)
    {
        if(lawn[n][i] > lawn[n][m])
        {
            flag = false;
            break;
        }
    }
    if(!flag)
    {
        for(int i=0;i<N;i++)
        {
            if(lawn[i][m] > lawn[n][m])
            {
                flag = false;
                break;
            }
            flag = true;
        }
    }
    return flag;
}

int main()
{
    ifstream datain("B-large.in");
    ofstream dataout("B-large.out");
    int T;
    datain>>T;
    for(int k=1;k<=T;k++)
    {
        int N,M;
        datain>>N>>M;
        for(int i=0;i<N;i++)
        {
            for(int j=0;j<M;j++)
            {
                datain>>lawn[i][j];
            }
        }
        bool flag = true;
        for(int i=0;i<N;i++)
        {
            for(int j=0;j<M;j++)
            {
                flag = checkPoint(N,M,i,j);
                if(!flag)
                    break;
            }
            if(!flag)
                break;
        }
        if(flag)
        {
            dataout<<"Case #"<<k<<": YES"<<endl;
        }
        else
        {
            dataout<<"Case #"<<k<<": NO"<<endl;
        }
    }

    return 0;
}
