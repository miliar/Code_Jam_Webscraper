#include<iostream>
#include<fstream>
#include<vector>
#include<math.h>

using namespace std;
vector<int> primes(10000000);
int Divisor(unsigned long temp) {
    for (int i = 0; (primes[i] * primes[i]) < temp; i++) {
        if (temp % primes[i] == 0)
            return primes[i];
    }
    return -1;
}
void proceed(int num, int N, int J) {
    ofstream outfile;
    outfile.open("/Users/mac/code/c++/cj3_output7.txt",
                 ios::out | ios::app);
    outfile << "Case #"<< num <<": "<< endl;
    int count = 0;
    unsigned long temp = 0;
    vector<int> divisors(9 , 0);
    bool isJam = true;
    string jamcheck(N, '1');
    for (unsigned long i = 0; i < pow(2, N-2); i++) {
        isJam = true;
        temp = i; // generate a check number
        for (int j = N - 2; j > 0; j--) {
            if (temp % 2) {
                jamcheck[j] = '1';
            } else {
                jamcheck[j] = '0';
            }
            temp = temp / 2;
        }
        // composite jamcheck ready

        cout << "str= " << jamcheck <<"N="<<N<< endl;
        // begin to check if it is jam coin
        for (int base = 2; base < 11; base++) { // base by base check
            cout << "base = " << base;
            temp = 0; // initialize middle value
            for (int k = N - 1; k >= 0; k--) { // digit by digit separate
                if (jamcheck[k] == '1')
                    temp += pow(base, N - 1 - k);
            }
            // after one base sum, then began check divisor
            cout << " num="<<temp << " ";
            int dvs = Divisor(temp);
            if (dvs == -1) {
                isJam = false;
                break;
            } else {
                divisors[base-2] = dvs; // store the divisor
            }
            cout << endl;
            if (!isJam) break; // this number is not jam coin
        } // end base by base check
        if (isJam) { // if it is a jam coin then print
            outfile << jamcheck <<" ";
            for (int i = 0; i < 9; i++) {
                outfile << divisors[i] << " ";
            }
            outfile << endl;
            count++;
            if (count == J) return;
        }
    } // end check one number move to next
} // end proceed

int main() {
    ifstream infile;
    infile.open("/Users/mac/code/c++/C-small-attempt1.in");
    if (infile.fail()) cout << "open file fail" <<endl;
    ifstream infile2;
    infile2.open("/Users/mac/code/c++/primes.txt");
    if (infile2.fail()) cout << "open prime file fail" <<endl;
    int prime;
    for (int i = 0; i < 10000000; i++) {
        infile2 >> prime;
        primes[i] = prime;
    }
    int num = 0, N = 0, J = 0;
    infile >> num;
    for (int k = 0; k < num; k++) {
        infile >> N;
        infile >> J;
        proceed(k+1, N, J);
    }
    infile.close();
    return 0;
}
