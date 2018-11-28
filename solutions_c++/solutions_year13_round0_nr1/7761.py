#include<iostream>
#include<cstdio>
#include<string>
#include<vector>

using namespace std;

vector<string> sav(4);

void read(void);
void output(int);
bool win(char);
bool fin(void);
int main()
{
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);


    int G;
    int n;

    cin>>G;

    n=G;

    while(n--)
    {
        read();
        output(G-n);
    }

    return 0;
}

void read()
{
    for(int i=0;i<4;++i)
        cin>>sav[i];

    return;
}


bool win(char J)
{
    vector<string> S(4);
    S=sav;
    bool key=false;

    string C;

    for(int i=0;i<4;++i)
        C.push_back(J);

    for(int i=0;i<4;++i)
        for(int j=0;j<4;++j)
            if(S[i][j]=='T')
                S[i][j]=J;

    for(int i=0;i<4;++i)
        if(S[i]==C)
            return true;

    for(int i=0;i<4;++i)
        if(S[0][i]==J && S[1][i]==J && S[2][i]==J && S[3][i]==J)
            return true;

    if(S[0][0]==J && S[1][1]==J && S[2][2]==J && S[3][3]==J)
        return true;

    if(S[0][3]==J && S[1][2]==J && S[2][1]==J && S[3][0]==J)
        return true;


    return false;
}

void output(int n)
{
    printf("Case #%d: ",n);

    if(win('O'))
        puts("O won");
    else if(win('X'))
        puts("X won");
    else if(fin())
        puts("Draw");
    else
        puts("Game has not completed");

    return;
}

bool fin()
{
    for(int i=0;i<4;++i)
        for(int j=0;j<4;++j)
            if(sav[i][j]=='.')
                return false;

    return true;
}
