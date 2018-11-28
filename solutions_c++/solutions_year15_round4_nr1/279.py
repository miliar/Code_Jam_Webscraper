#include <iostream>
#include<fstream>

using namespace std;

int x,y,n,m,ans,a,b;
bool mark;
char c[200][200];

bool go()
{
    x+=a;y+=b;
    while(x>=0 && y>=0 && x<n && y<m)
    {
        if(c[x][y]!='.')
            return true;
        x+=a;y+=b;
    }
    return false;
}

bool check(int i,int j)
{
    x=i,y=j,a=0,b=0;
    if(c[i][j]=='^')    a=-1;
    if(c[i][j]=='v')    a=1;
    if(c[i][j]=='<')    b=-1;
    if(c[i][j]=='>')    b=1;
    if(go())
        return true;
    ans++;
    x=i,y=j,a=0,b=1;
    if(go())
        return true;
    x=i,y=j,a=0,b=-1;
    if(go())
        return true;
    x=i,y=j,a=1,b=0;
    if(go())
        return true;
    x=i,y=j,a=-1,b=0;
    if(go())
        return true;
    return false;
}

int main()
{
    ifstream cin("A-large.in");
    ofstream cout("A-large.out");
    int qw;
    cin>>qw;
    for(int q=1;q<=qw;q++)
    {
        cin>>n>>m;
        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++)
                cin>>c[i][j];
        cout<<"Case #"<<q<<": ";
        ans=0;
        mark=false;
        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++)
                if(c[i][j]!='.')
                    if(!check(i,j))
                        mark=true;
        if(mark)
            cout<<"IMPOSSIBLE\n";
        else
            cout<<ans<<endl;
    }
}
