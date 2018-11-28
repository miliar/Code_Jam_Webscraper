#include <iostream>
#include <cstring>
#include <cstdlib>
using namespace std;

int main()
{
    bool xbit[4][4];
    bool obit[4][4];
    bool tbit[4][4];
    int t;
    char c;
    int cont = 1;
    
    cin >> t;
    while(t>0){
        memset(xbit,0,sizeof(xbit));
        memset(obit,0,sizeof(obit));
        memset(tbit,0,sizeof(tbit));
        
        bool unend = 0;
        int final = 0;
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
               cin >> c;
               if(c=='X')
                   xbit[i][j] = 1;
               else if(c=='O')
                   obit[i][j] = 1;
               else if(c=='T')
                   tbit[i][j] = 1;
               else if(c=='.')
                   unend = 1;
            }
        }
        
        bool xwin = 1;
        bool owin = 1;
        for(int i=0;i<4;i++){
            xwin = 1;
            owin = 1;
            for(int j=0;j<4;j++){
                xwin = xwin & (xbit[i][j] | tbit[i][j]);
                owin = owin & (obit[i][j] | tbit[i][j]);
            }
            if(xwin){
                final = 1;
            }
            if(owin){
                final = 2;
            }
        }

        for(int j=0;j<4;j++){
            xwin = 1;
            owin = 1;
            for(int i=0;i<4;i++){
                xwin = xwin & (xbit[i][j] | tbit[i][j]);
                owin = owin & (obit[i][j] | tbit[i][j]);
            }
            if(xwin){
                final = 1;
            }
            if(owin){
                final = 2;
            }
        }

        xwin = 1;
        owin = 1;
        for(int i=0;i<4;i++){
            xwin = xwin & (xbit[i][i] | tbit[i][i]);
            owin = owin & (obit[i][i] | tbit[i][i]);
        }
        if(xwin){
            final = 1;
        }
        if(owin){
            final = 2;
        }
        
        xwin = 1;
        owin = 1;
        for(int i=0;i<4;i++){
            xwin = xwin & (xbit[i][3-i] | tbit[i][3-i]);
            owin = owin & (obit[i][3-i] | tbit[i][3-i]);
        }
        if(xwin){
            final = 1;
        }
        if(owin){
            final = 2;
        }
        
        if(final==1){
            cout << "Case #"<< cont <<": X won" << endl;
        }else if(final==2){
            cout << "Case #"<< cont <<": O won" << endl;
        }else if(unend){
            cout << "Case #" << cont << ": Game has not completed" << endl;
        }else{
            cout << "Case #" << cont << ": Draw" << endl;
        }
        
        t--;
        cont++;
    }
    return 0;
}
