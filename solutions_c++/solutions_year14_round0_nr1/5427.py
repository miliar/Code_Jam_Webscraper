#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ifstream fin( "in.in" );
    ofstream fout( "output.txt" );
    int card1[4][4], card2[4][4],
        i, j, k,
        n, ctr = 0,
        c1, c2,
        original;
    
    fin >> n;
    
    while( ctr < n )
    {
           original = 0;
           fin >> c1;
           for( i=0; i<4; i++ )
                for( j=0; j<4; j++ )
                     fin >> card1[i][j];
           
           fin >> c2;
           for( i=0; i<4; i++ )
                for( j=0; j<4; j++ )
                     fin >> card2[i][j];
           c1--;
           c2--;
           
           for( i=0; i<4; i++ )
                for( j=0; j<4; j++ )
                {
                     if( card1[c1][i] == card2[c2][j] )
                     {
                         k = i;
                         original++;
                     }
                }
           
           if( original == 0 )
               fout << "Case #" << ++ctr << ": Volunteer cheated!\n";
           else if( original == 1 )
               fout << "Case #" << ++ctr << ": " << card1[c1][k] << '\n';
           else
               fout << "Case #" << ++ctr << ": Bad magician!\n";
    }
}
