#include <iostream>
#include <string>
#include <cstring>
#include <cstdio>
#include <vector>
using namespace std;

int pos;
int com(string st)
{
    pos = -1;
    string tmp[] = {"TOOO","OTOO","OOTO","OOOT","OOOO","TXXX", "XTXX", "XXTX", "XXXT", "XXXX" };
    for(int i=0;i<10;i++)
        if(st.compare(tmp[i])==0) pos=i;
    return pos;
}

int main()
{
    int t,f;
    scanf("%d",&t);

    bool X,O,D,N;

    for(int i=1;i<=t;i++)
    {
        char board[4][4];
        X = O = D = N = false;

        //input
        for(int ii=0;ii<4;ii++)
            for(int jj=0;jj<4;jj++)
                cin >> board[ii][jj];

        //Check for horizontal patterns
        for(int ii=0;ii<4;ii++)
        {
            string hr = "";
            for(int jj=0;jj<4;jj++)
                hr += board[ii][jj];

            f = com(hr);
            if(f!=-1)
                if(f<=4) O = true;
                else X = true;
        }


        printf("Case #%d: ",i);

        //Check for vertical patterns
        if(!O && !X){
            string vr="";
            for(int ii=0;ii<4;ii++)
            {
                vr = "";
                for(int jj=0;jj<4;jj++)
                    vr += board[jj][ii];
                f = com(vr);
                if(f!=-1)
                    if(f<=4) O = true;
                    else X = true;
            }
        }

        //Check for Diagonals
        if(!O && !X){
        string dg="";
        for(int ii=0;ii<4;ii++)
            dg += board[ii][ii];

        f = com(dg);
        if(f!=-1)
            if(f<=4) O = true;
            else X = true;

        dg = "";
        for(int ii=0,jj=3;ii<4;ii++,jj--)
            dg += board[jj][ii];

        f = com(dg);
        if(f!=-1)
            if(f<=4) O = true;
            else X = true;
        }

       //Check for "NOT COMPLETED"
        for(int ii=0;ii<4;ii++)
            for(int jj=0;jj<4;jj++)
                if(board[ii][jj]=='.') N = true;

        if(X) printf("X won\n");
        else if(O) printf("O won\n");
        else if(N) printf("Game has not completed\n");
        else printf("Draw\n");
    }
    return 0;
}
