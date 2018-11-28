
#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <set>

using namespace std;

/*
unsigned long rotate_unsigned longeger( unsigned long target, unsigned long biggest_power_of_ten )
{
    unsigned long low_digit = target%10;
    return (target/10) + low_digit*biggest_power_of_ten;
    
}
*/

int main( int argc, char ** argv )
{
    fstream input_file;
    input_file.open( argv[1] );
    unsigned long num_lines;
    input_file >> num_lines;

   
    //string current_string;
    // Eat the line that had the number of lines
    //getline( input_file, current_string );

    for (unsigned long i=0; i<num_lines; i++)
    {
        unsigned long initial_radius, paint_amount;
        input_file >> initial_radius >> paint_amount;

        // Ring 1 is (r+1)^2\pi - \pi r^2 = (2r + 1)\pi
        // Ring 2 is (r+3)^2\pi - (r+2)^2\pi = 6r + 9 - 4r - 4 = 2r + 5 \pi
        // Ring 3 is (r+5)^2\pi - (r+4)^2\pi = 10r + 25 - 8r - 16 = 2r + 9
        // Ring n is (r+(2n-1))^2\pi - (r + (2n-2)^2)\pi = (4n - 2)r + 4n^2 - 4n + 1 - [4nr - 4r + 4n^2 - 8n + 4] = 2r + 4n - 3
        //
        // Sum of n rings is 2rn + (4*1 - 3) + (4*2 - 3) + ... + (4*n - 3)
        // That is 2rn + 4*(n(n + 1)/2) - 3n

        unsigned long answer = 1;
        unsigned long n = 1;
        while (2*initial_radius*n + 2*n*(n+1) - 3*n <= paint_amount)
        {
            answer = n;
            n++;
        }


        cout << "Case #" << i+1 << ": " << answer << endl;
        //cout << fixed << setprecision(9) << B << endl;
    }

    input_file.close();

    return 0;

}
