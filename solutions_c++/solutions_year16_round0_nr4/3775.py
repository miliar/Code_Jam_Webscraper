#include<iostream>
#include<fstream>
#define cin ifile
#define cout ofile
using namespace std;


int main()
{
    ifstream ifile;
    ifile.open("D-small-attempt0.in");
    ofstream ofile;
    ofile.open("output1.txt");
    int t;
    cin>>t;

    for(int v=1;v<=t;v++)
    {
        int k,c,s;
        cin>>k>>c>>s;

        cout<<"Case #"<<v<<": ";
        for(int i=1;i<=k;i++)
            cout<<i<<" ";
        cout<<"\n";
    }

    return 0;
}
