#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cmath>

using namespace std;

fstream file_stream;

void parse_input(void);

int main(int argc, char** argv)
{
    file_stream.open(argv[1]);
    string line;
    getline(file_stream, line);
    char* str = new char[line.length() + 1];
    strcpy(str, line.c_str());
    int num = atoi(strtok(str, " "));
    for(int i = 0; i < num; ++i){
        cout << "Case #" << i + 1 << ": ";
        parse_input();
    }
    delete[] str;
}

void parse_input(void)
{
    cout << fixed;
    cout << setprecision(7);
    double per_sec = 2.0;
    string line;
    getline(file_stream, line);
    char* str = new char[line.length() + 1];
    strcpy(str, line.c_str());
    double c = atof(strtok(str, " "));
    double f = atof(strtok(0, " "));
    double x = atof(strtok(0 , " "));
    double total = 0.0;
    while(true){
        double time_to_farm = (c / per_sec);
        double time1 = (x / per_sec) + total;
        double time2 = (x / (per_sec + f)) + total + time_to_farm;
//        cout << (x / (per_sec + f)) + total + time_to_farm << " " << total + (x / per_sec) << endl;
        if(time2 < time1){
            total += time_to_farm;
            per_sec += f;
        }
        else{
            total += (x / per_sec);
            break;
        }
    }
    cout << total << endl;
}
