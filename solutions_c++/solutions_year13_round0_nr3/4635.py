#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <math.h>

using namespace std;


bool pal(long n){
    int length = log10(n) + 1;
    for (int i = 0; i < length / 2; i++){
        int x = n % (int)pow(10, i + 1) / (int)pow(10, i);
        int y = n % (int)pow(10, length - i) / (int)pow(10, length - i - 1);
        if (x != y) return false;
    }
    return true;
}

int count(long int a, long int b){
    int total = 0;
    for (long int i = a; i <= b; i++) {
        long int ir = sqrt(i);
        float fr = sqrt(i);
        if (ir == fr && pal(i) && pal((long int)sqrt(i))) total ++;
    }
    return total;
}

int main(){
    int size;
    ifstream fin;
    ofstream fout;
    fin.open("C-small-attempt0.in");
    fout.open("fsqare_output.out");
    fin >> size;
    if (size < 1) return 0;
    
    int k = 0;
    
    while (k < size) {
        long int a, b;
        fin >> a;
        fin >> b;
        int result = count(a, b);
        fout << "Case #" << (k + 1) << ": " << result << endl;
        k++;
    }
    
    return 0;
}
