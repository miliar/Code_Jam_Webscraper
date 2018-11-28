#include <iostream>
#include <string>
#include <fstream>
using namespace std;

char p[5][5];
string x;
int caz=0;
ifstream f("test.in");
ofstream g("test.out");

bool check_col(int col)
{
    int x=0,o=0;
    for(int i=1;i<=4;++i)
        if(p[i][col]=='X')
            ++x;
            else
                if(p[i][col]=='O')
                    ++o;
                    else
                        if(p[i][col]=='T')
                            ++x,++o;
    if(x==4)
    {
        g<<"Case #"<<++caz<<": X won\n";
        return true;
    }
    if(o==4)
    {
        g<<"Case #"<<++caz<<": O won\n";
        return true;
    }
    return false;
}
bool check_line(int line)
{
    int x=0,o=0;
    for(int i=1;i<=4;++i)
        if(p[line][i]=='X')
            ++x;
            else
                if(p[line][i]=='O')
                    ++o;
                    else
                        if(p[line][i]=='T')
                            ++x,++o;
    if(x==4)
    {
        g<<"Case #"<<++caz<<": X won\n";
        return true;
    }
    if(o==4)
    {
        g<<"Case #"<<++caz<<": O won\n";
        return true;
    }
    return false;
}
bool check_diag()
{
    int x=0,o=0;
    int l=4,c=1;
    while(l>=1)
    {
        if(p[l][c]=='X')
            ++x;
            else
                if(p[l][c]=='O')
                    ++o;
                    else
                        if(p[l][c]=='T')
                            ++x,++o;
        --l;
        ++c;
    }
    if(x==4)
    {
        g<<"Case #"<<++caz<<": X won\n";
        return true;
    }
    if(o==4)
    {
        g<<"Case #"<<++caz<<": O won\n";
        return true;
    }
    return false;
}
bool check_diag2()
{
    int x=0,o=0;
    for(int i=1;i<=4;++i)
        if(p[i][i]=='X')
            ++x;
            else
                if(p[i][i]=='O')
                    ++o;
                    else
                        if(p[i][i]=='T')
                            ++x,++o;
    if(x==4)
    {
        g<<"Case #"<<++caz<<": X won\n";
        return true;
    }
    if(o==4)
    {
        g<<"Case #"<<++caz<<": O won\n";
        return true;
    }
    return false;
}



int main()
{
    int t;
    f>>t;
    f.get();

    for(;t;--t)
    {
        bool done=false,completed=true;
        for(int i=1;i<=4;++i)
            for(int j=1;j<=4;++j)
                f>>p[i][j];
        getline(f,x);

        for(int i=1;i<=4;++i)
            for(int j=1;j<=4;++j)
                if(p[i][j]=='.')
                    completed=false;


        for(int i=1;i<=4;++i)
            if(check_col(i)==true)
            {
                done=true;
                break;
            }
        if(done==false)
            for(int i=1;i<=4;++i)
                if(check_line(i)==true)
                {
                    done=true;
                    break;
                }
        if(done==false)
        if(check_diag()==true)
            done=true;
        if(done==false)
        if(check_diag2()==true)
            done=true;

        if(done==false)
        {
            if(completed==false)
                g<<"Case #"<<++caz<<": Game has not completed\n";
                else
                    g<<"Case #"<<++caz<<": Draw\n";
        }

    }

    return 0;
}
