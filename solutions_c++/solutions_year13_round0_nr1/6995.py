#include<iostream>
#include<cstdio>
#include<vector>
#include<cmath>
#include<cstring>
#include<set>
#include<sstream>
#include<string>
#include<algorithm>
#include<map>
#include<stack>
#include<queue>

using namespace std;

string str[4];

bool tic(char ch)
{
    bool flag;
    for(int i=0;i<4;i++)
    {
        flag=true;
        for(int j=0;j<4;j++)
        {
            if(!(str[i][j]==ch || str[i][j]=='T')){flag=false;break;}
        }
        if(flag)return true;
    }
    for(int i=0;i<4;i++)
    {
        flag=true;
        for(int j=0;j<4;j++)
        {
            if(!(str[j][i]==ch || str[j][i]=='T')){flag=false;break;}
        }
        if(flag)return true;
    }
    flag=true;
    for(int i=0;i<4;i++)
        if(!(str[i][i]==ch || str[i][i]=='T')){flag=false;break;}
    if(flag)return true;
    flag=true;
    int j=3;
    for(int i=0;i<4;i++)
        {
            if(!(str[i][j]==ch || str[i][j]=='T')){flag=false;break;}
            j--;
        }
    if(flag)return true;
    return false;

}

int main()
{
    ios_base::sync_with_stdio(false);
    freopen("A-large.in","r",stdin);
    freopen("A.out","w",stdout);
    int t,test=0;

    cin>>t;

    while(t--)
    {
        cin>>str[0]>>str[1]>>str[2]>>str[3];

        bool dot=false;

        for(int i=0;i<4;i++)for(int j=0;j<4;j++)if(str[i][j]=='.'){dot=true;break;}
        bool x=tic('X');
        bool o=tic('O');
        cout<<"Case #"<<++test<<": ";

        if(x)cout<<"X won"<<endl;
        else if(o)cout<<"O won"<<endl;
        else if(dot)cout<<"Game has not completed"<<endl;
        else cout<<"Draw"<<endl;

    }





    return 0;

}
