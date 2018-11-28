#include<fstream>
using namespace std;
ifstream cin ("temp.in");
ofstream cout ("temp.out");
char save[100][100];
int main ()
{
    int t;
    cin>>t;
    for (int i=1;i<=t;i++)
    {
        cout<<"Case #"<<i<<": ";
        int r,c;
        int num=0;
        bool can=true;
        cin>>r>>c;
        for (int x=0;x<r;x++)
            for (int y=0;y<c;y++)
                cin>>save[x][y];
        for (int x=0;x<r&&can;x++)
            for (int y=0;y<c&&can;y++)
                if (save[x][y]!='.')
                {
                    bool find=false;
                    if (save[x][y]=='^')
                        for (int z=x-1;z>=0&&!find;z--)
                            if (save[z][y]!='.') find=true;
                    if (save[x][y]=='v')
                        for (int z=x+1;z<r&&!find;z++)
                            if (save[z][y]!='.') find=true;
                    if (save[x][y]=='>')
                        for (int z=y+1;z<c&&!find;z++)
                            if (save[x][z]!='.') find=true;
                    if (save[x][y]=='<')
                        for (int z=y-1;z>=0&&!find;z--)
                            if (save[x][z]!='.') find=true;
                    if (!find)
                    {
                        for (int z=x-1;z>=0&&!find;z--)
                            if (save[z][y]!='.') find=true;
                        for (int z=x+1;z<r&&!find;z++)
                            if (save[z][y]!='.') find=true;
                        for (int z=y+1;z<c&&!find;z++)
                            if (save[x][z]!='.') find=true;
                        for (int z=y-1;z>=0&&!find;z--)
                            if (save[x][z]!='.') find=true;
                        if (find) num++;
                        else can=false;
                    }
                }
        if (!can) cout<<"IMPOSSIBLE"<<endl;
        else cout<<num<<endl;
    }

}
