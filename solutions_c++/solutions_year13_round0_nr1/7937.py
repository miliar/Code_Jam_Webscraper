

#include <iostream>
#include <fstream>
#include <string>


using namespace std;


int main()
{
    ofstream out("a.out");
    ifstream in("a.in");
    int t,x=0,o=0,tt=0,p=0;
    bool xwin=false,owin=false;

    string s[4];
    in>>t;
    for(int i=0;i<t;i++)
    {
        for(int j=0;j<4;j++)
            in>>s[j];
        for(int j=0;j<4;j++)
        {   
            for(int k=0;k<4;k++)
            {
                if(s[j][k]=='X')
                    x++;
                else if(s[j][k]=='O')
                    o++;
                else if(s[j][k]=='T')
                    tt=1;
                else p++;
            }
            if(x==4||(x==3&&tt==1)) {xwin=true; break;}
            else if(o==4||(o==3&&tt==1)) {owin=true; break;}
            x=o=tt=0;
        }
        for(int j=0;j<4;j++)
        {   
            for(int k=0;k<4;k++)
            {
                if(s[k][j]=='X')
                    x++;
                else if(s[k][j]=='O')
                    o++;
                else if(s[k][j]=='T')
                    tt=1;
                else p++;
            }
            if(x==4||(x==3&&tt==1)) {xwin=true; break;}
            else if(o==4||(o==3&&tt==1)) {owin=true; break;}
            x=o=tt=0;
        }
        for(int j=0;j<4;j++)
        {
            if(s[j][j]=='X')
                    x++;
                else if(s[j][j]=='O')
                    o++;
                else if(s[j][j]=='T')
                    tt=1;
                else p++;
        }
        if(x==4||(x==3&&tt==1)) {xwin=true;}
            else if(o==4||(o==3&&tt==1)) {owin=true;}
            x=o=tt=0;
        for(int j=0;j<4;j++)
        {
            if(s[j][3-j]=='X')
                    x++;
                else if(s[j][3-j]=='O')
                    o++;
                else if(s[j][3-j]=='T')
                    tt=1;
                else p++;
        }
        if(x==4||(x==3&&tt==1)) {xwin=true;}
            else if(o==4||(o==3&&tt==1)) {owin=true;}
            x=o=tt=0;
        if(xwin) out<<"Case #"<<i+1<<": X won"<<endl;
        else if(owin) out<<"Case #"<<i+1<<": O won"<<endl;
        else if(!xwin&&!owin&&p==0) out<<"Case #"<<i+1<<": Draw"<<endl;
        else out<<"Case #"<<i+1<<": Game has not completed"<<endl;
        p=0;xwin=false,owin=false;

    }
    

    
    out.close();
    in.close();
    return 0;
}