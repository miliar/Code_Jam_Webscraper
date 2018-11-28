#include<stdio.h>
#include<iostream>
#include<string.h>
#include<vector>
#include<map>
#include <iostream>     // std::cout
#include <fstream>
#include <sstream>
#include <math.h>

using namespace std;

int digs[10];
int *myJam;
int N, J;

bool findDiv(uint64_t N, uint32_t& div){
    
    uint64_t i,sq =0;
    if(N==1 || N==2)
        return false;
    
    if(N%2==0){
        div = 2;
        return true;
    }
    sq=sqrt(N);
    for(i=2; i<=sq; i++)
    {
        if(N%i==0){
            div = (uint32_t)i;
            return true;
        }
    }
    return false;
}

bool isPrime(int*jcoin, string& divstr){
    std::stringstream ss;
    for(int base = 2; base< 11; base++){
        uint64_t num = 0;
        uint64_t mul = 1;
        for(int i = 0; i< N; i++){
            num = num + jcoin[i] * mul;
            mul = mul * base;
        }
        uint32_t div;
        //printf("NN DEBUG: finDiv: %llu Base:%d\n", num, base);
        if(!(findDiv(num, div)))
            return false;
        ss << ' ' << div;
    }
    divstr = ss.str();
    return true;
}

void encodeJam(int num){
    memset(myJam, 0, sizeof(int) * N);
    myJam[0]   = 1;
    myJam[N-1] = 1;
    int i = 1;
    while(num != 0){
        myJam[i] = num % 2;
        i++;
        num = num >> 1;
    }
    //cout << "NN DEBUG Encode J: ";
    //for(int i = N -1; i >= 0; i--){
    //    cout << myJam[i];
    //}
    //cout << endl;
}

void run(){
        int startNum = 0;
        int found = 0;
        while(found != J){
            encodeJam(startNum);
            string divStr;
            if(isPrime(myJam, divStr)){
                //printf("NN DEBUG:ANS \n");
                for(int i = N-1; i>= 0; i--){
                    cout << myJam[i];
                }
                cout << divStr << endl;
                found++;
            }
            startNum++;
        }
}

int main(int argc, char**argv){
    int numTest;
    ifstream myfile ("C-small-attempt0.in.txt");
    myfile >>  numTest;
    for(int caseNo = 0; caseNo < numTest; caseNo++){
        myfile >> N;
        myfile >> J;
        //printf("NN DEBUG: N%d J%d \n", N, J);
        myJam = new int [N];
        printf("Case #%d:\n", (caseNo+1));
        run();
    }
}
