#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream fin;
    fin.open("A-small-attempt1.in");
    ofstream fout;
    fout.open("output.out");
    int t;
    fin>>t;
    int z[4][4],x[4][4];
    for(int k=0;k<t;++k)
    {
        int a,b;
        fin>>a;
        for(int i=0;i<4;++i)
            for(int j=0;j<4;++j)
                fin>>z[i][j];
        fin>>b;
        for(int i=0;i<4;++i)
            for(int j=0;j<4;++j)
                fin>>x[i][j];
        int same=0,ans;
        a--,b--;
        for(int i=0;i<4;++i)
            for(int j=0;j<4;++j)
                if(z[a][i]==x[b][j])
                    ++same,ans=z[a][i];
        fout<<"Case #"<<k+1<<": ";
        if(same==0)fout<<"Volunteer cheated!"<<endl;
        else if(same==1)fout<<ans<<endl;
        else fout<<"Bad magician!"<<endl;
    }
    fin.close();
    fout.close();
    return 0;
}
