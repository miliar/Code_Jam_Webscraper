//Ominous Omino

#include<iostream>
#include<fstream>
#include<string>

using namespace std;
int main()
{
    int testcases,n;
    int x,r,c;
    bool flag=0;
    ifstream fin("ominous_small.txt");
    ofstream fout("ominous_out1");
    fin>>testcases;
    for(int i=0;i<testcases;i++)
    {
        flag=0;
        fin>>x>>r>>c;
        if(r*c%x==0)
        {
            if(c>=(x-1) && r>=(x-1) )
                flag=1;
        }
        if(flag==0) fout<<"Case #"<<(i+1)<<": RICHARD"<<endl;
        else        fout<<"Case #"<<(i+1)<<": GABRIEL"<<endl;
    }
    fin.close();
    fout.close();
    return 0;
}
