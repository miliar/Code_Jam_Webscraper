 #include <iostream>

using namespace std;
bool won_x(char mat[4][4])
{
for(int i=0;i<4;i++)
{
    int x=0,t=0;
    for(int j=0;j<4;j++)
    {
        if(mat[i][j]=='X')x++;
        else if(mat[i][j]=='T')t++;

    }
    if(x==4||(x==3&&t==1))return true;
}
for(int i=0;i<4;i++)
{
    int x=0,t=0;
    for(int j=0;j<4;j++)
    {
        if(mat[j][i]=='X')x++;
        else if(mat[j][i]=='T')t++;

    }
    if(x==4||(x==3&&t==1))return true;
}
int x=0,t=0;
for(int i=0;i<4;i++)
{
    if(mat[i][i]=='X')x++;
    else if(mat[i][i]=='T')t++;
}
if(x==4||(x==3&&t==1))return true;
x=0,t=0;
for(int i=0;i<4;i++)
{
    if(mat[i][3-i]=='X')x++;
    else if(mat[i][3-i]=='T')t++;
}
if(x==4||(x==3&&t==1))return true;
return false;
}
////////////////////////////////////////////////////////////
bool won_o(char mat[4][4])
{
for(int i=0;i<4;i++)
{
    int x=0,t=0;
    for(int j=0;j<4;j++)
    {
        if(mat[i][j]=='O')x++;
        else if(mat[i][j]=='T')t++;

    }
    if(x==4||(x==3&&t==1))return true;
}
for(int i=0;i<4;i++)
{
    int x=0,t=0;
    for(int j=0;j<4;j++)
    {
        if(mat[j][i]=='O')x++;
        else if(mat[j][i]=='T')t++;

    }
    if(x==4||(x==3&&t==1))return true;
}

int x=0,t=0;
for(int i=0;i<4;i++)
{
    if(mat[i][i]=='O')x++;
    else if(mat[i][i]=='T')t++;
}
if(x==4||(x==3&&t==1))return true;
x=0,t=0;
for(int i=0;i<4;i++)
{
    if(mat[i][3-i]=='O')x++;
    else if(mat[i][3-i]=='T')t++;
}
if(x==4||(x==3&&t==1))return true;
return false;
}
///////////////////////////
bool comp(char mat[4][4])
{
    for(int i=0;i<4;i++)
    for(int j=0;j<4;j++)
    if(mat[i][j]=='.')return false;
    return true;
}
int main()
{
    int t;
    cin>>t;
    for(int k=1;k<=t;k++)
    {
    char mat[4][4];
    for(int i=0;i<4;i++)
    {
        for(int j=0;j<4;j++)
        {
            cin>>mat[i][j];
        }
    }
    if(won_x(mat))cout<<"Case #"<<k<<": X won"<<endl;
    else if(won_o(mat))cout<<"Case #"<<k<<": O won"<<endl;
    else if(!comp(mat))cout<<"Case #"<<k<<": Game has not completed"<<endl;
    else
    cout<<"Case #"<<k<<": Draw"<<endl;
    }
    return 0;
}
