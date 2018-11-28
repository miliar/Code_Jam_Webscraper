#include<stdio.h>
#include<algorithm>
#include<iostream>
using namespace std;

char fun()
{
    char s[4][4],ch;
    int a=0,i=0,j=0;

    for(i=0;i<4;i++)    cin>>s[i];

    for(i=0,j=0;i<4;i++)    //row
    {
        ch='.';
        for(j=0;j<4;j++)
        if(s[i][j]=='.')    break;
        else if(s[i][j]!='T')
        {
            ch=s[i][j];
            break;
        }
        for(;j<4;j++)
            if(ch!=s[i][j] && s[i][j]!='T') break;
        if(j==4 && ch!='.')
        {
            //cout<<"Row"<<ch;
            return ch;
        }
    }

    for(j=0;j<4;j++)    //column
    {
        ch='.';
        for(i=0;i<4;i++)
        if(s[i][j]=='.')    break;
        else if(s[i][j]!='T')
        {
            ch=s[i][j];
            break;
        }
        for(;i<4;i++)
            if(s[i][j]!=ch && s[i][j]!='T') break;
        if(i==4 && ch!='.')
        {
            //cout<<"col"<<ch;
            return ch;
        }
    }

    ch='.';
    for(i=0;i<4;i++)    //Diag-1
        if(s[i][i]=='.') break;
        else if(s[i][j]!='T')
        {
            ch=s[i][i];
            break;
        }
    for(;i<4;i++)
        if(s[i][i]!=ch && s[i][j]!='T') break;
    if(i==4 && ch!='.')
    {
        //cout<<"dia1"<<ch;
        return ch;
    }

    ch='.';
    //Diag-2
    for(i=0;i<4;i++)
        if(s[i][3-i]=='.')  break;
        else if(s[i][j]!='T')
        {
            ch=s[i][3-i];
            break;
        }
    for(;i<4;i++)
        if(s[i][3-i]!=ch && s[i][3-i]!='T') break;
    if(i==4 && ch!='.')
    {
        //cout<<"dia2"<<ch;
        return ch;
    }

    for(i=0,j=0;i<4;i++)    //Not completed
        for(j=0;j<4;j++)
        if(s[i][j]=='.')
        {
            return '.';
        }

}

main()
{
    char str[4][25]={"X won","O won","Draw","Game has not completed"};
    int T,c=0,a;
    freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
    cin>>T;
    for(c=1;c<=T;c++)
    {
        char ch=fun();
        if(ch=='X') a=0;
        else if(ch=='O')    a=1;
        else if(ch=='.')    a=3;
        else   a=2;
        cout<<"Case #"<<c<<": "<<str[a]<<endl;
    }
    return 0;
}
