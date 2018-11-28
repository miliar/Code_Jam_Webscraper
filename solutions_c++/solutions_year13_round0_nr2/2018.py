#include <iostream>
using namespace std;

int n, m;
int lawn[200][200];
int rowMax[200], colMax[200];

bool calculate()
{
    for(int i=1; i<=n; ++i)
    {
        rowMax[i]=lawn[i][1];
        for(int j=2; j<=m; ++j)
            rowMax[i]=rowMax[i]>lawn[i][j]?rowMax[i]:lawn[i][j];
    }
    for(int j=1; j<=m; ++j)
    {
        colMax[j]=lawn[1][j];
        for(int i=2; i<=n; ++i)
            colMax[j]=colMax[j]>lawn[i][j]?colMax[j]:lawn[i][j];
    }
    for(int i=1; i<=n; ++i)
        for(int j=1; j<=m; ++j)
            if(!(lawn[i][j]==rowMax[i]||lawn[i][j]==colMax[j]))
                return false;
    return true;
}

int main()
{
    int numOfCases;
    cin>>numOfCases;
    for(int i=1; i<=numOfCases; ++i)
    {
        cin>>n>>m;
        for(int j=1; j<=n; ++j)
            for(int k=1; k<=m; ++k)
                cin>>lawn[j][k];
        cout<<"Case #"<<i<<": ";
        cout<<(calculate()?"YES":"NO");
        cout<<endl;
    }
    return 0;
}

