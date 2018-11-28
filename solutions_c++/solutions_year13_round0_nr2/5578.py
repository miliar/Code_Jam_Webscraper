#include <iostream>
#include <stdint.h>
#include <fstream>
#include <string>

using namespace std;

int main(int argc, char* argv[])
{
    ifstream sourceFile("./files/B-small-attempt1.in");
    ofstream output("./files/output.txt");

    if (sourceFile.is_open()) {

        int T;
        sourceFile >> T;
        for(int i = 0; i < T; i++) {
            int N, M;
            sourceFile >> N >> M;

            int** data = new int*[N];
            for(int j = 0; j < N; j++) {
                data[j] = new int[M];
                for(int k = 0; k < M; k++) {
                    sourceFile >> data[j][k];
                }
            }

            bool overall_pass = true;

            for(int j = 0; j < N && overall_pass; j++) {
                for(int k = 0; k < M && overall_pass; k++) {
                    if(data[j][k] == 1) {
                        bool pass1 = true, pass2 = true;
                        for(int a = 0; a < N; a++) {
                            if(data[a][k] != 1) {
                                pass1 = false;
                                break;
                            }
                        }
                        for(int b = 0; b < M; b++) {
                            if(data[j][b] != 1) {
                                pass2 = false;
                                break;
                            }
                        }
                        if(!pass1 && !pass2) {
                            overall_pass = false;
                        }
                    }
                }
            }

            output << "Case #" << i + 1 << ": ";
            if(overall_pass) {
                output << "YES" << endl;
            }
            else {
                output << "NO" << endl;
            }
        }
        sourceFile.close();
    }

    return 0;
}
