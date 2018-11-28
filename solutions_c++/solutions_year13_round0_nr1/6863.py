#include<iostream>
#include<cstdio>
#include<cstdlib>
using namespace std;
int main()
{
    char a[4][4];
    int row[4],col[4],diag[2];
    int row1[4],col1[4],diag1[2];
    int t,n=0;
    cin>>t;
    while(t--)
    {
        n++;
        int dot=0;
        diag[0]=diag[1]=diag1[0]=diag1[1]=0;
        for(int i=0;i<4;i++)
        {
            row[i]=col[i]=row1[i]=col1[i]=0;
            for(int j=0;j<4;j++)
            {
                cin>>a[i][j];
            }
        }
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                if(a[i][j]=='X' || a[i][j]=='T')
                {
                    row[i]++;
                    col[j]++;
                }
                if(a[i][j]=='O' || a[i][j]=='T')
                {
                    row1[i]++;
                    col1[j]++;
                }
                if(a[i][j]=='.')dot++;
            }
        }
        for(int i=0;i<4;i++)
        {
            if(a[i][i]=='X' || a[i][i]=='T')diag[0]++;
            if(a[i][i]=='O' || a[i][i]=='T')diag1[0]++;
        }
        int j=3;
        for(int i=0;i<4;i++)
        {
            if(a[i][j]=='X' || a[i][j]=='T')diag[1]++;
            if(a[i][j]=='O' || a[i][j]=='T')diag1[1]++;
            j--;
        }
        if(row[0]==4 || row[1]==4 || row[2]==4 || row[3]==4 || col[0]==4 || col[1]==4 || col[2]==4 || col[3]==4 || diag[0]==4 || diag[1]==4)
            cout<<"Case #"<<n<<": X won"<<endl;
        else if(row1[0]==4 || row1[1]==4 || row1[2]==4 || row1[3]==4 || col1[0]==4 || col1[1]==4 || col1[2]==4 || col1[3]==4 || diag1[0]==4 || diag1[1]==4)
            cout<<"Case #"<<n<<": O won"<<endl;
        else if(dot==0)
            cout<<"Case #"<<n<<": Draw"<<endl;
        else
            cout<<"Case #"<<n<<": Game has not completed"<<endl;
    }
    return 0;
}
