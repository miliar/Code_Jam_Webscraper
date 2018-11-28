#include <iostream> 
#include <fstream>

using namespace std;

// Start includes & defs
#define X "X won"
#define O "O won"
#define D "Draw"
#define G "Game has not completed"

// End include  & defs

int main (int argc, char** argv)
{
    ifstream read;
    read.open(argv[1]);

    ofstream write;
    write.open(argv[2]);

    int noOfTest = -1;
    read >> noOfTest;

    int n = 1;

    while ( n <= noOfTest )
    {
        // Start code ... 
        int res = -1;

        char c00, c01, c02, c03;
        char c10, c11, c12, c13;
        char c20, c21, c22, c23;
        char c30, c31, c32, c33;
        char dummy;

        read >> c00 >> c01 >> c02 >> c03;
        read >> c10 >> c11 >> c12 >> c13;
        read >> c20 >> c21 >> c22 >> c23;
        read >> c30 >> c31 >> c32 >> c33;
        read.get(dummy);

        //x row
        if ( ( res == -1) and  (
                    (c00 == 'X' or c00 == 'T') 
                    and (c01 == 'X' or c01 == 'T')    
                    and (c02 == 'X' or c02 == 'T')    
                    and (c03 == 'X' or c03 == 'T')    
             ) or
                (
                 (c10 == 'X' or c10 == 'T') 
                 and (c11 == 'X' or c11 == 'T')    
                 and (c12 == 'X' or c12 == 'T')    
                 and (c13 == 'X' or c13 == 'T')    
                ) or
                (
                 (c20 == 'X' or c20 == 'T') 
                 and (c21 == 'X' or c21 == 'T')    
                 and (c22 == 'X' or c22 == 'T')    
                 and (c23 == 'X' or c03 == 'T')    
                ) or
                (
                 (c30 == 'X' or c30 == 'T') 
                 and (c31 == 'X' or c31 == 'T')    
                 and (c32 == 'X' or c32 == 'T')    
                 and (c33 == 'X' or c33 == 'T')    
                )
            )
        {
            res = 0;
        }

        //x col
        if ( ( res == -1 ) and (
                    (c00 == 'X' or c00 == 'T') 
                    and (c10 == 'X' or c10 == 'T')    
                    and (c20 == 'X' or c20 == 'T')    
                    and (c30 == 'X' or c30 == 'T')    
             ) or
                (
                 (c01 == 'X' or c01 == 'T') 
                 and (c11 == 'X' or c11 == 'T')    
                 and (c21 == 'X' or c21 == 'T')    
                 and (c31 == 'X' or c31 == 'T')    
                ) or
                (
                 (c02 == 'X' or c02 == 'T') 
                 and (c12 == 'X' or c12 == 'T')    
                 and (c22 == 'X' or c22 == 'T')    
                 and (c32 == 'X' or c32 == 'T')    
                ) or
                (
                 (c03 == 'X' or c03 == 'T') 
                 and (c13 == 'X' or c13 == 'T')    
                 and (c23 == 'X' or c23 == 'T')    
                 and (c33 == 'X' or c33 == 'T')    
                )
            )
        {
            res = 0;
        }

        // x dgl
        if ( ( res == -1 ) and  (
                    (c00 == 'X' or c00 == 'T') 
                    and (c11 == 'X' or c11 == 'T')    
                    and (c22 == 'X' or c22 == 'T')    
                    and (c33 == 'X' or c33 == 'T')    
             ) or
                (
                 (c03 == 'X' or c03 == 'T') 
                 and (c12 == 'X' or c12 == 'T')    
                 and (c21 == 'X' or c21 == 'T')    
                 and (c30 == 'X' or c30 == 'T')    
                ) 
                
            )
        {
            res = 0;
        }



        //o row
        if ( ( res == -1 ) and (
                    (c00 == 'O' or c00 == 'T') 
                    and (c01 == 'O' or c01 == 'T')    
                    and (c02 == 'O' or c02 == 'T')    
                    and (c03 == 'O' or c03 == 'T')    
             ) or
                (
                 (c10 == 'O' or c10 == 'T') 
                 and (c11 == 'O' or c11 == 'T')    
                 and (c12 == 'O' or c12 == 'T')    
                 and (c13 == 'O' or c13 == 'T')    
                ) or
                (
                 (c20 == 'O' or c20 == 'T') 
                 and (c21 == 'O' or c21 == 'T')    
                 and (c22 == 'O' or c22 == 'T')    
                 and (c23 == 'O' or c03 == 'T')    
                ) or
                (
                 (c30 == 'O' or c30 == 'T') 
                 and (c31 == 'O' or c31 == 'T')    
                 and (c32 == 'O' or c32 == 'T')    
                 and (c33 == 'O' or c33 == 'T')    
                )
            )
        {
            res = 1;
        }


        //o col
        if ( ( res == -1) and (
                    (c00 == 'O' or c00 == 'T') 
                    and (c10 == 'O' or c10 == 'T')    
                    and (c20 == 'O' or c20 == 'T')    
                    and (c30 == 'O' or c30 == 'T')    
             ) or
                (
                 (c01 == 'O' or c01 == 'T') 
                 and (c11 == 'O' or c11 == 'T')    
                 and (c21 == 'O' or c21 == 'T')    
                 and (c31 == 'O' or c31 == 'T')    
                ) or
                (
                 (c02 == 'O' or c02 == 'T') 
                 and (c12 == 'O' or c12 == 'T')    
                 and (c22 == 'O' or c22 == 'T')    
                 and (c32 == 'O' or c32 == 'T')    
                ) or
                (
                 (c03 == 'O' or c03 == 'T') 
                 and (c13 == 'O' or c13 == 'T')    
                 and (c23 == 'O' or c23 == 'T')    
                 and (c33 == 'O' or c33 == 'T')    
                )
            )
        {
            res = 1;
        }

        // o dgl
        if ( ( res == -1 ) and  (
                    (c00 == 'O' or c00 == 'T') 
                    and (c11 == 'O' or c11 == 'T')    
                    and (c22 == 'O' or c22 == 'T')    
                    and (c33 == 'O' or c33 == 'T')    
             ) or
                (
                 (c03 == 'O' or c03 == 'T') 
                 and (c12 == 'O' or c12 == 'T')    
                 and (c21 == 'O' or c21 == 'T')    
                 and (c30 == 'O' or c30 == 'T')    
                ) 
                
            )
        {
            res = 1;
        }

        if (( res == -1 ) and (
                    (c00 == '.' ) or
                    (c01 == '.' ) or
                    (c02 == '.' ) or
                    (c03 == '.' ) or
                    (c10 == '.' ) or
                    (c11 == '.' ) or
                    (c12 == '.' ) or
                    (c13 == '.' ) or
                    (c20 == '.' ) or
                    (c21 == '.' ) or
                    (c22 == '.' ) or
                    (c23 == '.' ) or
                    (c30 == '.' ) or
                    (c31 == '.' ) or
                    (c32 == '.' ) or
                    (c33 == '.' ) 
                    ))
        {
            res = 3;
        }

        // End code ...
        if ( res == 0 )
            write << "Case #" << n << ": " << X << endl;
        else if ( res == 1 )
            write << "Case #" << n << ": " << O << endl;
        else if ( res == 3 )
            write << "Case #" << n << ": " << G << endl;
        else 
            write << "Case #" << n << ": " << D << endl;
        ++n;
    }

    read.close();
    write.close();
    return 0;
}
