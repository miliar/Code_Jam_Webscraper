#include <iostream>
using namespace std;

int main() {
    int t,x,o;
    cin>>t;
    string tab[4];
    int win;
    int xk[4], ok[4], wnd[4];
    bool nd;
    for(int i=1;i<=t;i++) {
        nd=false;
        for(int j=0;j<4;j++) {
            xk[j]=0;
            ok[j]=0;
            wnd[j]=0;
            cin>>tab[j];
            }
        win=0;
        for(int j=0;j<4;j++) {
            x=0;o=0;
            for(int k=0;k<4;k++) {
                if(tab[j][k]=='X') { xk[k]++; x++; }
                else if(tab[j][k]=='O') { ok[k]++; o++; }
                else if(tab[j][k]=='T') { ok[k]++; xk[k]++; x++; o++; }
                }
            if (x==4) win=1;
            else if(o==4) win=2;

            if(win>0) break;
            }
        if(win==0) {
            for(int j=0;j<4;j++) {
                if(xk[j]==4) { win=1; break; }
                if(ok[j]==4) { win=2; break; }
                }
            }
        if(win==0) {
            x=0;o=0;
            for(int j=0;j<4;j++) {
                if(tab[j][j]=='X') x++;
                else if(tab[j][j]=='O') o++;
                else if(tab[j][j]=='T') { x++; o++; }
                }
            if (x==4) win=1;
            else if(o==4) win=2;
            }

        if(win==0) {
            x=0;o=0;
            for(int j=0;j<4;j++) {
                if(tab[j][3-j]=='X') x++;
                else if(tab[j][3-j]=='O') o++;
                else if(tab[j][3-j]=='T') { x++; o++; }
                }
            if (x==4) win=1;
            else if(o==4) win=2;
            }

        bool jk;
        if(win==0) {
            for(int j=0;j<4;j++) {
                jk=false;
                for(int k=0;k<4;k++) {
                    if(tab[j][k]=='X') {
                        if((wnd[j]==0) || (wnd[j]==1)) wnd[j]=1;
                        else wnd[j]=3;
                        }
                    if(tab[j][k]=='O') {
                        if((wnd[j]==0) || (wnd[j]==2)) wnd[j]=2;
                        else wnd[j]=3;
                        }
                    if(tab[j][k]=='.') jk=true;
                    }
                if((wnd[j]!=3) && (jk==true)) { win=-1; break; }
                }
            }
        for(int j=0;j<4;j++) wnd[j]=0;
        if(win==0) {
            for(int j=0;j<4;j++) {
                jk=false;
                for(int k=0;k<4;k++) {
                    if(tab[k][j]=='X') {
                        if((wnd[j]==0) || (wnd[j]==1)) wnd[j]=1;
                        else wnd[j]=3;
                        }
                    if(tab[k][j]=='O') {
                        if((wnd[j]==0) || (wnd[j]==2)) wnd[j]=2;
                        else wnd[j]=3;
                        }
                    if(tab[k][j]=='.') jk=true;
                    }
                if((wnd[j]!=3) && (jk==true)) { win=-1; break; }
                }
            }
        if(win==0) {
            wnd[0]=0;
            jk=false;
            for(int j=0;j<4;j++) {
                if(tab[j][j]=='X') {
                    if((wnd[0]==0) || (wnd[0]==1)) wnd[0]=1;
                    else wnd[0]=3;
                    }

                if(tab[j][j]=='O') {
                    if((wnd[0]==0) || (wnd[0]==2)) wnd[0]=2;
                    else wnd[0]=3;
                    }

                if(tab[j][j]=='.') jk=true;
                }
            if((wnd[0]!=3) && (jk==true)) win=-1;
            }

        if(win==0) {
            wnd[0]=0;
            jk=false;
            for(int j=0;j<4;j++) {
                if(tab[j][j-3]=='X') {
                    if((wnd[0]==0) || (wnd[0]==1)) wnd[0]=1;
                    else wnd[0]=3;
                    }

                if(tab[j][j-3]=='O') {
                    if((wnd[0]==0) || (wnd[0]==2)) wnd[0]=2;
                    else wnd[0]=3;
                    }

                if(tab[j][j-3]=='.') jk=true;
                }
            if((wnd[0]!=3) && (jk==true)) win=-1;
            }

        cout << "Case #" << i << ": ";
        switch(win) {
            case -1:
                cout << "Game has not completed";
                break;
            case 0:
                cout << "Draw";
                break;
            case 1:
                cout << "X won";
                break;
            case 2:
                cout << "O won";
                break;
            }
        cout << endl;
        }
    return 0;
}
