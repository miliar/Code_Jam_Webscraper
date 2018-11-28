#include <iostream>

using namespace std;
string s[4];

bool f (char i,char x){
    if ( i == x || i == 'T' ) return true;
    return false;
}
int main (){
    int t;
    cin >> t;
    int p = 1;
    while(t){
    t--;
        bool kh = false;
        for ( int i=0;i<4;i++){
            cin >> s[i];
            for( int j=0;j<4;j++) if( s[i][j] == '.' ) kh = true;
        }
        char ans = -1;
        for(int i=0;i<4;i++){
            if( f (s[i][0],'X') &&  f (s[i][1],'X') && f (s[i][2],'X') && f (s[i][3],'X') ) ans = 'X';
            if( f (s[i][0],'O') &&  f (s[i][1],'O') && f (s[i][2],'O') && f (s[i][3],'O') ) ans = 'O';
        }
        for(int i=0;i<4;i++){
            if( f (s[0][i],'X') &&  f (s[1][i],'X') && f (s[2][i],'X') && f (s[3][i],'X') ) ans = 'X';
            if( f (s[0][i],'O') &&  f (s[1][i],'O') && f (s[2][i],'O') && f (s[3][i],'O') ) ans = 'O';
        }   
        bool b = true;
        for(int i=0;i<4;i++){
            if( !f(s[i][i],'X') ) b = false;
        }
        if ( b ) ans = 'X';
        
        b = true;
        for(int i=0;i<4;i++){
            if( !f(s[i][3-i],'X') ) b   = false;
        }
        if ( b ) ans = 'X';
        
        b = true;
        for(int i=0;i<4;i++){
            if( !f(s[i][i],'O') ) b = false;
        }
        if ( b ) ans = 'O';
        
        b = true;
        for(int i=0;i<4;i++){
            if( !f(s[i][3-i],'O') ) b   = false;
        }
        if ( b ) ans = 'O';
        cout << "Case #"<< p << ": ";
        p++;
        if ( ans == -1 ){
            if( kh == false ) cout << "Draw\n";
            else cout << "Game has not completed\n";
        }
        else cout << ans << " won\n";
    }
}
