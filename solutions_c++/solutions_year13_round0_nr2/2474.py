#include <cstdlib>
#include <fstream>
#include <vector>
using namespace std;

int main(int argc, char *argv[])
{
    ofstream fout("answers.out");
    ifstream fin("B-large.in");
    vector <string> results;
    int i,j,k,check=0,N,M,t,T;
    int F[100][100]={0};
    fin>>T;
    for(t=0;t<T;t++)
    {
        fin>>N>>M;
        for(i=0;i<N;i++)
        {
            for(j=0;j<M;j++)
            {
                fin>>F[i][j];
            }
        }
        for(i=0;i<N;i++)
        {
            for(j=0;j<M;j++)
            {
                check=0;
                for(k=0;k<M;k++)
                {
                    if(F[i][k]>F[i][j]){check=1;break;}
                }
                if(check==1)
                {
                   check=0;
                   for(k=0;k<N;k++)
                   {
                       if(F[k][j]>F[i][j]){check=1;break;}
                   }
                }
                if(check==1)
                {
                   results.push_back("NO");
                   break;
                }
            }
            if(j<M){break;}
        }
        if(i==N){results.push_back("YES");}
    }
    for(t=0;t<T;t++)
    {
        fout<<"Case #"<<t+1<<": "<<results[t]<<endl;
    }
    system("PAUSE");
    return EXIT_SUCCESS;
}
