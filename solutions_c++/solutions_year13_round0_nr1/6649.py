#include <fstream>
using namespace std;
ifstream fin("tiktaktoe.in");
ofstream fout("tiktaktoe.out");
int i,j,n,nr,ok=0,k,dot,x,o;
char s[7][7];
int main()
{
    fin>>n;fin.get();
    for(i=1;i<=n;++i)
        {
            ok=0;
            dot=0;
            for(j=0;j<4;++j)
                {
                    fin.get(s[j],7);
                    fin.get();
                    if(ok==0)
                    {
                        nr=1;
                    ok=1;
                    x=0;
                    o=0;
                    for(k=0;k<4;++k)
                    {
                        if(s[j][k]=='X')
                            x=1;
                        if(s[j][k]=='O')
                            o=1;
                        if(s[j][k]=='.')
                            ok=0;
                    }
                    if(x==1&&o==1)
                        ok=0;
                    if(ok==1)
                        {
                            if(x==1)
                                fout<<"Case #"<<i<<": "<<"X"<<" won"<<'\n';
                            else
                                fout<<"Case #"<<i<<": "<<"O"<<" won"<<'\n';
                        }
                }
                }
            if(ok==0)
                for(j=0;j<4&&ok==0;++j)
                    {
                        ok=1;
                        x=0;
                        o=0;
                        for(k=0;k<4;++k)
                            {
                                if(s[k][j]=='X')
                                    x=1;
                                if(s[k][j]=='O')
                                    o=1;
                                if(s[k][j]=='.')
                                    ok=0;
                                if(s[k][j]=='.')
                                    dot=1;
                            }
                        if(x==1&&o==1)
                            ok=0;
                        if(ok==1)
                            {
                                if(x==1)
                                    fout<<"Case #"<<i<<": "<<"X"<<" won"<<'\n';
                                else
                                    fout<<"Case #"<<i<<": "<<"O"<<" won"<<'\n';
                            }
                    }
            if(ok==0)
            {
                ok=1;
                x=0;
                o=0;
                        for(k=0;k<4;++k)
                            {
                                if(s[k][k]=='X')
                                    x=1;
                                if(s[k][k]=='O')
                                    o=1;
                                if(s[k][k]=='.')
                                    ok=0;
                            }
                        if(x==1&&o==1)
                            ok=0;
                        if(ok==1)
                            {
                                if(x==1)
                                    fout<<"Case #"<<i<<": "<<"X"<<" won"<<'\n';
                                else
                                    fout<<"Case #"<<i<<": "<<"O"<<" won"<<'\n';
                            }
            }
            if(ok==0)
            {
                ok=1;
                x=0;
                o=0;
                        for(k=0;k<4;++k)
                            {
                                if(s[k][3-k]=='X')
                                    x=1;
                                if(s[k][3-k]=='O')
                                    o=1;
                                if(s[k][3-k]=='.')
                                    ok=0;
                            }
                        if(x==1&&o==1)
                            ok=0;
                        if(ok==1)
                            {
                                if(x==1)
                                    fout<<"Case #"<<i<<": "<<"X"<<" won"<<'\n';
                                else
                                    fout<<"Case #"<<i<<": "<<"O"<<" won"<<'\n';
                            }
            }

            if(ok==0&&dot==0)
                  fout<<"Case #"<<i<<": "<<"Draw"<<'\n';
                else
                if(ok==0)
                      fout<<"Case #"<<i<<": "<<"Game has not completed"<<'\n';
        fin.get();
        }
    return 0;
}
