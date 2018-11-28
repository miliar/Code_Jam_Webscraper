#include <iostream>
#include <string>
#include <fstream>
#include <algorithm>
using namespace std;

void megold(istream& in, ostream& out)
{
    int sor, osz;
    in>>sor>>osz;
    int kert[sor][osz];
    for(int i=0; i<sor; i++)
    {
        for(int j=0; j<osz; j++)
        {
            in>>kert[i][j];
        }
    }

    int sorMax[sor], oszMax[osz];
    for(int i=0; i<sor; i++)
    {
        int mx=0;
        for(int j=0; j<osz; j++)
        {
            mx=max(kert[i][j],mx);
        }
        sorMax[i]=mx;
    }
    for(int i=0; i<osz; i++)
    {
        int mx=0;
        for(int j=0; j<sor; j++)
        {
            mx=max(kert[j][i],mx);
        }
        oszMax[i]=mx;
    }

    /*for(int i=0; i<sor; i++) cout<<sorMax[i]<<endl;
    for(int i=0; i<osz; i++) cout<<oszMax[i]<<' ';
    cout<<endl;*/

    for(int i=0; i<sor; i++)
    {
        for(int j=0; j<osz; j++)
        {
            if(kert[i][j]!=sorMax[i] && kert[i][j]!=oszMax[j])
            {
                out<<"NO";
                return;
            }
        }
    }
    out<<"YES";
}

int main()
{
    ifstream in("B-large.in");
    ofstream out("lawn.out");
    int n;
    in>>n;
    string temp;
    getline(in, temp);
    for(int i=1; i<=n; i++)
    {
        out<<"Case #"<<i<<": ";
        megold(in, out);
        out<<endl;
    }
    in.close();
    out.close();

    return 0;
}

