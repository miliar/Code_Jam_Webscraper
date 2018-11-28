#include<fstream>
#include<iostream>

using namespace std;

int main()
{
    int t, T, i, j, s, f=0, c=0;
    char d[1002];
    ifstream fin("small.in");
    ofstream fout("small.out");
    fin>>T;
    for (t=1;t<=T;t++)
    {
        f=0;
        fin>>s;
        s++;
        for (i=0;i<s;i++)
            fin>>d[i];
        for (i=1;i<s;i++)
        {
            c=0;
            if (d[i]=='0')
                continue;
            for (j=0;j<i;j++)
                c+=(d[j]-'0');
            c+=f;
            if (c<i)
            {
                f+=i-c;
            }
        }
        fout<<"Case #"<<t<<": "<<f<<endl;
    }
}
