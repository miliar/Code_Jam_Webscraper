#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
#include <vector>
#include <algorithm>
#include <sstream>
#include <stdio.h>

using namespace std;

vector<int> findAndRemove (vector<int> vec , int number) {
    vector<int>::iterator it;

    if ((it = std::find(vec.begin(),vec.end(),number)) != vec.end()){
            vec.erase(it);
    }
    return vec;
}

/*
int countSheeps(string line) {
    int arr[] = {0,1,2,3,4,5,6,7,8,9};
    vector<int> from0to9(arr, arr + sizeof(arr) / sizeof(arr[0]) );

    vector<int> digits;

    long number = atol(line.c_str());
    //Case 0, INSONMIA
    if (number == 0 ) {
        return -1;
    }

    int N = 1;
    for (int i = line.length()-1; i>=0;i--){
        int current_number = (int) line[i] - (int) '0';
        digits.push_back(current_number);

        from0to9 = findAndRemove(from0to9,current_number);

    }

    while (from0to9.size() != 0) {
        N++;
        int carry = 0;
        for (int i = 0; i < digits.size(); i++){
            int current_number = ((digits[i] * N) + carry);
            int current_digit = current_number % 10;
            carry = current_number - current_digit;
            from0to9 = findAndRemove(from0to9,current_digit);
            if (from0to9.size() == 0){
                carry = 0;
                break;
            }

        }
        #Arreglar error de incluir siempre al 0
        if (carry) {
            stringstream ss;
            ss << carry;
            string st_number = ss.str();
            for ( int i = 0; i < st_number.size(); i++){
                from0to9 = findAndRemove(from0to9, (int) st_number[i] - (int) '0');
                if (from0to9.size() == 0){
                    break;
                }
            }
        }

    }

    return N * number;
}*/

int countSheeps(string line) {
    int arr[] = {0,1,2,3,4,5,6,7,8,9};
    vector<int> from0to9(arr, arr + sizeof(arr) / sizeof(arr[0]) );


    long number = atol(line.c_str());
    //Case 0, INSONMIA
    if (number == 0 ) {
        return -1;
    }

    int N = 1;
    for (int i = line.length()-1; i>=0;i--){
        int current_number = (int) line[i] - (int) '0';
        from0to9 = findAndRemove(from0to9,current_number);
    }

    while (from0to9.size() != 0){
        N++;
        long number_aux = number * N;
        stringstream ss;
        ss << number_aux;
        string st_number = ss.str();
        for ( int i = st_number.length()-1; i >= 0; i--){
            from0to9 = findAndRemove(from0to9, (int) st_number[i] - (int) '0');
            if (from0to9.size() == 0){
                break;
            }
        }

    }

    return N * number;
}

void escribirArchivo(vector<long> results){
    ofstream output ("output_large.txt");
    if (output.is_open())
      {
        for (int i = 0; i< results.size(); i++){
            output << "Case #" << i+1 << ": ";
            if (results[i] == -1){
                output<< "INSOMNIA";
            }else {
                output << results[i];
            }
            output << "\n";
        }
        output.close();
      }
      else cout << "Unable to open file";

}

int main () {
  string line;
  ifstream myfile ("A-large.in");
  vector<long> results;
  if (myfile.is_open())
  {
    getline(myfile,line);
    int testCases  = atoi(line.c_str());

    for (int i = 0; i < testCases; i++){
        getline(myfile,line);
        cout << "Numero : " << line << endl;
        cout << "Estoy durmiendo en " << countSheeps(line) << endl;
        results.push_back(countSheeps(line));
    }

    myfile.close();
    escribirArchivo(results);
  }

  else cout << "Unable to open file";

  return 0;
}


