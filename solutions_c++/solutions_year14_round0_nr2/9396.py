#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include <cstdlib>

using namespace std;

int get_float(string line, double ** floatarray){

    size_t startpos = 0;
    size_t spacepos = 0;
    spacepos = (line.find(" ", startpos));
    (*floatarray)[0] = atof(line.substr(startpos, spacepos-startpos).c_str());
    startpos = spacepos + 1;
    spacepos = (line.find(" ", startpos));
    (*floatarray)[1] = atof(line.substr(startpos, spacepos-startpos).c_str());
    startpos = spacepos + 1;
    (*floatarray)[2] = atof(line.substr(startpos).c_str());

    return 0;
}

double calculate_time(double farm_needed, double current_production, double farm_production, double cookie_needed, double current_time, double compare_time){
    double time_1 = current_time + cookie_needed / current_production;
    if (farm_needed > cookie_needed)
        return time_1;
    else if (time_1 > compare_time){
        return compare_time;
    }
    else{
        double time_2 = current_time + farm_needed / current_production;
       //         cout << time_2 << "\n";
        //return time_2;
        return min(time_1, calculate_time(farm_needed, current_production + farm_production, farm_production, cookie_needed, time_2, time_1));
    }
}

int main(){
    ofstream output;
    ifstream input;
    string line;

    int totalcase;
    int currentcase;

    input.open("B-small-attempt0.in");
    output.open("output.txt");

    double * floatarray = (double*)malloc(3 * sizeof(double));
    double time;
    double currentproduction = 2.0;
    if (input.is_open()){
        getline(input, line);
        totalcase = atoi(line.c_str());
        currentcase = 1;

        while (getline(input,line)){
            get_float(line, &floatarray);
            //cout<< floatarray[0] << " " << floatarray[1] << " " << floatarray [2] << "\n";
            time = calculate_time(floatarray[0], 2.0, floatarray[1], floatarray[2], 0.0, floatarray[2]/2.0);
            //cout<< floatarray[0] << " " << floatarray[1] << " " << floatarray [2] << "\n";
            output.precision(10);
            output << "Case #" << currentcase << ": " << time << "\n";
            currentcase++;
        }

    }
    input.close();
    output.close();
    return 0;
}
