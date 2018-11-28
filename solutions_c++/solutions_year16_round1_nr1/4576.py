#include <iostream>
#include <cstring>

using namespace std;

void add1ST(char a, char* b, char* output) {
    output[0] = a;
    for(int i = 0; i < 1000; i++) {
        output[i + 1] = b[i];
    }
}
void cp(char* a, char* b) {
    for(int i = 0; i < 1000; i++) {
        a[i] = b[i];
    }
}

int main(int argc, char** argv) {
    int t;
    char S[1000], solution[1001];
    cin >> t; //read the number of cases
    for(int i = 1; i <= t; i++) { //lets solve all cases
        cin >> S; //read string
        solution[0] = S[0];
        solution[1] = 0;
        for(int i = 1; S[i] != 0; i++) {
            if(solution[0] > S[i]) {
                solution[i] = S[i];
                solution[i + 1] = 0;
            } else {
                char temp[1001];
                add1ST(S[i], solution, temp);
                cp(solution, temp);
                solution[i + 1] = 0;
            }
        }
        
        cout << "Case #" << i << ": " << solution << endl;
    }
    
    return 0;
}

