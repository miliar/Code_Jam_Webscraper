#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <set>
using namespace std;

int main(int argc, const char *argv[]){
    vector<int> hold_all;
    vector<int> digit;
    vector<int> test_number;
    ifstream input;
    input.open("01.txt");
    int number;
    string hold;
    getline(input,hold);
    number = stoi(hold);
    cout << number << endl;
    while(getline(input,hold)){
        test_number.push_back(stoi(hold));
    }
    for (int i=0; i<test_number.size(); i++) {
        cout << test_number[i] << endl;
    }
    ofstream output;
    output.open("result.txt");
    for(int i=0;i<number;i++){
        output << "Case #" << i+1 << ": ";
        int n = test_number[i];;
        int counter = 2;
        int hold;
        while(true){
            hold = n;
            if(test_number[i]!=0){
                while(n!=0){
                    vector<int>::iterator it;
                    it = find(digit.begin(),digit.end(),n%10);
                    if(it == digit.end()){
                        digit.push_back(n%10);
                        n /= 10;
                    }
                    else{
                        n /=10;
                    }
               
                }
                n = hold;
            }
            else{
                output << "INSOMNIA" << endl;
                break;
            }
            if(digit.size()==10){
                cout << "o:"<< i << " " << n << endl;
                output << n << endl;
                break;
            }
            else{
                n = test_number[i]*counter;
                counter += 1;
            }
        }
        digit.clear();
        hold_all.clear();
    }
    input.close();
    output.close();
    return 0;
}