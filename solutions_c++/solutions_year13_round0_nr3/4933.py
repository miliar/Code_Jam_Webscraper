#include <iostream>
#include <stdint.h>
#include <fstream>
#include <math.h>

using namespace std;

int square_check(int source) {
    float root = sqrt((float)source);

    if(root == (int)root)
        return root;
    else
        return -1;
}

bool fair_check(int source) {
    if(source < 10) {
        return true;
    }
    else if (source < 100) {
        if((source - source % 10)/10 == source % 10)
            return true;
        else
            return false;
    }
    else {
        if((source - source % 100)/100 == source % 10)
            return true;
        else
            return false;
    }
}

int find_one_digit(int start, int finish) {
    int count = 0;
    for(int i = start; i <= finish; i++) {
        if(square_check(i) > 0) {
            count++;
        }
    }
    return count;
}

int find_two_digits(int start, int finish) {
    int count = 0;
    for(int i = start; i <= finish; i++) {
        if(square_check(i) > 0 && ((i - (i % 10))/10 == i % 10)) {
            count++;
        }
    }
    return count;
}

int find_three_digits(int start, int finish) {
    int count = 0;
    for(int i = start; i <= finish; i++) {
        if(square_check(i) > 0 && ((i - (i % 100))/100 == i % 10)) {
            count++;
        }
    }
    return count;
}

int main(int argc, char* argv[])
{

    ifstream sourceFile("./files/C-small-attempt1.in");
    ofstream output("./files/output.txt");

    if (sourceFile.is_open()) {

        int T;
        sourceFile >> T;
        for(int i = 0; i < T; i++) {
            int A, B;
            sourceFile >> A >> B;
            int count = 0;

            for(int j = A; j <= B; j++) {
                if(fair_check(j) && square_check(j) > 0 && fair_check(sqrt(j))) {
                    cout << j << " is fair and square (" << sqrt(j) << ")" << endl;
                    count++;
                }
            }

            output << "Case #" << i + 1 <<": " << count << endl;

        }
        sourceFile.close();
        output.close();
    }

    return 0;
}
