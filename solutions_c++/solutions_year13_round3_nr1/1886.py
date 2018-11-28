#ifndef CONSONANTS_H
#define CONSONANTS_H

#include <fstream>
#include <cstring>
using namespace std;

ifstream con_input;
ofstream con_output;

int con_num_cases;

bool is_con(char tmp){
    if(tmp == 'a' || tmp == 'i' || tmp == 'o' || tmp == 'e' || tmp == 'u'){
        return false;
    }
    return true;
}

bool has_con(char* from, char* end, int n_value){
    int count = 0;
    while(from <= end){
        if(is_con(*from)){
            count++;
            if(count >= n_value){
                return true;
            }
        }else{
            count = 0;
        }
        from++;
    }
    return false;
}

void consonants(){
    con_input.open("test.txt");
    con_output.open("con_output");
    con_input >> con_num_cases;
    cout << con_num_cases << endl;

    char* name = new char[1000];
    int n_value;
    int result;
    for(int i = 0; i < con_num_cases; i++){
        con_input >> name;
        con_input >> n_value;
        result = 0;
        int str_len = strlen(name);
        for(char* from = name; from <= name + str_len - n_value; from++){
            char* end = from + n_value - 1;
            while(end != name + str_len){
                if(has_con(from, end, n_value)){
                    result++;
                }
                end++;
            }
        }

        con_output << "Case #" << i + 1 << ": " << result << endl;
    }
}
#endif
