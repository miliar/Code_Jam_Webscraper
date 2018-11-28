#include<iostream>
#include<string>
#include<fstream>
using namespace std;

int main()
{
    int t,i,j,k=0,x,o,T,d;
    string s[5];
    bool f;
    ifstream in ("input.txt");
    ofstream out ("output.txt");
    in>>t;
    while(t>k)
    {
        f=true;
        for(i=0;i<4;++i)
        in>>s[i];
        out<<"Case #"<<++k<<": ";
        d=0;
        for(i=0;i<4;++i)
        {
            x=o=T=0;
            for(j=0;j<4;++j)
            if(s[i][j]=='X')
            ++x;
            else if(s[i][j]=='O')
            ++o;
            else if(s[i][j]=='.')
            ++d;
            else
            ++T;
            if(x==4||(x==3&&T==1))
            {
                out<<"X won\n";
                f=false;
                continue;
            }
            else if(o==4||(o==3&&T==1))
            {
                out<<"O won\n";
                f=false;
                continue;
            }
        }
        if(f)
        for(j=0;j<4;++j)
        {
            x=o=T=0;
            for(i=0;i<4;++i)
            if(s[i][j]=='X')
            ++x;
            else if(s[i][j]=='O')
            ++o;
            else if(s[i][j]=='.')
            ++d;
            else
            ++T;
            if(x==4||(x==3&&T==1))
            {
                out<<"X won\n";
                f=false;
                continue;
            }
            else if(o==4||(o==3&&T==1))
            {
                out<<"O won\n";
                f=false;
                continue;
            }
        }
        x=o=T=0;
        if(f)
        for(i=j=0;i<4;++i,++j)
        {
            if(s[i][j]=='X')
            ++x;
            else if(s[i][j]=='O')
            ++o;
            else if(s[i][j]=='.')
            ++d;
            else
            ++T;
            if(x==4||(x==3&&T==1))
            {
                out<<"X won\n";
                f=false;
                continue;
            }
            else if(o==4||(o==3&&T==1))
            {
                out<<"O won\n";
                f=false;
                continue;
            }
        }
        x=o=T=0;
        if(f)
        for(i=0,j=3;i<4;++i,--j)
        {
            if(s[i][j]=='X')
            ++x;
            else if(s[i][j]=='O')
            ++o;
            else if(s[i][j]=='.')
            ++d;
            else
            ++T;
            if(x==4||(x==3&&T==1))
            {
                out<<"X won\n";
                f=false;
                continue;
            }
            else if(o==4||(o==3&&T==1))
            {
                out<<"O won\n";
                f=false;
                continue;
            }
        }
        if(f)
        {
            if(d==0)
            out<<"Draw\n";
            else
            out<<"Game has not completed\n";
        }
    }
    in.close();
    out.close();
    return 0;
}
