#include <iostream>
#include <vector>
#include <math.h>

using namespace std;

bool isPalindrome(double value){
    double start = value;
    int digits = 0;
//    cout << "check : "<< value <<endl;

    while(start >= 10){
        start = start/10;
        digits ++;
    }

    if(digits == 0) return true;
    int end = (int)fmod(value, 10);
//cout<<"digits "<<digits<<endl;
//cout<<"end "<<end<<endl;

    if(digits == 1)
        if((int)start == end) return true;
        else return false;
    
    if ((int)start == end){
        double new_value = floor((value - start*pow(10, digits))/10);
        return isPalindrome(new_value);
    } else{
        return false;
    }
}
int main(){
    int n_cases;
    vector < vector <double> > cases;

    cin >> n_cases;

    for(int i = 0; i < n_cases; i++){
        double start, end;
        vector <double> this_case;
        cin >> start >> end;
        this_case.push_back(start);
        this_case.push_back(end);
        cases.push_back(this_case);
    }

    for(int i = 0; i < n_cases; i++){

        int counter = 0;
        int sqrt_start = (int) ceil(sqrt(cases[i][0]));
        int sqrt_end = (int) floor(sqrt(cases[i][1]));

    //    cout<<sqrt_start<<'-'<<sqrt_end<<endl;

        for(int sqrt = sqrt_start; sqrt <= sqrt_end; sqrt++){
    //cout << "sqrt : "<< sqrt <<endl;
           if(pow(sqrt, 2) > pow(sqrt_end,2)) break;
           if(isPalindrome(sqrt) && isPalindrome(pow(sqrt, 2))) counter++;
                   //cout << "Pal " <<sqrt << endl;}
        }

        cout << "Case #" << i+1 << ": " << counter << endl;
    }
}
