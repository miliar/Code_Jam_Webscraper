#include <iostream>
#include <cstdio>
#include <vector>
#include <conio.h>
#include <string>

using namespace std;


int provjeri(string red){
int i,j;
int izlaz;
int O_win;
int X_win;
int brojac;

for( j = 0; j < 4; j++ ){

    O_win = 0;
    X_win = 0;

    for( i = 0+4*j ; i < 4+4*j ; i++ )
        if( red[i] != '.' )
            if( red[i] == 'O' ) O_win++;
                else if( red[i] == 'X' ) X_win++;
                else if( red[i] == 'T' ) { O_win++; X_win++; }
// 0 - izjednaceno, 1 - neodigrano, 2 - O win, 3 - X win

        if( X_win == 4 ) return 3;
        if( O_win == 4 ) return 2;

}

for( j = 0; j < 4; j++ ){

    O_win = 0;
    X_win = 0;

    for( i = j ; i < 16 ; i=i+4 )
        if( red[i] != '.' )
            if( red[i] == 'O' ) O_win++;
                else if( red[i] == 'X' ) X_win++;
                else if( red[i] == 'T' ) { O_win++; X_win++; }
// 0 - izjednaceno, 1 - neodigrano, 2 - O win, 3 - X win

        if( X_win == 4 ) return 3;
        if( O_win == 4 ) return 2;

}

    O_win = 0;
    X_win = 0;

for( i = 0; i < 16; i=i+5 )
    if( red[i] == 'O' ) O_win++;
        else if( red[i] == 'X' ) X_win++;
        else if( red[i] == 'T' ) { O_win++; X_win++; }
if( X_win == 4 ) return 3;
if( O_win == 4 ) return 2;



    O_win = 0;
    X_win = 0;

for( i = 3; i < 16; i=i+3 )
    if( red[i] == 'O' ) O_win++;
        else if( red[i] == 'X' ) X_win++;
        else if( red[i] == 'T' ) { O_win++; X_win++; }
if( X_win == 4 ) return 3;
if( O_win == 4 ) return 2;



brojac = 0;
for( i = 0; i < 16; i++ )
    if( red[i] != '.' ) brojac++;

if( brojac == 16 ) return 0;
else return 1;

return izlaz;
}


int main(){
int T;
int i;

string red1;
string red2;
string red3;
string red4;
string redovi;

int izlaz; // 0 - izjednaceno, 1 - neodigrano, 2 - O win, 3 - X win
scanf("%d",&T);

for( i = 0; i < T ; i++ ){

    cin >> red1;
    cin >> red2;
    cin >> red3;
    cin >> red4;

    redovi="";
    redovi+=red1+red2+red3+red4;

    izlaz = provjeri(redovi);
// 0 - izjednaceno, 1 - neodigrano, 2 - O win, 3 - X win

    if( izlaz == 0 ) printf("Case #%d: Draw",i+1);
    if( izlaz == 1 ) printf("Case #%d: Game has not completed",i+1);
    if( izlaz == 2 ) printf("Case #%d: O won",i+1);
    if( izlaz == 3 ) printf("Case #%d: X won",i+1);
}

return 0;
}
