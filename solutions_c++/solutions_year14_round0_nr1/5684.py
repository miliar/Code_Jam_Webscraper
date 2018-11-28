#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char *argv[]) 
{
    int i, j, k, tmp;
    int case_no = 0;
    int this_guess = 0;
    int total_match = 0;
    int final_ans=0;
    int a[5];
    int b[5];
    ifstream fp;

    fp.open(argv[1]);
    if(!fp.is_open()) { cout<<"File open error!"<<endl; }
    
    fp>>case_no;
    for( i = 0 ; i < case_no ; i++ ) {

        total_match = 0;
        final_ans=0;
        fp>>this_guess;
        this_guess--; // adjust index

        // Record first matrix
        for( j = 0 ; j < 4 ; j++) {
            if( j != this_guess ) {
                // bypass row
                for( k = 0 ; k < 4 ; k++) {
                    fp>>tmp;
                }
            } else {
                for( k = 0 ; k < 4 ; k++) {
                    fp>>tmp;
                    a[k] = tmp;
                }
            }
        }
        fp>>this_guess;
        this_guess--; //adjust index

        // Record second matrix
        for( j = 0 ; j < 4 ; j++) {
            if( j != this_guess) {
                for( k = 0 ; k < 4 ; k++) {
                    fp>>tmp;
                }
            } else {
                for( k = 0 ; k < 4 ; k++) {
                    fp>>tmp;
                    b[k] = tmp;
                }
            }
        }

        // Check 2 guesses according to 2 matrices
        for( j = 0 ; j < 4 ; j++) {
            for( k = 0 ; k < 4 ; k++) {
                if( a[j] == b[k] ) {
                    total_match++;
                    final_ans = a[j];
                }
            }
        }
    
        // Report Magic Message
		cout<<"Case #"<<i+1<<": ";
        if( total_match == 1) {
            cout<<final_ans<<endl;
        } else if( total_match == 0 ) {
            cout<<"Volunteer cheated!"<<endl;
        } else {
            cout<<"Bad magician!"<<endl;
        }
    }
    
    fp.close();
    return 0;

}
