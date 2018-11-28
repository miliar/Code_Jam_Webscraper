#include <iostream>
#include <fstream>
#include <math.h>
using namespace std;

int main(int argc, char **argv) {
    if (argc < 2) {
        cout << "Please specify input file" << endl;
        return 1;
    }
    ifstream in(argv[1]);

    int testCases;
    in >> testCases;
    for (int testCase =0; testCase < testCases; testCase++) {
        char *result = (char*)"YES";
        // Read test case
        int N,M; // N lines with M integers
        int height[100][100];
        in >> N >> M;
        for(int n=0; n<N; n++) {
            for (int m=0; m<M; m++) {
                in >> height[n][m];
            }
        }
        
        // Handle problem:
        int biggestLeft[100][100];
        int biggestRight[100][100];
        int biggestTop[100][100];
        int biggestDown[100][100];

        for (int n=0; n<N; n++) {
            biggestLeft[n][0] = 0;
            for(int m=1; m<M; m++) {
                biggestLeft[n][m] = max(biggestLeft[n][m-1], height[n][m-1]); 
            }
        }

        for (int n=0; n<N; n++) {
            biggestRight[n][M-1] = 0;
            for(int m=M-2; m>=0; m--) {
                biggestRight[n][m] = max(biggestRight[n][m+1], height[n][m+1]); 
            }
        }

        for (int m=0; m<M; m++) {
            biggestTop[0][m] = 0;
            for(int n=1; n<N; n++) {
                biggestTop[n][m] = max(biggestTop[n-1][m], height[n-1][m]); 
            }
        }

        for (int m=0; m<M; m++) {
            biggestDown[N-1][m] = 0;
            for(int n=N-2; n>=0; n--) {
                biggestDown[n][m] = max(biggestDown[n+1][m], height[n+1][m]); 
            }
        }
        

        for (int n=0; n<N; n++) {
            for(int m=0; m<M; m++) {
                if(    !(((biggestLeft[n][m] <= height[n][m]) 
                    && (biggestRight[n][m] <= height[n][m])) || // Horizontal line ok
                       ((biggestTop[n][m] <= height[n][m])
                    && (biggestDown[n][m] <= height[n][m]) ))) { // Vertical line ok
                    result = (char*) "NO";
                    goto endloop;
                }
            }
        }
        endloop:



        cout << "Case #" << (testCase+1) << ": " << result << endl;
    } 
    
    return 0;
}
