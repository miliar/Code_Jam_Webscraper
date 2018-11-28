#include<iostream>
#include<vector>
#include<queue>
#include<algorithm>t
#include<cstdlib>
using namespace std;



char A[52][52];
char tymczasowo[52][52];
int ilosc[52][52];

int counter(int x, int y)
{
    int res=0;
    for(int i =x-1; i<=x+1; i++)
        for(int j=y-1; j<=y+1; j++)
            if(A[i][j]=='*') res++;
    return res;
}

void tryy(int x, int y)
{
    A[x][y]='+';
    int ileile=counter(x, y);
    if(ileile!=0)
        return;
    for(int i=x-1; i<=x+1; i++)
    {
        for(int j=y-1; j<=y+1; j++)
        {
            if(A[i][j]!='*' && A[i][j]!='+' && A[i][j]!= '$')
            {
                ilosc[i][j]=counter(i, j);
                if(ilosc[i][j]==0) tryy(i, j);
            }
        }
    }
}

bool checker(int r, int c, int m)
{
    for(int i=1; i<=r; i++)
        for(int j=1; j<=c; j++)
            tymczasowo[i][j]=A[i][j];
    for(int i=1; i<=r; i++)
    {
        for(int j=1; j<=c; j++)
        {
            if(A[i][j]=='.')
            {
                tryy(i, j);
                int ok=0;
                for(int ii=1; ii<=r; ii++)
                {
                    for(int jj=1; jj<=c; jj++)
                    {
                        if(A[ii][jj]=='+' || ilosc[ii][jj]!=0)
                            ok++;
                    }
                }
                if(ok==(r*c-m))
                    {
                        A[i][j]='c';
                        return true;
                    }
                else
                    {
                        for(int i=1; i<=r; i++)
                            for(int j=1; j<=c; j++)
                                {
                                    A[i][j]=tymczasowo[i][j];
                                    ilosc[i][j]=0;
                                }
                    }
            }
        }
    }
    return false;
}

void prepare(int r, int c, int m) {
        /// guardians
        for(int i=0; i<=r+1; i++)
			A[i][0]=A[i][c+1]='$';

        for(int i = 0; i <= c+1; i++)
			 A[0][i]=A[r+1][i]='$';
        ///guardians

        for(int i=1; i<=r; i++)
        	for(int j=1; j<=c; j++)
            {
                A[i][j]='.';
                ilosc[i][j]=0;
            }
}

int main()
{
    ios_base::sync_with_stdio(0);
    int T;
    cin>>T;
    for(int tt=0; tt<T; tt++)
    {
        long long n;
        int r, c, m;
        bool check=false;
        cin>>r>>c>>m;

        n=(1<<(r*c));
        prepare(r, c, m);

        for(long long S=0; S<=n-1; S++)
        {
            int counter=0;
            for(long long i=0; i<=r*c; i++)
				if((S&(1<<i))!=0)
					counter++;

            if(counter!= m)
				continue;

            int column, row=0;

            for(long long i=0; i<=r*c; i++)
            {
                column=i%c+1;
                if(column==1)
                    row++;

                if((S&(1<<i))!=0)
                    A[row][column] = '*';
            }
            if(checker(r, c, m))
            {
                cout<<"Case #"<<tt+1<<":"<<endl;
                for(int i=1; i<=r; i++)
                {
                    for(int j=1; j<=c; j++)
                    {
                        if(A[i][j]=='+')
							cout<<'.';
                        else
                            cout<<A[i][j];
                    }
                    cout<<endl;
                }
                check=true;
                break;
            }
            for(int i=1; i<=r; i++)
                for(int j=1; j<=c; j++)
                    {
                        A[i][j]='.';
                        ilosc[i][j]= 0;
                    }
        }
        if(!check) cout<<"Case #"<<tt+1<<":"<<endl<<"Impossible"<<endl;
    }
    return 0;
}
