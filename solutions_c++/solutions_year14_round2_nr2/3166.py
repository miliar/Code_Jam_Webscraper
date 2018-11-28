// list::push_front
#include <iostream>
#include <fstream>
#include <list>
void war(int);
using namespace std;

int main(int argc,char* argv[])
{
    std::ifstream infile(argv[1]);
    int T;
    infile >> T; //no of testcases
    for (int i = 1; i <= T; i++){
        int A,B,K;
        infile >> A;
        infile >> B;
        infile >> K;
        int result,count=0;
        for (int k = 0;k < A; k++) {
            for (int j = 0;j < B; j++) {
                result = k & j;
                if ((result) >= 0 && (result) < K) {
                    count++;
                }
            }
        }
        cout << "Case #" << i << ": " << count << endl;
    }
}
