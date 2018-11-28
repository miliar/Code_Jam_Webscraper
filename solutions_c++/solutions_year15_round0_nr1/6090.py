#include <iostream>
#include <fstream>
#include <cstring>

using namespace std;

int main()
{
    int t,smax,count,n,res;
    char st[1100];
    ifstream fin("A-large.in");
    ofstream fout("output.txt");
    fin>>t;
    for(int q=1;q<=t;q++)
    {
        count=0;
        res=0;
        fin>>smax;
        fin>>st;
        n=strlen(st);
        if(n==1)
        fout<<"Case #"<<q<<": 0\n";
        else
        {
            count=st[0]-'0';
            for(int i=1;i<n;i++)
            {
                if(count<i)
                {
                    res=res+(i-count);
                    count=i;
                    count=count+(st[i]-'0');
                }
                else
                {
                    count=count+(st[i]-'0');
                }
            }
            fout<<"Case #"<<q<<": "<<res<<"\n";
        }
    }
    return 0;
}
