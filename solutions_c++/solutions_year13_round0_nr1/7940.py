#include <iostream>
#include <cstdio>
using namespace std;

char tic[4][4];

bool TicTac(char c)
{
    for(int i=0; i<4; ++i){
        if((tic[i][0]==c || tic[i][0]=='T')&& (tic[i][1]==c || tic[i][1]=='T') && (tic[i][2]==c || tic[i][2]=='T') && (tic[i][3]==c || tic[i][3]=='T'))
            return true;
        if((tic[0][i]==c || tic[0][i]=='T')&& (tic[1][i]==c || tic[1][i]=='T') && (tic[2][i]==c || tic[2][i]=='T') && (tic[3][i]==c || tic[3][i]=='T'))
            return true;
    }
    if((tic[0][0]==c || tic[0][0]=='T') && (tic[1][1]==c || tic[1][1]=='T') && (tic[2][2]==c || tic[2][2]=='T') && (tic[3][3]==c || tic[3][3]=='T'))
        return true;
    if((tic[0][3]==c || tic[0][3]=='T') && (tic[1][2]==c || tic[1][2]=='T') && (tic[2][1]==c || tic[2][1]=='T') && (tic[3][0]==c || tic[3][0]=='T'))
        return true;
    return false;
}

bool if_dian()
{
    for(int i=0; i<4; ++i)
        for(int j=0; j<4; ++j)
            if(tic[i][j]=='.')
                return true;
    return false;
}

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int n;
    cin>>n;
    for(int k=1; k<=n; ++k){
        printf("Case #%d: ",k);
        for(int i=0; i<4; ++i){
            for(int j=0; j<4; ++j)
               cin>>tic[i][j];
        }
        if(TicTac('X'))
            printf("X won\n");
        else if(TicTac('O'))
            printf("O won\n");
        else{
            if(if_dian())
                printf("Game has not completed\n");
            else
                printf("Draw\n");
        }



    }


}
