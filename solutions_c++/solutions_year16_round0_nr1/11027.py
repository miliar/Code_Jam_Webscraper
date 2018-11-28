#include <iostream>
#include <fstream>

using namespace std;


int main() {

    ofstream fout;
    fout.open("C:\\Users\\User\\ClionProjects\\Google_jam\\answers.txt", ios::out);

    if (!fout.is_open()){
        cout << "can't open" << endl;
    }

    ifstream cin("C:\\Users\\User\\ClionProjects\\Google_jam\\A-large.in");
    int n;
    cin >> n;

    int *cases; //array for cases
    cases = new int[n];

    for (int i = 0; i < n; i++) {
        cin >> cases[i];
    }

    bool digits[10];
    for (int j = 0; j < 10; j++) {
        digits[j] = false;
    }


    for (int i = 0; i < n; i++) { // For all cases
        if (cases[i] != 0){
            int counter = 0; // to know when full digits array will be true
            int increment = 1;
            int output = cases[i];

            while (counter != 10){
                output = increment * cases[i];
                int k = output;
                while (k != 0) { // fill the digits array
                    int c = k % 10;
                    if (digits[c] == false){
                        counter++;
                        digits[c] = true;
                    }
                    k = k / 10;
                }
                increment ++;
            }
            fout << "Case #" << i + 1 << ": " << output << endl;
            for (int j = 0; j < 10; j++) {
                digits[j] = false;
            }
        }
        else {
            fout << "Case #" << i + 1 << ": INSOMNIA" << endl;
        }
    }

    fout.close();

    return 0;
}