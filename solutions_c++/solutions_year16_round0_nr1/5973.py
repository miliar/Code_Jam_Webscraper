#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

int getDigit(int, int);

int main(int argc, char* argv[]){
    ifstream inputStream ("A-large.in");
    ofstream outputStream ("output.txt");
    int cases;
    int currentCase;

    if(inputStream.is_open()){
        cout << "Input Stream opened\n";

        // Get Case Count
        inputStream >> cases;

        // Iterate Through Cases
        for(int c = 0; c < cases; c++){
            bool done = false;
            bool insomnia = false;
            int counter = 1;
            int current_value;
            int lastDigit;
            int old_value;
            int found_count = 0;
            bool found[10];

            for(int f = 0; f < sizeof(found); f++)
                found[f] = false;

            inputStream >> currentCase;

            while(!done){
                old_value = current_value;
                current_value = counter * currentCase;

                if(old_value && current_value == old_value){
                    done = true;
                    insomnia = true;
                }else if(counter > 10000){
                    done = true;
                    insomnia = true;
                    cout << "limit reached.\n";
                }

                int flat = current_value;
                int num_digits;
                double test = log10(flat);

                if(floor(test) == test){
                    num_digits = ceil(test) + 1;
                }else{
                    num_digits = ceil(test);
                }

                for(int d = 1; d <= num_digits; d++){
                    int curr_digit = getDigit(flat, d);

                    cout << "\t\tdigit " << curr_digit << " at " << d << " in " << current_value << "\n";

                    lastDigit = curr_digit;

                    if(!(found[curr_digit])){
                        found[curr_digit] = true;

                        found_count += 1;

                        cout << "\tFound Digit " << curr_digit << " in " << current_value << "\n";
                    }

                    if(found_count >= 10){
                        done = true;
                        break;
                    }
                }

                counter += 1;
            }

            if(insomnia){
                cout << "Last Digit: INSOMNIA\n";
                outputStream << "Case #" << (c + 1) << ": INSOMNIA\n";
            }else{
                cout << "Last Digit: " << current_value << "\n";
                outputStream << "Case #" << (c + 1) << ": " << current_value << "\n";
            }
        }
    }else{
        cout << "Cannot open input stream\n";
    }

    inputStream.close();
    outputStream.close();

    return 0;
}

int getDigit(int value, int positionFromLeft)
{
    int posFromRight = 1;
    {
        int v = value;
        while (v /= 10)
            ++posFromRight;
    }
    posFromRight -= positionFromLeft - 1;
    while (--posFromRight)
        value /= 10;
    value %= 10;
    return value > 0 ? value : -value;
}
