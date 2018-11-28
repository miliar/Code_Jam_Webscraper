#include <fstream>
#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <cmath>

int len;

unsigned long long int toBase(std::string w, int b){
    unsigned long long int res = 0;
    for (int i = 0; i < len; ++i){
        int d = std::stoi(std::string(1, w[i]));
        res += d * pow(b, len - i -1);
    }
    return res;
}

unsigned long long int isPrime(unsigned long long int c){
    if (!(c % 2))
        return c / 2;
    unsigned long long int i;
    for (i = 3; (i*i) <= c; i+= 2)
        if (!(c % i))
            return i;
    return 0; 
}




std::string generateNew(){
    static long long unsigned int a = 1; 
    long long unsigned int c = a;
    a += 2; 
    std::string w = std::string(len, '0');
    for (int i = 0; i < len; i++){
        int d = c % 2;
        c = c / 2;
        w[len - i -1] = (d ? '1' : '0');
    }
    w[0] = '1'; 
    return w;
}


int main(int argc, char *argv[]){
    std::ifstream inF;
    inF.open(argv[1]);
    unsigned long long int n;
    inF>>n;//1
    inF>>n;
    unsigned long long int j;
    inF>>j;
    len = n;
    std::vector<unsigned long long int> v;
    unsigned  done = 0;
    std::string acc;
    std::cout<<"Case #1:"<<std::endl;
    while (done < j){
        acc = generateNew();
        v.clear();
        for (unsigned long long int i = 2; i <= 10; ++i){
            unsigned long long int res = isPrime(toBase(acc ,i));
            if (!res)
                break;
            v.push_back(res);
        }
        if (v.size() != 9)
            continue;
        std::cout<<acc<<" ";
        for (int i = 0; i < 9; i++)
            std::cout<<v[i]<<" ";
        std::cout<<std::endl;
        done++;
    }
    return 0;
}
