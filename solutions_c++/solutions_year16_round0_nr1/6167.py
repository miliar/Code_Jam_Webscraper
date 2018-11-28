#include <iostream>
#include <sstream>
#include <string>

using namespace std;

    bool x0=false;
    bool x1=false;
    bool x2=false;
    bool x3=false;
    bool x4=false;
    bool x5=false;
    bool x6=false;
    bool x7=false;
    bool x8=false;
    bool x9=false;
    string value;

bool check();

int doTheMath(string value);
void reset();

int main(){
    long long int t;
    long long int n;
    cin >> t;
    for(long long int i = 0;i < t; i++){
        cin >> n;
        if(n == 0)
            cout << "CASE #" << i+1 <<": INSOMNIA" << endl;
        else {
            long long int index = 1;
            reset();
            string value;
         //   cout << "Here!" << endl;
            long long int n_copy = n;
            while(check() == false){
                value = to_string(n_copy);
//cout << "Value: " << value << endl;
                doTheMath(value);
                n_copy = ++index * n;
            }
            cout << "CASE #" << i+1 <<": " << value << endl;
        }
    }
}




bool check(){
    if(x0 &&  x1 && x2 && x3 && x4 && x5 && x6 && x7 && x8 && x9)
        return true;
    else
        return false;
}

int doTheMath(string value){
    for(int i = 0; i < value.length(); i++){
        if(value.at(i) == '0')
            x0 = true;
        else if(value.at(i) == '1')
            x1 = true;
        else if(value.at(i) == '2')
            x2 = true;
        else if(value.at(i) == '3')
            x3 = true;
        else if(value.at(i) == '4')
            x4 = true;
        else if(value.at(i) == '5')
            x5 = true;
        else if(value.at(i) == '6')
            x6 = true;
        else if(value.at(i) == '7')
            x7 = true;
        else if(value.at(i) == '8')
            x8 = true;
        else
            x9 = true;
    }
    return 0;
}

void reset(){
    x0=false;
    x1=false;
    x2=false;
    x3=false;
    x4=false;
    x5=false;
    x6=false;
    x7=false;
    x8=false;
    x9=false;
}
