#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <sstream>
#include "memory.h"
using namespace std;

ifstream fin("A-large.in");
ofstream fout("A-large.out");

bool check[10];

int slove(int input){
    for(unsigned long long i = 1; i <= 1844674407370955161; i++){
        stringstream ss;
        unsigned long long n;
        n = input * i;
        string str;
        ss << n;
        ss >> str;
        for(int j = 0; j < str.length(); j++){
            switch(str[j]){
                case '0':
                    check[0] = true;
                    break;
                case '1':
                    check[1] = true;
                    break;
                case '2':
                    check[2] = true;
                    break;
                case '3':
                    check[3] = true;
                    break;
                case '4':
                    check[4] = true;
                    break;
                case '5':
                    check[5] = true;
                    break;
                case '6':
                    check[6] = true;
                    break;
                case '7':
                    check[7] = true;
                    break;
                case '8':
                    check[8] = true;
                    break;
                case '9':
                    check[9] = true;
                    break;
                
            }
        }
        bool pass = true;
        for(int j = 0; j < sizeof(check); j++){
            if(check[j] == false){
                pass = false;
            }
        }
        if(pass){
            return n;
        }else{
            continue;
        }
    }
    return -1;
}

int main(){
    
    int t;
    while(fin >> t){
        for(int i = 1; i <= t; i++){
            int input;
            fin >> input;
            memset(check, false, sizeof(check));
            fout << "Case #" << i << ": ";
            if(input <= 0){
                fout << "INSOMNIA" << endl;
            }else{
                fout << slove(input) << endl;
            }
        }
    }
    
    return 0;
}