#include<iostream>
#include<fstream>
#include<map>
#include<stdlib.h>
#include<string.h>
#include<vector>
using namespace std;
int main()
{
    ifstream fin;
    ofstream fout;
    fin.open("input.txt");
    fout.open("ans.txt");
    int t,j,len,count[3000],i,a[100],n,k,max,i1;
    //bool arr[11];
    fin>>t;
    //cout<<t;

    for(j=1;j<=t;j++)
    {
        fin>>n;
        memset(count,0,sizeof(count));
        max=0;
        for(i=1;i<=2*n-1;i++)
        {
            for(i1=1;i1<=n;i1++)
            {
                fin>>a[i1];
                if(max<=a[i1]) max=a[i1];
                count[a[i1]]++;
            }

        }
        fout<<"Case #"<<j<<": ";
        for(i=1;i<=max;i++)
        {
           // cout<<count[i]<<" "<<i<<endl;
            if(count[i]%2!=0)
            fout<<i<<" ";
        }
        fout<<endl;

    }

    return 0;
}
