#include <iostream>
#include <fstream>
using namespace std;

int main ( )
{
    ifstream input ( "A-small-attempt4.in" );
    ofstream output ( "sub-5.out" );
    
    int test;
    int result;
    int answer;
    input >> test;
    string status = "unchanged";
    
    int array[4][4] , array2[4][4];
    
    for ( int testcase=1 ; testcase<=test ; ++testcase )
    {
        int row1;
        input >> row1;
        
        for ( int row=0 ; row<4 ; row++ ) {
            for ( int col=0 ; col<4 ; col++ ) {
                input >> array[row][col];
            }
        }
        
        int row2;
        input >> row2;
        
        for ( int row=0 ; row<4 ; row++ ) {
            for ( int col=0 ; col<4 ; col++ ) {
                input >> array2[row][col];
            }
        }
        
        
        for ( int col1=0 ; col1<4 ; ++col1 )
        {
            for ( int col2=0 ; col2<4 ; ++col2 )
            {
                if ( array[row1-1][col1] == array2[row2-1][col2] && status == "unchanged" )
                {
                     result = 1;
                     answer = array[row1-1][col1];
                     status = "changed";
                }
                else if ( array[row1-1][col1] == array2[row2-1][col2] && status == "changed" )
                {
                     result = 2;
                }
            }
        }
        
        if ( result == 1 )
        {
             cout << "Case #" << testcase << ": " << answer << endl;
             output << "Case #" << testcase << ": " << answer << endl;
        }
        else if ( result == 2 )
        {
             cout << "Case #" << testcase << ": Bad magician!" << endl;
             output << "Case #" << testcase << ": Bad magician!" << endl;
        }
        else
        {
            cout << "Case #" << testcase << ": Volunteer cheated!" << endl;
            output << "Case #" << testcase << ": Volunteer cheated!" << endl;
        }
        
        status = "unchanged"; 
        result = 0;       
    }
    
    input.close();
    output.close();
    
    system("pause");
}
