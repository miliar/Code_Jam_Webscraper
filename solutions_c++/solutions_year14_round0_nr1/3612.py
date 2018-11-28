#include <iostream>
#include <fstream>
using namespace std;
int main()
{
    ifstream fin("A-small-attempt0.in");
    ofstream fout("A-small-attempt0.out");
    int a[5][5],b[5][5],i,j,k,n,m,t,cnt,ans;
    fin>>t;
    for (k=1;k<=t;k++)
    {
        fin>>n;
        for (i=0;i<4;i++)
            for (j=0;j<4;j++)
            fin>>a[i][j];
        fin>>m;
        for (i=0;i<4;i++)
                for (j=0;j<4;j++)
            fin>>b[i][j];
        cnt=0;
        ans=0;
        for (i=0;i<4;i++)
            for (j=0;j<4;j++)
            if (a[n-1][i]==b[m-1][j]) {cnt++; ans=a[n-1][i];}
            fout<<"Case #"<<k<<": ";
        if (cnt==0) fout<<"Volunteer cheated!"<<endl;
        if (cnt==1) fout<<ans<<endl;
        if (cnt>1)  fout<<"Bad magician!"<<endl;
        
        
    }

    
return 0;    
}
