#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cstdlib>
using namespace std;

void solve(int case_num){
    int Smax;
    string pstr; 
    cin >> Smax >> pstr;
    int num_standing = 0;
    int ret = 0;

    for(int s=0; s<=Smax; s++){
        int num_persons = atoi(pstr.substr(s,1).c_str());
        if(num_persons > 0){
            if(num_standing < s){
                int guests_needed = (s-num_standing);
                num_standing += guests_needed;
                ret += guests_needed;
            }
            num_standing += num_persons;
        }
    }
    printf("Case #%d: %d\n",case_num, ret);
}

int main(){
    int num_cases;
    cin >> num_cases;
    for(int ii=1; ii <= num_cases; ++ii)
        solve(ii);
}
