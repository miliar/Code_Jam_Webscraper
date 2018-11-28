#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdlib>
#include <string>
#include <vector>

using namespace std;
int solve_case(int smax,string si);


int main(void){
    string line,sstr;
    istringstream iss;
    int smax;
    int cases = 0;
    int case_all;

    getline(cin,line);
    iss.str(line);
    iss >> case_all;
    iss.clear();

    for(cases=1;cases <= case_all;cases++){
        getline(cin,line);
        iss.str(line);
        if((iss >> smax) && (iss >> sstr)){
            cout << "Case #" << cases << ": " 
                    << solve_case(smax,sstr) << endl;
        }
        iss.clear();
    }
}

int solve_case(int smax,string si){
    int excess = 0;
    int need = 0;

    for(int i=0;i<=smax;i++){
        int a = si[i] - '0';
        if(a > 0){
            excess += a-1;
        }else{
            if(excess > 0){
                excess--;
            }else{
                need++;
            }
        }
    }
    return need;
}

