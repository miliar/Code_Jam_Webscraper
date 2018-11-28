#include <iostream>
#include <fstream>
#include <string>
#include <cmath>

using namespace std;

ifstream fin("C.in");
ofstream fout("C.out");

int T;
string A, B;

bool palindrome(long N) {
    string SN = to_string(N);
    for(int i=0; i< SN.size()/2; i++) {
        if(SN[i] != SN[SN.size()-i-1])
            return false;
    }
    return true;
}

int main() {
    fin >> T;
    for(int it=1; it <= T; it++) {
        fin >> A >> B;
        long a= stol(A), b=stol(B);
        long rtA = sqrt(a), rtB = sqrt(b);
        rtA = (rtA*rtA == a)? rtA: rtA+1;
        long count = 0;
        for(int i=rtA; i<=rtB; i++) {
            if(palindrome(i) && palindrome(i*i))   
                count++;
        }
        
        fout << "Case #" << it << ": " << count << endl;
    }
}
