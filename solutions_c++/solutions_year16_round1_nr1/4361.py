#include<fstream>
#include<string.h>
#include<stdio.h>
#include<iostream>
using namespace std;
int main()
{
    int T,i,j,k,init,len;
    char S[1001],chs,chl,temp[1001];
    ifstream fin("A-large.in");
    ofstream fout("out2.in");
    fin>>T;
    for(i=-1;i<T;i++)
    {
        //cout<<i;
        fin.clear();
        fflush(stdin);
        j=-1;
        do{
            j++;
            fin.get(S[j]);
        }while(S[j]!='\n');
        S[j]=NULL;
        len=strlen(S);
        temp[len]=NULL;
        for(j=0;j<len;j++)
        {
            if(j==0)
                temp[j]=S[j];
            else
            {
                if(temp[0]<=S[j])
                {
                    for(k=j-1;k>=0;k--)
                        temp[k+1]=temp[k];
                    temp[0]=S[j];
                }
                else
                    temp[j]=S[j];
            }
        }
        if(i!=-1)
        fout<<"Case #"<<i+1<<": "<<temp<<endl;
    }
}
