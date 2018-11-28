#include<fstream>
using namespace std;
int main()
{
    ifstream fin;
    fin.open("B-large.in");
    ofstream fout;
    fout.open("output.txt");
    int U=1,T;
    fin>>T;
    while(T-->0)
    {
        int N,M;
        fin>>N>>M;
        int lawn[N][M],rowmax[N],columnmax[M];
        for(int i=0;i<M;i++)
        {
            columnmax[i]=0;
        }
        for(int i=0;i<N;i++)
        {
            int maxr=0;
            for(int j=0;j<M;j++)
            {
                fin>>lawn[i][j];
                maxr=max(maxr,lawn[i][j]);
                columnmax[j]=max(columnmax[j],lawn[i][j]);
            }
            rowmax[i]=maxr;
        }
        bool possible=true;
        for(int i=0;i<N;i++)
            {
                for(int j=0;j<M;j++)
                possible=possible&&(lawn[i][j]==min(rowmax[i],columnmax[j]));
                if(!possible) break;
            }
        if(possible)
            fout<<"Case #"<<U<<": YES"<<endl;
        else fout<<"Case #"<<U<<": NO"<<endl;
       U++;
    }
    return 0;
}
