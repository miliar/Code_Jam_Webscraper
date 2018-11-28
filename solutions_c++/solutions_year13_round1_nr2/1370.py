#ifndef ENERGY_H
#define ENERGY_H

#include <fstream>
#include <cstring>
#include <math.h>
using namespace std;

ifstream energy_input;
ofstream energy_output;

int init_energy, regain_energy, num_activities;
int* values;
int num_cases;

int do_energy(int init_energy, int current_energy, int* values, int from){
    if(from == num_activities - 1){
        return current_energy * values[from];
    }
    int max_gain = -1;
    for(int i = 0; i <= current_energy; i++){
        int next_current_energy = current_energy - i + regain_energy > init_energy ? 
            init_energy : current_energy - i + regain_energy;
        int gain = i * values[from] + do_energy(init_energy, next_current_energy, values, from + 1);
        if(max_gain < gain){
            max_gain = gain;
        }
    }
    return max_gain;
}

void energy(){
    energy_input.open("test.txt");
    energy_output.open("energy_output");
    energy_input >> num_cases;

    for(int i = 1; i <= num_cases; i++){
        energy_input >> init_energy;
        energy_input >> regain_energy;
        energy_input >> num_activities;
        values = new int[num_activities];
        int max_gain = 0;
    
        for(int j = 0; j < num_activities; j++){
            energy_input >> values[j];
        }

        int current_energy = init_energy;
        max_gain = do_energy(init_energy, current_energy, values, 0);

        energy_output << "Case #" << i << ": " << max_gain << endl;
    }
}
#endif
