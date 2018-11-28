#include <bits/stdc++.h>

using namespace std;

int main()
{
    FILE * inFile;
    FILE * outFile;

    inFile = fopen("A-large.in", "r");
    outFile = fopen("test.out", "w");

    int t;
    fscanf(inFile, "%d", &t);
    int testCase = 0;
    while(t--){
        testCase++;
        int n;
        fscanf(inFile, "%d", &n);
        int copyN = n;
        int i = 0;
        int nUsed = 0;
        while(n && nUsed != ((1 << 10) - 1)){
            while(n){
                int lastDigit = n % 10;
                n = n/10;
                nUsed = nUsed |(1 << lastDigit);
            }
            i++;
            n = copyN * (i +1);
        }
        if(nUsed == ((1 << 10) - 1 ))
            fprintf(outFile, "Case #%d: %d\n", testCase, i*copyN);
        else{
            fprintf(outFile, "Case #%d: INSOMNIA\n", testCase);
        }
    }
    fclose(inFile);
    fclose(outFile);
    return 0;
}
