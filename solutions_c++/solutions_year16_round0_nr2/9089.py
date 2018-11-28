//#include<iostream>
#include<fstream>
//#include<math.h>
//#include<conio.h>
//#include<stdio.h>
using namespace std;
int main()
{
    ifstream fin("B-large.in");
    ofstream fout("B-largeout.in");
    long long int T,i,j,k,temp,J,n, flag=1,N;
    long int *cont;
    char S[101],tmp;
    fin>>T;
    cont=new long int [T];
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
        //cout<<S<<endl;
        for(j=0;j<N;j++)
        {
            if(S[j]!=S[j+1]&&j!=N-1)
            {
                for(k=j;k>=0;k--)
                    if(S[k]=='+')
                        S[k]='-';
                    else
                        S[k]='+';
                /*for(k=0;k<j/2;k++)
                {
                    tmp=S[k];
                    S[k]=S[N-k-1];
                    S[N-k-1]=tmp;
                }*/
                cont[i]++;
                //cout<<"S:"<<S<<"\ncont:"<<cont[i]<<endl<<endl;
                j=0;
            }
        }
        if(S[0]=='-')
            cont[i]++;
        //cout<<i<<endl<<cont[i]<<endl;
    }
    for(i=0;i<T;i++)
    {
        //cout<<"Case #"<<i+1<<": "<<cont[i];
        fout<<"Case #"<<i+1<<": "<<cont[i];
        if(i<T)
            fout<<endl;
            //cout<<endl;
    }
    delete cont;
    fin.close();
    fout.close();


}
