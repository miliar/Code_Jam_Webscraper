#include <iostream>

using namespace std;

const char *y="YES",*n="NO";
void check();
int main()
{
    int cases;
    cin>>cases;
    for(int i=1;i<=cases;i++)
    {
        cout<<"Case #"<<i<<": ";
        check();
    }
}

void check()
{
    int n,m;
    cin>>n>>m;
    char *line[n];
    bool *possible[n];
    for(int i=0;i<n;i++)
    {
        line[i]=new char[m];
        possible[i]=new bool[m];
        for(int j=0;j<m;j++)
        {
            possible[i][j]=false;
            cin>>line[i][j];
        }
    }



    for(int i=0;i<n;i++)
    {
        int max=0;
        for(int j=0;j<m;j++)
        {
            max=(max>line[i][j]?max:line[i][j]);
        }
                for(int j=0;j<m;j++)
        {
            if(max==line[i][j])
                possible[i][j]=true;
        }

    }
    for(int i=0;i<m;i++)
    {

        int max=0;
        for(int j=0;j<n;j++)
        {
            max=(max>line[j][i]?max:line[j][i]);
        }
        for(int j=0;j<n;j++)
        {
            if(max==line[j][i])
                possible[j][i]=true;
        }
    }

    for(int i=0;i<n;i++)
        for(int j=0;j<m;j++)
            if(!possible[i][j])
            {
                cout<<::n<<'\n';
                return;
            }
    cout<<::y<<'\n';
    return;
}
