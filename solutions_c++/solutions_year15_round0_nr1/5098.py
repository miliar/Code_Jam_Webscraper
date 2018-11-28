#include <iostream>
#include <string>
#include <cstdio>
#include <vector> 
#include <algorithm> 

using namespace std;

int main(){

    int num_test_cases;
    cin >> num_test_cases;
    for(int test_case = 1; test_case <= num_test_cases; ++test_case){

        int s_max;
        cin >> s_max;
        string shyness_string;
        cin >> shyness_string;
        vector<short> shyness_levels;
        for(char& c : shyness_string){
            shyness_levels.push_back(c - '0');
        }
        int less_shy = 0;
        int max_shy_needed = 0;
        for(int i = 0; i <= s_max; i++){
            if(i > less_shy){
                max_shy_needed = max(max_shy_needed, i - less_shy);
            }
            less_shy += shyness_levels[i];
        }
        cout << "Case #" << test_case << ": " << max_shy_needed << endl;
    }
    return 0;
}
