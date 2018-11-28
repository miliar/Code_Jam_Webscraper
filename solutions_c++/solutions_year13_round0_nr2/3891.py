#include<fstream>
#include<iostream>
#include<string>
#include<cstring>
using namespace std;
int main()
{
int T,N,M;
char str[30];
cin>>str;
fstream fi,fo;
fi.open(str,fstream::in);
fo.open("output.txt",fstream::out);
fi>>T;

for (int k=0;k<T;k++)
{
    fi>>N;
    fi>>M;
    int A[N][M];
    int D[N][M];
    for(int i=0;i<N;i++)
    {
            for(int j=0;j<M;j++)
            {
                fi>>A[i][j];D[i][j]=100;
            }
    }int max=0;
    for(int i=0;i<N;i++)
    {
        max=A[i][0];
        for(int j=0;j<M;j++){max=max>A[i][j]?max:A[i][j];}
        for (int j=0;j<M;j++){D[i][j]=max;}
    }
    bool x=true;int i=0;
    for (i=0;i<M;i++)
    {
        int j=0;
        max=A[0][i];
        for(j=0;j<N;j++){max=max>A[j][i]?max:A[j][i];}
        for (j=0;j<N;j++){D[j][i]=max<D[j][i]?max:D[j][i];if(D[j][i]!=A[j][i]){break;}}
        if(j<N){break;}
    }
    if(i<M){fo<<"Case #"<<k+1<<": NO"<<endl;}
    else {fo<<"Case #"<<k+1<<": YES"<<endl;}
}
fi.close();
fo.close();
return (0);
}
