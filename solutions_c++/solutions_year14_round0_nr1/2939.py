#include <iostream>
#include <fstream>
#include <string>

int main(int argc, const char *argv[])
{
    std::fstream fin( argv[1] );

    int cases;
    fin >> cases;
    for( int i = 1; i <= cases; i++ ){
        std::cout << "Case #" << i << ": ";
        int ans1, ans2;
        int grid1[16], grid2[16];
        fin >> ans1;
        for( int j = 0; j < 16; j++ )
            fin >> grid1[j];
        fin >> ans2;
        for( int j = 0; j < 16; j++ )
            fin >> grid2[j];
        int matches = 0;
        int card = 0;
        ans1--;
        ans2--;
        for( int c1 = 0; c1 < 4; c1++ )
            for( int c2 = 0; c2 < 4; c2++ ){
                if( grid1[ ans1 * 4 + c1 ] == grid2[ ans2 * 4 + c2 ] ){
                    card = grid1 [ ans1 * 4 + c1 ]; 
                    matches++;
                }
            }
        switch( matches ){
            case 0:
                std::cout << "Volunteer cheated!" << std::endl;
                break;
            case 1:
                std::cout << card << std::endl;
                break;
            default:
                std::cout << "Bad magician!" << std::endl;
                break;
        }
    }
    
    
    return 0;
}
