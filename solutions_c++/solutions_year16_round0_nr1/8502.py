#include <iostream>
#include <string>
#include <fstream>
#include <cstdlib>
#include <algorithm>

using namespace std;

int main()
{
    ifstream fin;
    ofstream fout;

    fin.open("A-large.in", ios::in);
    if (!fin.is_open())
    {
        cerr << "Unable to open file 'A-small'" << endl;
        exit(10);
    }

    fout.open("A-large-answer.txt", ios::out);
    if(!fout.is_open())
    {
        cerr << "Unable to open file 'A-small-answer'" << endl;
        exit(10);
    }


    int T, N, numberToDisplay, mod;
    int number = 0;

    fin >> T;

    for (int i=0; i < T; i++){

        fin >> N;

        if (N == 0){
            fout << "Case #" << i+1 << ": INSOMNIA" << endl;
        }
        else{
            int array[10] = {0};
            int j = 0;
            int multiplicationFactor = 1;

            while (j < 10){
                number = N * multiplicationFactor;
                numberToDisplay = number;

                while (number != 0){
                    mod = number % 10;
                    number /= 10;
                    if (mod == 0) {
                        if (array[mod] == 0){
                            array[mod] = 1;
                            j++;
                            mod = 1;
                        }
                    }
                    else if (array[mod] != mod){
                        array [mod] = mod;
                        j++;
                    }
                }
                multiplicationFactor++;
            }
            //cout << "Case #" << i+1 << ": " << numberToDisplay << endl;
            fout << "Case #" << i+1 << ": " << numberToDisplay << endl;
        }
    }

    fin.close();
    fout.close();


    return 0;
}
