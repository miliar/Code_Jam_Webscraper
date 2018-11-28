#include<stdio.h>
#include<iostream>
using namespace std;
int main()
{
    int test,w=1;
    cin>>test;
    while(test--)
    {
        char array[4][5]={'\0'},y;
        int i,j,k,l,m,n,p=0;
        for(i=0;i<4;i++)
        cin>>array[i];
        for(i=0;i<4;i++)
        {
            if((array[i][0]=='X'||array[i][0]=='T')&&(array[i][1]=='X'||array[i][1]=='T')&&(array[i][2]=='X'||array[i][2]=='T')&&(array[i][3]=='X'||array[i][3]=='T'))
            {
                cout<<"Case #"<<w<<": X won\n";
                p=1;
                break;
            }
            else if((array[i][0]=='O'||array[i][0]=='T')&&(array[i][1]=='O'||array[i][1]=='T')&&(array[i][2]=='O'||array[i][2]=='T')&&(array[i][3]=='O'||array[i][3]=='T'))
            {
                cout<<"Case #"<<w<<": O won\n";
                p=1;
                break;
            }
        }
        if(p!=1)
        {
            for(i=0;i<4;i++)
            {
            if((array[0][i]=='X'||array[0][i]=='T')&&(array[1][i]=='X'||array[1][i]=='T')&&(array[2][i]=='X'||array[2][i]=='T')&&(array[3][i]=='X'||array[3][i]=='T'))
            {
                cout<<"Case #"<<w<<": X won\n";
                p=1;
                break;
            }
            else if((array[0][i]=='O'||array[0][i]=='T')&&(array[1][i]=='O'||array[1][i]=='T')&&(array[2][i]=='O'||array[2][i]=='T')&&(array[3][i]=='O'||array[3][i]=='T'))
            {
                cout<<"Case #"<<w<<": O won\n";
                p=1;
                break;
            }
            }
        
        }
        if((array[0][0]=='X'||array[0][0]=='T')&&(array[1][1]=='X'||array[1][1]=='T')&&(array[2][2]=='X'||array[2][2]=='T')&&(array[3][3]=='X'||array[3][3]=='T')&&p!=1)
        {
            cout<<"Case #"<<w<<": X won\n";
            p=1;
        }
        if((array[0][0]=='O'||array[0][0]=='T')&&(array[1][1]=='O'||array[1][1]=='T')&&(array[2][2]=='O'||array[2][2]=='T')&&(array[3][3]=='O'||array[3][3]=='T')&&p!=1)
        {
            cout<<"Case #"<<w<<": O won\n";
            p=1;
        }
        if((array[3][0]=='X'||array[3][0]=='T')&&(array[2][1]=='X'||array[2][1]=='T')&&(array[1][2]=='X'||array[1][2]=='T')&&(array[0][3]=='X'||array[0][3]=='T')&&p!=1)
        {
            cout<<"Case #"<<w<<": X won\n";
            p=1;
        }
        if((array[3][0]=='O'||array[3][0]=='T')&&(array[2][1]=='O'||array[2][1]=='T')&&(array[1][2]=='O'||array[1][2]=='T')&&(array[0][3]=='O'||array[0][3]=='T')&&p!=1)
        {
            cout<<"Case #"<<w<<": O won\n";
            p=1;
        }
        k=0;
        int r=0,d=0;
        if(p!=1)
        {
            for(i=0;i<4;i++)
            {
                if((array[i][0]=='O'||array[i][0]=='T'||array[i][0]=='.')&&(array[i][1]=='O'||array[i][1]=='T'||array[i][1]=='.')&&(array[i][2]=='O'||array[i][2]=='T'||array[i][2]=='.')&&(array[i][3]=='O'||array[i][3]=='T'||array[i][3]=='.'))
                {
                    cout<<"Case #"<<w<<": Game has not completed\n";
                    d=1;
                    r=1;
                    break;
                }
                if((array[i][0]=='X'||array[i][0]=='T'||array[i][0]=='.')&&(array[i][1]=='X'||array[i][1]=='T'||array[i][1]=='.')&&(array[i][2]=='X'||array[i][2]=='T'||array[i][2]=='.')&&(array[i][3]=='X'||array[i][3]=='T'||array[i][3]=='.'))
                {
                    cout<<"Case #"<<w<<": Game has not completed\n";
                    d=1;
                    r=1;
                    break;
                }
            }
            if(d!=1)
            {
            for(i=0;i<4;i++)
            {
                if((array[0][i]=='O'||array[0][i]=='T'||array[0][i]=='.')&&(array[1][i]=='O'||array[1][i]=='T'||array[1][i]=='.')&&(array[2][i]=='O'||array[2][i]=='T'||array[2][i]=='.')&&(array[3][i]=='O'||array[3][i]=='T'||array[3][i]=='.'))
                {
                    cout<<"Case #"<<w<<": Game has not completed\n";
                    d=1;
                    r=1;
                    break;
                }
                if((array[0][i]=='X'||array[0][i]=='T'||array[0][i]=='.')&&(array[1][i]=='X'||array[1][i]=='T'||array[1][i]=='.')&&(array[2][i]=='X'||array[2][i]=='T'||array[2][i]=='.')&&(array[3][i]=='X'||array[3][i]=='T'||array[3][i]=='.'))
                {
                    cout<<"Case #"<<w<<": Game has not completed\n";
                    d=1;
                    r=1;
                    break;
                }
            }
            }
            if(d!=1)
            {
            if((array[0][0]=='O'||array[0][0]=='T'||array[0][0]=='.')&&(array[1][1]=='O'||array[1][1]=='T'||array[1][1]=='.')&&(array[2][2]=='O'||array[2][2]=='T'||array[2][2]=='.')&&(array[3][3]=='O'||array[3][3]=='T'||array[3][3]=='.'))
                {
                    cout<<"Case #"<<w<<": Game has not completed\n";
                    d=1;
                    r=1;
                }
            }
            if(d!=1)
            {
            if((array[0][0]=='X'||array[0][0]=='T'||array[0][0]=='.')&&(array[1][1]=='X'||array[1][1]=='T'||array[1][1]=='.')&&(array[2][2]=='X'||array[2][2]=='T'||array[2][2]=='.')&&(array[3][3]=='X'||array[3][3]=='T'||array[3][3]=='.'))
                {
                    cout<<"Case #"<<w<<": Game has not completed\n";
                    d=1;
                    r=1;
                }
            }
            if(d!=1)
            {
            if((array[3][0]=='O'||array[3][0]=='T'||array[3][0]=='.')&&(array[2][1]=='O'||array[2][1]=='T'||array[2][1]=='.')&&(array[1][2]=='O'||array[1][2]=='T'||array[1][2]=='.')&&(array[0][3]=='O'||array[0][3]=='T'||array[0][3]=='.'))
                {
                    cout<<"Case #"<<w<<": Game has not completed\n";
                    d=1;
                    r=1;
                }
            }
            if(d!=1)
            {
            if((array[3][0]=='X'||array[3][0]=='T'||array[3][0]=='.')&&(array[2][1]=='X'||array[2][1]=='T'||array[2][1]=='.')&&(array[1][2]=='X'||array[1][2]=='T'||array[1][2]=='.')&&(array[0][3]=='X'||array[0][3]=='T'||array[0][3]=='.'))
                {
                    cout<<"Case #"<<w<<": Game has not completed\n";
                    d=1;
                    r=1;
                }
            }
            if(r!=1)
            {
                cout<<"Case #"<<w<<": Draw\n";
            }
        }
        w++;
    }
    return 0;
}
