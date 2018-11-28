#include <iostream>
#include <fstream>
using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

int n,m,k;
char a[55][55];

bool draw()
{
    int i,j;
    if(n*m == k)
        return false;

    if(n==1 || m==1 || n*m == k+1)
    {
        for(i=0; i<n; ++i)
            for(j=0; j<m; ++j)
                if(a[i][j]=='.' && k>0)
                {
                    a[i][j] = '*';
                    --k;
                }
        return true;
    }

    if(n==2 || m==2)
    {
        if(k%2 == 1 || k+2 == n*m)
            return false;

        if(n==2)
        {
            for(j=0; j<m; ++j)
                for(i=0; i<n; ++i)
                    if(a[i][j]=='.' && k>0)
                    {
                        a[i][j] = '*';
                        --k;
                    }
            return true;
        }
        for(i=0; i<n; ++i)
            for(j=0; j<m; ++j)
                if(a[i][j]=='.' && k>0)
                {
                    a[i][j] = '*';
                    --k;
                }
        return true;
    }

    for(i=0; i<n-3; ++i)
        for(j=0; j<m; ++j)
            if(a[i][j]=='.' && k>0)
            {
                a[i][j] = '*';
                --k;

                if(k==0 && j==m-2)
                {
                    a[i][j]='.';
                    a[i+1][0]='*';
                    break; 
                }
            }

    if(k==0)
        return true;
    

    for(j=0; j<m-3; ++j)
        for(i=0; i<n; ++i)
            if(a[i][j]=='.' && k>0)
            {
                a[i][j] = '*';
                --k;

                if(k==0 && i==n-2)
                {
                    a[i][j]='.';
                    a[n-3][j+1]='*';
                    break; 
                }
            }

    if(k==0)
        return true;

    if(k==1)
    {
        a[n-3][m-3]='*';
        return true;
    }
    else if(k==2)
        return false;
    else if(k==3)
    {
        a[n-3][m-3] = a[n-3][m-2] = a[n-3][m-1] = '*';
        return true;
    }
    else if(k==4)
        return false;
    else if(k==5)
    {
        a[n-3][m-3] = a[n-3][m-2] = a[n-3][m-1] = '*';
        a[n-2][m-3] = a[n-1][m-3] = '*';
        return true;
    }
    else
       return false;

    cout << "Error"; 

    return true;
}

void print()
{
    int i,j;
    for(i=0;i<n;++i)
    {
        for(j=0; j<m; ++j)
            fout<<a[i][j];
        fout << endl;
    }
}

int main()
{
    int t,i,j,tt;
    fin >> tt;
    for(t=1; t<=tt; ++t)
    {
        fin>>n>>m>>k;
        for(i=0; i<n; ++i)
            for(j=0; j<m; ++j)
                a[i][j]='.';
        a[n-1][m-1] = 'c';

        fout << "Case #" << t << ":" <<endl;

        if(!draw())
            fout<<"Impossible"<<endl;
        else
            print();
    }
    return 0;
}


