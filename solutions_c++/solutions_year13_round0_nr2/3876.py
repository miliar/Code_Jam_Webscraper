#include<iostream>
#include<algorithm>
using namespace std;
#define F(i,m,n) for(int i = m; i<=n; i++)

int desiredGrid[100][100];
int originalGrid[100][100];

void inputGrid(int m, int n)
{
    F(a,0,m-1)
        {
            F(b,0,n-1)
            {
               cin>>desiredGrid[a][b];
               originalGrid[a][b] = 100;
            }

        }
}

void outputGrid(int m, int n)
{
    F(a,0,m-1)
        {
            F(b,0,n-1)
            {
                cout<<originalGrid[a][b]<<" ";
            }
            cout<<'\n';
        }
}

void cutLawn(int m, int n)
{
    //for rows
    F(i,0,m-1)
    {
        int max = 0;
        F(j,0,n-1)
        {
            if(max < desiredGrid[i][j])
            {
                max = desiredGrid[i][j];
            }
        }

        F(j,0,n-1)
        {
            if(originalGrid[i][j] > max)
            {
                originalGrid[i][j] = max;
            }
        }
    }


    //for cols
    F(j,0,n-1)
    {
        int max = 0;
        F(i,0,m-1)
        {
            if(max < desiredGrid[i][j])
            {
                max = desiredGrid[i][j];
            }
        }

        F(i,0,m-1)
        {
            if(originalGrid[i][j] > max)
            {
                originalGrid[i][j] = max;
            }
        }
    }
}

void verifyCutting(int m, int n)
{
    F(i,0,m-1)
    {
        F(j,0,n-1)
        {
            if(originalGrid[i][j] != desiredGrid[i][j])
            {
                cout<<"NO";
                return;
            }
        }
    }
    cout<<"YES";
}

int main()
{

    int t;
    cin>>t;

    int m,n;

    F(i,1,t)
    {
        cin>>m>>n;
        inputGrid(m,n);

        cout<<"Case #"<<i<<": ";

        cutLawn(m,n);

        verifyCutting(m,n);
        cout<<endl;
       // outputGrid(m,n);
    }

    return 0;
}
