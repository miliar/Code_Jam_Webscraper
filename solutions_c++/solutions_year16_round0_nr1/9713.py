#include <iostream>
#include <fstream>
#include <string.h>
#include <map>
#include <vector>
#include <cmath>
#include <list>
#include <string>
#include <sstream>

using namespace std;

void getDigits(unsigned int N, unsigned char buffer[]){
    while(N>0){
        unsigned int rem = N%10;
//        cout << "-----" << N << " " << rem << endl;
        buffer[rem] = 1;
        N = N/10;
    }
}

bool checkSleep(unsigned char buffer[]){
    for(int i=0; i<10; i++)
        if(buffer[i] == 0)
            return false;
    return true;
}

int main(int argc, char **argv){
    istream &in  = (argc>1)?*(new ifstream(argv[1])):cin;
    ostream &out = (argc>2)?*(new ofstream(argv[2])):cout;

    int T;
    in >> T;

    for(int i=1; i<=T; i++){
        int N;
        in >> N;
        string result;
        if(N != 0){
            unsigned char buffer[] = {0,0,0,0,0,0,0,0,0,0};
            int j=0;
            do{
                j++;
                getDigits(j*N, buffer);
            }while(!checkSleep(buffer));
            result = to_string(j*N);
        }else{
            result = "INSOMNIA";
        }
        out << "Case #" << i << ": " << result << endl;

    }

    return 0;
}
