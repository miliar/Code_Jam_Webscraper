#include<iostream>
using namespace std;
bool checkRow(char);
bool checkColumn(char);
bool checkDiagonal(char);
bool checkDiagonal2(char);
char input[4][4];
bool isBlank=false;
int main()
{
int T=0;
cin>>T;

for(int j=0;j<T;j++)
{
    cout<<"Case #"<<(j+1)<<": ";
for(int i=0;i<4;i++)
  cin>>input[i];
    if(checkRow('X'))
        cout<<"X won";
    else if(checkRow('O'))
        cout<<"O won";
    else if(checkColumn('X'))
        cout<<"X won";
    else if(checkColumn('O'))
        cout<<"O won";
    else if(checkDiagonal('X'))
        cout<<"X won";
    else if(checkDiagonal2('X'))
        cout<<"X won";
    else if(checkDiagonal('O'))
        cout<<"O won";
    else if(checkDiagonal2('O'))
        cout<<"O won";
    else if(isBlank)
        cout<<"Game has not completed";
    else
        cout<<"Draw";

cout<<endl;
}
return 0;
}


bool checkRow(char x)
{
    int count=0;
    for(int i=0;i<4;i++)
    {
       count=0;
     for(int j=0;j<4;j++)
     {
        if(input[i][j]==x || input[i][j]=='T') count++;
        else if(input[j][i]=='.') isBlank=true;
     }
     if(count==4)
     {return true;}
    }
return false;
}

bool checkColumn(char x)
{
    int count=0;
    for(int i=0;i<4;i++)
    {
       count=0;
     for(int j=0;j<4;j++)
     {
        if(input[j][i]==x || input[j][i]=='T') count++;
        else if(input[j][i]=='.') isBlank=true;
     }
     if(count==4)
     {return true;}
    }
return false;
}

bool checkDiagonal(char x)
{
    int i=0;
    int count=0;
       count=0;
     for(int j=0;j<4;j++)
     {
        if(input[i][j]==x || input[i][j]=='T') count++;
        else if(input[j][i]=='.') isBlank=true;
        i++;
     }
     if(count==4)
     {return true;}
return false;
}


bool checkDiagonal2(char x)
{
    int i=0;
    int count=0;
     for(int j=3;j>=0;j--)
     {
        if(input[i][j]==x || input[i][j]=='T') count++;
        else if(input[j][i]=='.') isBlank=true;
        i++;
     }
     if(count==4)
     {return true;}
return false;
}
