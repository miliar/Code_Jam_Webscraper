#include <iostream>
#include <fstream>
using namespace std;
int main()
{
    ifstream fin;
    fin.open("A-large.in");
    ofstream fout;
    fout.open("A-large.out");
    int n,i,j;
    int* smax= new int[100];
    int* sum= new int[100];
    int* toinvite= new int[100];
    string* people= new string[100];
    fin>>n;
    for(i=0;i<n;i++)
    {
        fin>>smax[i];
        fin>>people[i];
    }
    for(i=0;i<n;i++)
    {
        toinvite[i]=0;
        sum[i]=0;
    }
    for(j=0;j<n;j++)
    {
        for(i=0;i<smax[j];i++)
        {
            if(people[j][i]!=48)
            {
                sum[j]+=(int(people[j][i])-48);
                continue;
            }
            else if(sum[j]>(i))
            {
                continue;
            }
            else
            {
                sum[j]++;
                toinvite[j]++;
            }
        }
    }
    for(j=0;j<n;j++)
    {
        fout<<"Case #"<<j+1<<": "<<toinvite[j]<<"\n";
    }
}
