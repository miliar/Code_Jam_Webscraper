#include<iostream>
#include<fstream>

using namespace std;

int main()
{
    ifstream fin;
    ofstream fout;
    fin.open("B-large.in");
    fout.open("lawnmower.txt");
    int max=0,i,j,k,T,M,N,A[100][100],B[100][100],flag;
    fin>>T;
    for(i=1;i<=T;i++)
    {
        flag=0;
        fin>>N>>M;
        for(j=0;j<N;j++)
        {
            for(k=0;k<M;k++)
            {
                fin>>A[j][k];
                B[j][k]=100;
            }
        }
        for(j=0;j<N;j++)
        {
            max=0;
            for(k=0;k<M;k++)
            {
                if(A[j][k]>max)
                max=A[j][k];
            }
            for(k=0;k<M;k++)
            {
                if(B[j][k]>=max)
                B[j][k]=max;
            }
        }
        for(k=0;k<M;k++)
        {
            max=0;
            for(j=0;j<N;j++)
            {
                if(A[j][k]>max)
                max=A[j][k];
            }
            for(j=0;j<N;j++)
            {
                if(B[j][k]>=max)
                B[j][k]=max;
            }
        }
        for(j=0;j<N;j++)
        {
            for(k=0;k<M;k++)
            {
               if(A[j][k]!=B[j][k])
               flag=1;
            }
        }
        if(flag==0)
        fout<<"Case #"<<i<<": YES\n";
        else if(flag==1)
        fout<<"Case #"<<i<<": NO\n";
    }
    fin.close();
    fout.close();
    return 0;
}
