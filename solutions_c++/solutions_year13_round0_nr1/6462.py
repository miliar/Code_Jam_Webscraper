#include<iostream>
using namespace std;
char leftTopToRightBottom(char A[4][4])
{
    bool resx=false;
    bool reso=false;
    int cntsymx=0;
    int cntsymt=0;
    int cntsymo=0;
    for(int i=0;i<4;i++)
    {
        if(A[i][i]=='X')
        {
            cntsymx++;
        }
        else if(A[i][i]=='O')
        {
            cntsymo++;
        }
        else if(A[i][i]=='T')
        {
            cntsymt++;
        }
    }
    if(cntsymo==4 ||(cntsymo==3 && cntsymt==1))
    {
        reso=true;
        return 'O';
    }
    else if(cntsymx==4 ||(cntsymx==3 && cntsymt==1))
    {
        resx=true;
        return 'X';
    }
    else
    {
        return 0;
    }
}
char rightTopToLeftBottom(char A[4][4])
{
    bool resx=false;
    bool reso=false;
    int cntsymx=0;
    int cntsymt=0;
    int cntsymo=0;
    int j=3;
    for(int i=0;i<4;i++)
    {
        if(A[i][j]=='O')
        {
            cntsymo++;
        }
        else if(A[i][j]=='X')
        {
            cntsymx++;
        }
        else if(A[i][j]=='T')
        {
            cntsymt++;
        }
        j--;
    }
    if(cntsymo==4 ||(cntsymo==3 && cntsymt==1))
    {
        reso=true;
        return 'O';
    }
    else if(cntsymx==4 ||(cntsymx==3 && cntsymt==1))
    {
        resx=true;
        return 'X';
    }
    else
    {
        return 0;
    }
}
char rowWiseCheck(char A[4][4])
{
    bool resx=false;
    bool reso=false;
    int cntsymx=0;
    int cntsymt=0;
    int cntsymo=0;
    for(int i=0;i<4;i++)
    {
        cntsymx=0;
        cntsymt=0;
        cntsymo=0;
        for(int j=0;j<4;j++)
        {
            if(A[i][j]=='X')
            {
                cntsymx++;
            }
            else if(A[i][j]=='O')
            {
                cntsymo++;
            }
            else if(A[i][j]=='T')
            {
                cntsymt++;
            }
        }
        if(cntsymo==4 ||(cntsymo==3 && cntsymt==1))
        {
            reso=true;
            break;
        }
        else if(cntsymx==4 ||(cntsymx==3 && cntsymt==1))
        {
            resx=true;
            break;
        }
    }
    if(reso)
    {
        return 'O';
    }
    else if(resx)
    {
        return 'X';
    }
    else
    {
        return 0;
    }
}
char columnWiseCheck(char A[4][4])
{
    bool resx=false;
    bool reso=false;
    int cntsymx=0;
    int cntsymt=0;
    int cntsymo=0;
    for(int i=0;i<4;i++)
    {
        cntsymx=0;
        cntsymt=0;
        cntsymo=0;
        for(int j=0;j<4;j++)
        {
            if(A[j][i]=='X')
            {
                cntsymx++;
            }
            else if(A[j][i]=='O')
            {
                cntsymo++;
            }
            else if(A[j][i]=='T')
            {
                cntsymt++;
            }
        }
        if(cntsymo==4 ||(cntsymo==3 && cntsymt==1))
        {
            reso=true;
            break;
        }
        else if(cntsymx==4 ||(cntsymx==3 && cntsymt==1))
        {
            resx=true;
            break;
        }
    }
    if(reso)
    {
        return 'O';
    }
    else if(resx)
    {
        return 'X';
    }
    else
    {
        return 0;
    }
}
int main()
{
    int t;
    cin>>t;
    int cas=1;
    while(t--)
    {
        bool inc=false;
        char A[4][4];
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                cin>>A[i][j];
                if(inc==false && A[i][j]=='.')
                {
                    inc=true;
                }
            }
        }
        char res=leftTopToRightBottom(A);
        if(res=='O')
        {
            cout<<"Case #"<<cas<<": "<<"O won"<<endl;
            cas++;
            continue;
        }
        else if(res=='X')
        {
            cout<<"Case #"<<cas<<": "<<"X won"<<endl;
            cas++;
            continue;
        }
        res=rightTopToLeftBottom(A);
        if(res=='O')
        {
            cout<<"Case #"<<cas<<": "<<"O won"<<endl;
            cas++;
            continue;
        }
        else if(res=='X')
        {
            cout<<"Case #"<<cas<<": "<<"X won"<<endl;
            cas++;
            continue;
        }
        res=rowWiseCheck(A);
        if(res=='O')
        {
            cout<<"Case #"<<cas<<": "<<"O won"<<endl;
            cas++;
            continue;
        }
        else if(res=='X')
        {
            cout<<"Case #"<<cas<<": "<<"X won"<<endl;
            cas++;
            continue;
        }
        res=columnWiseCheck(A);
        if(res=='O')
        {
            cout<<"Case #"<<cas<<": "<<"O won"<<endl;
            cas++;
            continue;
        }
        else if(res=='X')
        {
            cout<<"Case #"<<cas<<": "<<"X won"<<endl;
            cas++;
            continue;
        }
        else
        {
            if(inc)
            {
                cout<<"Case #"<<cas<<": "<<"Game has not completed"<<endl;
                cas++;
            }
            else
            {
                cout<<"Case #"<<cas<<": "<<"Draw"<<endl;
                cas++;
            }
        }
    }
}
