#include <fstream>

using namespace std;

int main()
{
    fstream fin;
    fstream fout;
    fin.open("input.in",ios::in);
    fout.open("output.out",ios::out);
    int t,k,c,s,j;
    fin>>t;
    for(int i=1;i<=t;i++)
    {
        fin>>k>>c>>s;
        fout<<"Case #"<<i<<": ";
        for(j=1;j<k;j++)
            fout<<j<<" ";
        fout<<j;
        fout<<endl;
    }
    return 0;
}
