#include<iostream>
#include<vector>
using namespace std;

int printResult(vector < vector <char> > input, bool isDot)
{
    int oCount=0,xCount=0;
    for(int i=0;i<4;i++)
    {   oCount=0;xCount=0;
        for(int j=0;j<4;j++)
        {
            if(input[i][j]=='X')
                xCount++;
            if(input[i][j]=='O')
                oCount++;
            if(input[i][j]=='T')
            {
                 oCount++;xCount++;
            }

        }
        if(oCount==4)
        {
          //  cout<<"O Wins"<<endl;
           return 0;
        }
        if(xCount==4)
        {
          //  cout<<"X Wins"<<endl;
            return 1;
        }
    }

    for(int i=0;i<4;i++)
    {   oCount=0;xCount=0;
        for(int j=0;j<4;j++)
        {
            if(input[j][i]=='X')
                xCount++;
            if(input[j][i]=='O')
                oCount++;
            if(input[j][i]=='T')
            {
                 oCount++;xCount++;
            }

        }
        if(oCount==4)
        {
           // cout<<"O Wins"<<endl;
           return 0;
        }
        if(xCount==4)
        {
          // cout<<"X Wins"<<endl;
           return 1;
        }
    }

    oCount=0;xCount=0;
    for(int i=0,j=0;i<4&&j<4;i++,j++)
    {

            if(input[i][j]=='X')
                xCount++;
            if(input[i][j]=='O')
                oCount++;
            if(input[i][j]=='T')
            {
                 oCount++;xCount++;
            }

        }
        if(oCount==4)
        {
           // cout<<"O Wins"<<endl;
           return 0;
        }
        if(xCount==4)
        {
          //  cout<<"X Wins"<<endl;
           return 1;
        }

        oCount=0;xCount=0;
    for(int i=3,j=0;i>=0&&j<4;i--,j++)
    {

            if(input[i][j]=='X')
                xCount++;
            if(input[i][j]=='O')
                oCount++;
            if(input[i][j]=='T')
            {
                 oCount++;xCount++;
            }

        }
        if(oCount==4)
        {
         //   cout<<"O Wins"<<endl;
           return 0;
        }
        if(xCount==4)
        {
          //  cout<<"X Wins"<<endl;
           return 1;
        }

    if(isDot)
    {
        return 3;
    }
    else
        return 2;
return 3;
}
int main()
{
    int t;
    cin>>t;
    int temp=0;
    while(t--)
    {
        temp++;
        vector < vector <char > > input;
        vector<char> vinp;
        char ch;
        bool isDot=false;
        for(int i=0;i<16;i++)
        {
            cin>>ch;
            if(ch=='.')
                isDot = true;
            vinp.push_back(ch);
            if((i+1)%4==0)
            {
                input.push_back(vinp);
                vinp.clear();
            }
        }
        int x = printResult(input,isDot);
        if(x==0)
            cout<<"Case #"<<temp<<": O won"<<endl;
        else if(x==1)
            cout<<"Case #"<<temp<<": X won"<<endl;
        else if(x==2)
            cout<<"Case #"<<temp<<": Draw"<<endl;
        else
            cout<<"Case #"<<temp<<": Game has not completed"<<endl;
    }
    return 0;
}
