#include <stdio.h>
#include <iostream>
#include <string>
#include <cstring>

using namespace std;

int flagx,flagy;

void row(string arr[])
{
    for(int i=0;i<4;i++)
    {
        if(arr[i][0]=='X'&&arr[i][1]=='X'&&arr[i][2]=='X'&&arr[i][3]=='X')
        {
            flagx=1;
        }
        if(arr[i][0]=='X'&&arr[i][1]=='X'&&arr[i][2]=='X'&&arr[i][3]=='T')
        {
            flagx=1;
        }
        if(arr[i][0]=='T'&&arr[i][1]=='X'&&arr[i][2]=='X'&&arr[i][3]=='X')
        {
            flagx=1;
        }
        if(arr[i][0]=='X'&&arr[i][1]=='T'&&arr[i][2]=='X'&&arr[i][3]=='X')
        {
            flagx=1;
        }
        if(arr[i][0]=='X'&&arr[i][1]=='X'&&arr[i][2]=='T'&&arr[i][3]=='X')
        {
            flagx=1;
        }

        if(arr[i][0]=='O'&&arr[i][1]=='O'&&arr[i][2]=='O'&&arr[i][3]=='O')
        {
            flagy=1;
        }
        if(arr[i][0]=='O'&&arr[i][1]=='O'&&arr[i][2]=='O'&&arr[i][3]=='T')
        {
            flagy=1;
        }
        if(arr[i][0]=='T'&&arr[i][1]=='O'&&arr[i][2]=='O'&&arr[i][3]=='O')
        {
            flagy=1;
        }
        if(arr[i][0]=='O'&&arr[i][1]=='T'&&arr[i][2]=='O'&&arr[i][3]=='O')
        {
            flagy=1;
        }
        if(arr[i][0]=='O'&&arr[i][1]=='O'&&arr[i][2]=='T'&&arr[i][3]=='O')
        {
            flagy=1;
        }
    }
}


void column(string arr[])
{
    for(int i=0;i<4;i++)
    {
        if(arr[0][i]=='O'&&arr[1][i]=='O'&&arr[2][i]=='O'&&arr[3][i]=='O')
        {
            flagy=1;
        }
        if(arr[0][i]=='T'&&arr[1][i]=='O'&&arr[2][i]=='O'&&arr[3][i]=='O')
        {
            flagy=1;
        }
        if(arr[0][i]=='O'&&arr[1][i]=='T'&&arr[2][i]=='O'&&arr[3][i]=='O')
        {
            flagy=1;
        }
        if(arr[0][i]=='O'&&arr[1][i]=='O'&&arr[2][i]=='T'&&arr[3][i]=='O')
        {
            flagy=1;
        }
        if(arr[0][i]=='O'&&arr[1][i]=='O'&&arr[2][i]=='O'&&arr[3][i]=='T')
        {
            flagy=1;
        }

        if(arr[0][i]=='X'&&arr[1][i]=='X'&&arr[2][i]=='X'&&arr[3][i]=='X')
        {
            flagx=1;
        }
        if(arr[0][i]=='T'&&arr[1][i]=='X'&&arr[2][i]=='X'&&arr[3][i]=='X')
        {
            flagx=1;
        }
        if(arr[0][i]=='X'&&arr[1][i]=='T'&&arr[2][i]=='X'&&arr[3][i]=='X')
        {
            flagx=1;
        }
        if(arr[0][i]=='X'&&arr[1][i]=='X'&&arr[2][i]=='T'&&arr[3][i]=='X')
        {
            flagx=1;
        }
        if(arr[0][i]=='X'&&arr[1][i]=='X'&&arr[2][i]=='X'&&arr[3][i]=='T')
        {
            flagx=1;
        }
    }
}


void diagonal(string arr[])
{
    if(arr[0][0]=='X'&&arr[1][1]=='X'&&arr[2][2]=='X'&&arr[3][3]=='X')
    {
        flagx=1;
    }
    if(arr[0][0]=='T'&&arr[1][1]=='X'&&arr[2][2]=='X'&&arr[3][3]=='X')
    {
        flagx=1;
    }
    if(arr[0][0]=='X'&&arr[1][1]=='T'&&arr[2][2]=='X'&&arr[3][3]=='X')
    {
        flagx=1;
    }
    if(arr[0][0]=='X'&&arr[1][1]=='X'&&arr[2][2]=='T'&&arr[3][3]=='X')
    {
        flagx=1;
    }
    if(arr[0][0]=='X'&&arr[1][1]=='X'&&arr[2][2]=='X'&&arr[3][3]=='T')
    {
        flagx=1;
    }

    if(arr[0][0]=='O'&&arr[1][1]=='O'&&arr[2][2]=='O'&&arr[3][3]=='O')
    {
        flagy=1;
    }
    if(arr[0][0]=='T'&&arr[1][1]=='O'&&arr[2][2]=='O'&&arr[3][3]=='O')
    {
        flagy=1;
    }
    if(arr[0][0]=='O'&&arr[1][1]=='T'&&arr[2][2]=='O'&&arr[3][3]=='O')
    {
        flagy=1;
    }
    if(arr[0][0]=='O'&&arr[1][1]=='O'&&arr[2][2]=='T'&&arr[3][3]=='O')
    {
        flagy=1;
    }
    if(arr[0][0]=='O'&&arr[1][1]=='O'&&arr[2][2]=='O'&&arr[3][3]=='T')
    {
        flagy=1;
    }




    if(arr[0][3]=='X'&&arr[1][2]=='X'&&arr[2][1]=='X'&&arr[3][0]=='X')
    {
        flagx=1;
    }
    if(arr[0][3]=='T'&&arr[1][2]=='X'&&arr[2][1]=='X'&&arr[3][0]=='X')
    {
        flagx=1;
    }
    if(arr[0][3]=='X'&&arr[1][2]=='T'&&arr[2][1]=='X'&&arr[3][0]=='X')
    {
        flagx=1;
    }
    if(arr[0][3]=='X'&&arr[1][2]=='X'&&arr[2][1]=='T'&&arr[3][0]=='X')
    {
        flagx=1;
    }
    if(arr[0][3]=='X'&&arr[1][2]=='X'&&arr[2][1]=='X'&&arr[3][0]=='T')
    {
        flagx=1;
    }

    if(arr[0][3]=='O'&&arr[1][2]=='O'&&arr[2][1]=='O'&&arr[3][0]=='O')
    {
        flagy=1;
    }
    if(arr[0][3]=='T'&&arr[1][2]=='O'&&arr[2][1]=='O'&&arr[3][0]=='O')
    {
        flagy=1;
    }
    if(arr[0][3]=='O'&&arr[1][2]=='T'&&arr[2][1]=='O'&&arr[3][0]=='O')
    {
        flagy=1;
    }
    if(arr[0][3]=='O'&&arr[1][2]=='O'&&arr[2][1]=='T'&&arr[3][0]=='O')
    {
        flagy=1;
    }
    if(arr[0][3]=='O'&&arr[1][2]=='O'&&arr[2][1]=='O'&&arr[3][0]=='T')
    {
        flagy=1;
    }
}


bool isempty(string arr[])
{
    for(int i=0;i<4;i++)
    {
        for(int j=0;j<4;j++)
        {
            if(arr[i][j]=='.')
            {
                return true;
            }
        }
    }
    return false;
}

int main()
{
    int t;

    cin>>t;

    string arr[4];

    for(int k=0;k<t;k++)
    {
        int i=0;
        while(i<4)
        {
            cin>>arr[i];
            i++;
        }
        flagx=0;
        flagy=0;

        row(arr);
        column(arr);
        diagonal(arr);
        cout<<"Case #"<<(k+1)<<": ";
        if(flagx==1 && flagy==1)
        {
            cout<<"Draw";
        }
        else if(flagx==1)
        {
            cout<<"X won";
        }
        else if(flagy==1)
        {
            cout<<"O won";
        }
        else if(flagx==0 && flagy==0)
        {
            if(isempty(arr))
            {
                cout<<"Game has not completed";
            }
            else
            {
                cout<<"Draw";
            }
        }
        cout<<endl;
    }
    return 0;
}
