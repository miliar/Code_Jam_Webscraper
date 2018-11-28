#include <fstream>
#include <iostream>
#include <map>
#include <vector>

bool fillAndSay(long int next, bool (&used)[10]){
    while (next > 0){
        int d = next % 10;
        next = next / 10;
        used[d] = true;
    }
    for (int i = 0; i  < 10; ++i)
        if (!used[i])
            return false;

    return true;
}


int main(int argc, char *argv[]){
    std::ifstream inF;
    inF.open(argv[1]);
    int n;
    inF>>n;
    for (int j = 1; j < n+1; ++j){
        long int c;
        inF>>c;
        long int last = c;
        bool used[10] = {false,};
        int k;
        if (fillAndSay(c, used)){
            std::cout<<"Case #"<<j<<": "<<last<<std::endl;  
            continue;
        }
        for (k = 2; k < 1000; ++k){
            last = c*k;
            if (fillAndSay(last, used))
                break;
        }
        if (k >= 1000)
            std::cout<<"Case #"<<j<<": "<<"INSOMNIA"<<std::endl;  
        else
            std::cout<<"Case #"<<j<<": "<<last<<std::endl;  
    }
    return 0;
}
