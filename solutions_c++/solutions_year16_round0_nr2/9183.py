#include<fstream>
using namespace std;
int main()
{
    ifstream fin("B-large.in");
    ofstream fout("out.txt");
    long long int T,i,j,k,temp,J,n,flag=1,N;
    long int cont[101];
    char S[101],tmp;
    fin>>T;
    for(i=-1;i<T;i++)
    {
        cont[i]=0;
        flag=0;
        j=-1;
        do{
                j++;
                fin.get(S[j]);
        }while(S[j]!='\n');
        S[j]=NULL;
        for(j=0;S[j]!=NULL;j++);
        N=j;
        for(j=0;j<N;j++)
        {
            if(S[j]!=S[j+1]&&j!=N-1)
            {
                for(k=j;k>=0;k--)
                    if(S[k]=='+')
                        S[k]='-';
                    else
                        S[k]='+';
                j=0;
                cont[i]++;
            }
        }
        if(S[0]=='-')
            cont[i]++;
    }
    for(i=0;i<T;i++)
    {
        fout<<"Case #"<<i+1<<": "<<cont[i];
        if(i<T)
            fout<<endl;
    }
}
