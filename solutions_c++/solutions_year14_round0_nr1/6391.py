#include "cstdio"
#include "cmath"
#include "cstdlib"
#include "iostream"

using namespace std;

int cartas1[5][5];
int cartas2[5][5];

int main(){
 
 freopen("A-small-attempt0.in", "r",stdin);
 freopen("A-small-attempt0.out","w",stdout);
 
 int t;
 cin >> t;
 for ( int caso = 1; caso <= t; caso++ ){
    int a1, a2;
    cin >> a1;
    for ( int i = 0; i < 4; i++ ) 
        for ( int j = 0; j < 4; j++ )
            cin >> cartas1[i][j];   
    cin >> a2;
    for ( int i = 0; i < 4; i++ ) 
        for ( int j = 0; j < 4; j++ )
            cin >> cartas2[i][j];               
             
    int cantidad = 0, respuesta = -1;
    for ( int i = 0; i < 4; i++ )
        for ( int j = 0; j < 4; j++ )
            if ( cartas1[a1-1][i] == cartas2[a2-1][j] ){
               ++cantidad;
               respuesta = cartas1[a1-1][i];
               break;
            }
       
    cout << "Case #" << caso << ": ";     
    if ( cantidad == 0 )
       cout << "Volunteer cheated!" << endl;
    else if ( cantidad == 1 )
       cout << respuesta << endl; 
    else
       cout << "Bad magician!" << endl;     
 }//fcaso
 
 return 0;   
}//fp
