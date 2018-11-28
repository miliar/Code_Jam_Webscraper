#include <iostream>
#include <string>
#include <fstream>
using namespace std;

const string insomnia = "INSOMNIA";

bool seen_all_digits(int seen[], int n)
{

    for(int i = 0; i < n; i++) {
        if(seen[i] == 0) 
            return false;
    }
    return true;
}

void reset(int seen[], int n)
{
    for(int i = 0; i < n; i++) 
        seen[i] = 0;
}

int main()
{
    int test_cases;
    int test_input;
    int seen[10] = {0};

    ifstream infile("A-large.in");
    if(!infile) {
        cerr << " Could not read input file" << endl;
        return 0;
    }

    infile >> test_cases;
    for(int i = 1; i <= test_cases; i++) {
        infile >> test_input;
        
        int temp = test_input;
        if(test_input == 0) {
            cout << "Case #"<<i<<": INSOMNIA" << endl;
            continue;
        }

        int j = 0;
        int last_digit = 0;
        do {
            ++j;
            temp = test_input * j;
            // get each digit from input
            do {
                last_digit = temp % 10;
                //cout << last_digit << endl;
                temp = temp/10;

                if(seen[last_digit] == 0) 
                    ++seen[last_digit];
            } while( temp > 0);

        } while(!seen_all_digits(seen, 10));
        
        // check if we have seen all the digits
        if(seen_all_digits(seen,10)) {
            cout << "Case #" << i << ": " << test_input * j << endl;
        }
        
        reset(seen, 10);

    }
    return 0;
}
