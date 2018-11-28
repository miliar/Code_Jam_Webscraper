#include <bits/stdc++.h>
#include <fstream>
#define ll long long
using namespace std;
int t,x,r,c;
int main()
{
    fstream fin("D-small-attempt3.in",ios::in);
    fstream fout("out.txt",ios::out);
    fin>>t;
    for(int j=1;j<=t;j++)
    {
        fin>>x>>r>>c;
        if(x==1)
            fout<<"Case #"<<j<<": "<<"GABRIEL"<<endl;
        else if(x==2)
        {
            if((r*c)%2==0)
                fout<<"Case #"<<j<<": "<<"GABRIEL"<<endl;
            else
                fout<<"Case #"<<j<<": "<<"RICHARD"<<endl;
        }
        else if(x==3)
        {
            if((r*c)%3==0 && r!=1 && c!=1)
                fout<<"Case #"<<j<<": "<<"GABRIEL"<<endl;
            else
                fout<<"Case #"<<j<<": "<<"RICHARD"<<endl;
        }
        else
        {
            if((r*c)==12 || (r*c)==16)
                fout<<"Case #"<<j<<": "<<"GABRIEL"<<endl;
            else
                fout<<"Case #"<<j<<": "<<"RICHARD"<<endl;
        }
    }
}
