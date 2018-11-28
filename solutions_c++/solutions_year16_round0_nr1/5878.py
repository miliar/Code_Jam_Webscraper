#include <iostream>
#include <fstream>
#include <stdlib.h>
using namespace std;

bool seenAll(int a[], int n) {
    for (int i = 0; i < n; ++i)
        if (!a[i])
            return false;
    return true;
}

int small(int n) {
    if (n == 0)
        return -1;
    
    int a[10] = {0};
    
    int res, final = -1;
    for (int i = 1; !seenAll(a, 10); ++i) {
        final = res = i*n;
        while (res) {
            a[res%10] = 1;
            res /= 10;
        }
    }
    
    return final;
}

void getLastN(const string& inFile, const string& outFile) {
    ifstream in(inFile.c_str());
    if (!in)
        return;
    
    FILE* pFile = fopen(outFile.c_str(), "w");
    
    int T, N;
    in >> T;
    for (int i = 0; i < T; ++i) {
        in >> N;
        int res = small(N);
        fprintf(pFile, "Case #%d: %s\n", i+1, (res == -1 ? "INSOMNIA" : to_string(res)).c_str());
    }
}


int main(int argc, const char * argv[]) {
    getLastN("/Users/elvirakalviste/Desktop/CodeJam2016/CodeJam2016/a_small.in",
             "/Users/elvirakalviste/Desktop/CodeJam2016/CodeJam2016/a_small.out");
    
    return 0;
}
