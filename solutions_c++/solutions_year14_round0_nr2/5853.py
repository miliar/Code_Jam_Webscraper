#include <iomanip>
#include <iostream>
#include <fstream>

int main(int argc, char * argv[]){
    if (argc != 2){
        return 1;
    }

    std::ifstream in(argv[1]);
    if (!in){
        return 2;
    }

    std::ofstream out("out");

    int T; in >> T;
    for(int i = 0; i < T; i++){
        double C, F, X;
        in >> C >> F >> X;

        double rate = 2, time = 0;

        while (true){
            // if time to buy new farm + time to build up cookies
            // is less than
            // time to build up cookies
            if (((C / rate) + (X / (rate + F))) < (X / rate)){
                // add time spent getting enough cookies to get farm
                time += C / rate;
                // buy farm
                rate += F;
            }
            else{
                // add time needed to get all cookies at the current rate
                time += X / rate;
                break;
            }
        }

        out << "Case #" << i + 1 << ": " << std::setprecision(15) << time << std::endl;
    }

    return 0;
}
