#include<fstream>
#include<iostream>
#include<cmath>
#include<cstring>
using namespace std;

int main()
{
    ifstream fin("B.in");
    ofstream fout("out.txt");
    int t;
    fin>>t;
    for(int pp=0;pp<t;pp++)
    {
        int a,b,k;
        fin>>a>>b>>k;
        int ans = 0;
        for(int i=0;i<a;i++)
        {
            for(int j=0;j<b;j++)
            {
                int x = i&j;
                if(x<k)
                {
                    ans++;
                }
            }
        }
        fout<<"Case #"<<pp+1<<": ";
        fout<<ans<<endl;
    }
    fin.close();
    fout.close();
    return 0;
}
