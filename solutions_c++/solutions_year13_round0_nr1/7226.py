#include<iostream>
#include<algorithm>
#include<vector>
#include<stdio.h>

using namespace std;

string result(){

        int i,j,x=0,o=0,flag=0;
        string inp[4];
        for(i=0;i<4;i++)
            cin>>inp[i];

        for(i=0;i<4;i++){
            x=0,o=0;
            for(j=0;j<4;j++){

                if(inp[j][i]=='.')
                    flag=1;
                if(inp[j][i]=='X' || inp[j][i]=='T')
                    x++;
                if(inp[j][i]=='O' || inp[j][i]=='T')
                    o++;
            }

            if(x==4)
                return "X won";
            if(o==4)
                return "O won";

        }

        for(i=0;i<4;i++){
            x=0,o=0;
            for(j=0;j<4;j++){


                if(inp[i][j]=='X' || inp[i][j]=='T')
                    x++;
                if(inp[i][j]=='O' || inp[i][j]=='T')
                    o++;
            }

            if(x==4)
                return "X won";
            if(o==4)
                return "O won";
        }
        x=0,o=0;
        for(i=0;i<4;i++){
            if(inp[i][i]=='X' || inp[i][i]=='T')
                    x++;
                if(inp[i][i]=='O' || inp[i][i]=='T')
                    o++;
        }
        if(x==4)
                return "X won";
            if(o==4)
                return "O won";
        x=0,o=0;
        for(i=0;i<4;i++){
            if(inp[i][3-i]=='X' || inp[i][3-i]=='T')
                    x++;
                 if(inp[i][3-i]=='O' || inp[i][3-i]=='T')
                    o++;
        }
        if(x==4)
                return "X won";
            if(o==4)
                return "O won";

        if(flag)
            return "Game has not completed";
        return "Draw";
}
int main(){

    freopen("out_large.txt","w",stdout);
    freopen("A-large.in","r",stdin);
    int N,M,T;
    cin>>T;

    for(int tt=1;tt<=T;tt++){

        cout<<"Case #"<<tt<<": "<<result()<<endl;

    }
    return 0;
}
