#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <deque>
#include <algorithm>
#include <math.h>
#include <sstream>
using namespace std;

bool check(double temp){
    ostringstream strs;
    strs << temp;
    string square = strs.str();
    for(int i = 0; i < square.size()/2; i++){
        if(square.substr(i, 1) != square.substr(square.size() - i - 1, 1)){
            return false;
        }
    }
    return true;
}

int counter(double A, double B){
    int counter = 0;
    for(double i = A; i <= B; i++){
        if(check(i)){
            double temp = i * i;
            if(check(temp)){
                counter++;
            }
        }
    }
    return counter;
}

int main(){
    ofstream fout ("palindrome.out");
    ifstream fin ("palindrome.in");
    int N;
    fin >> N;
    for(int i = 0; i < N; i++){
        double A, B;
        fin >> A >> B;
        A = ceil(sqrt(A));
        B = floor(sqrt(B));
        int sol = counter(A, B);
        fout << "Case #" << (i + 1) << ": " << sol << endl;
    }
}
