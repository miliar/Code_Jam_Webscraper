#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

int main(void){

ifstream fin ("B-large.in");
ofstream fout ("B-large.out");

int T;
double C, F, X;
fin >> T;

for(int i=0; i<T; i++){
    fin >> C >> F >> X;

    double rate=2, cur_time=0, predicted_time=0, time_passed=0, time_to_get_farm=0;
    while(1){
        cur_time = time_passed + double(X)/double(rate); //TOTAL cookies / current Rate

        time_to_get_farm= double(C)/double(rate);
        predicted_time = time_to_get_farm + time_passed + double(X)/double(rate+F);

        if(cur_time > predicted_time){ //Buy a farm
            rate += F;
            time_passed += time_to_get_farm; //Looks like a recursive deal here
        }
        else{
            fout << fixed;
            fout << "Case #" << (i+1) << ": " << setprecision(12) << cur_time;
            break;
        }

    }

    if(i<(T-1)){
        fout << endl;
    }
}



return 0;
}
