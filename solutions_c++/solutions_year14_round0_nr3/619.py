#include<iostream>
#include<fstream>
#include<sstream>
#include<algorithm>
#include<vector>
using namespace std;

int main()
{
    ifstream in;
    ofstream out;
    out.open("output.txt");
    in.open("input.txt");
    int  testcase;
    in>>testcase;
    for(int i=0;i<testcase;i++)
    {
        int row,col,mains;
        in>>row;
        in>>col;
        in>>mains;

        char arr[row][col];
        int ma=mains;
        int r=0,c=0;
        int row1=row;
        int col1=col;

        for(int k=0;k<row1;k++)
            for(int j=0;j<col1;j++)
                arr[k][j]='.';
        while(mains != 0)
        {
            if(row >= col)
            {
                if(mains == col1-c-1)
                {
                    for(int k=c;k<col1-2;k++)
                    {
                        arr[r][k]='*';
                        mains--;
                    }
                    if(r < row1 && r+1 != row1)
                    arr[r+1][c]='*';
                    else
                     arr[r][col1-1]='*';
                     mains--;
                    break;
                }
                for(int k=c;k<col1;k++)
                {
                    if(mains == 0)
                    break;
                    arr[r][k]='*';
                    mains--;
                }
                row--;
                r++;
            }


            if(row < col)
            {
                if(mains == row1-r-1)
                {
                    for(int k=r;k<row1-2;k++)
                    {
                        arr[k][c]='*';
                        mains--;
                    }
                    if(c < col1 && c+1 != col1)
                    arr[r][c+1]='*';
                    else
                    arr[row1-1][c]='*';
                    mains--;
                    break;
                }
                for(int k=r;k<row1;k++)
                {
                    if(mains == 0)
                    break;
                    arr[k][c]='*';
                    mains--;
                }
                col--;
                c++;
            }
        }

        int coun=0;

        for(int k=0;k<row1;k++)
        {
            for(int l=0;l<col1;l++)
            {
                if(arr[k][l]=='.')
                {
                    if(arr[k-1][l-1]=='*' && l-1>=0 && k-1>=0)
                        coun++;
                    if(arr[k-1][l]=='*' && k-1>=0)
                        coun++;
                    if(arr[k-1][l+1]=='*' && l+1<col1 && k-1>=0)
                        coun++;
                    if(arr[k][l-1]=='*' && l-1>=0 )
                        coun++;
                    if(arr[k][l+1]=='*' && l+1<col1 )
                        coun++;
                    if(arr[k+1][l-1]=='*' && l-1>=0 && k+1<row1)
                        coun++;
                    if(arr[k+1][l]=='*' && k+1<row1)
                        coun++;
                    if(arr[k+1][l+1]=='*' && l+1<col1 && k+1<row1)
                        coun++;
                    coun+=48;
                    arr[k][l]=coun;
                    coun=0;
                }
            }
        }
        int check=0;
        for(int k=0;k<row1;k++)
        {
            for(int l=0;l<col1;l++)
            {
                if(arr[k][l] != '*' && arr[k][l] != '0')
                {
                    if(arr[k-1][l-1]=='0' && l-1>=0 && k-1>=0)
                        continue;
                    if(arr[k-1][l]=='0' && k-1>=0)
                        continue;
                    if(arr[k-1][l+1]=='0' && l+1<col1 && k-1>=0)
                        continue;
                    if(arr[k][l-1]=='0' && l-1>=0 )
                        continue;
                    if(arr[k][l+1]=='0' && l+1<col1 )
                        continue;
                    if(arr[k+1][l-1]=='0' && l-1>=0 && k+1<row1)
                        continue;
                    if(arr[k+1][l]=='0' && k+1<row1)
                        continue;
                    if(arr[k+1][l+1]=='0' && l+1<col1 && k+1<row1)
                        continue;
                    check=1;
                    break;
                }
            }
        }

        int cou=(row1*col1)-ma;
        out<<"Case #"<<i+1<<":"<<endl;
         if(check && cou != 1)
            out<<"Impossible"<<endl;
        else
        {
            for(int k=0;k<row1;k++)
            {
                for(int u=0;u<col1;u++)
                    if(arr[k][u] != '*')
                        arr[k][u]='.';
            }
            arr[row1-1][col1-1] = 'c';

            for(int k=0;k<row1;k++)
            {
                for(int u=0;u<col1;u++)
                out<<arr[k][u];
                out<<endl;
            }
        }
    }

    return 0;
}
