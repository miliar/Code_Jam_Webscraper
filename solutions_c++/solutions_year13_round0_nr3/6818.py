#include <iostream>
#include <cmath>
#include <fstream>
#include <sstream>
#include <string>
using namespace std;

int convert_str_to_int(string input){
  int tmp;
  istringstream converter(input);
  converter >> tmp;
  return tmp;
}

bool check_square(int input){
  float calc_tmp = 0;
  calc_tmp = sqrt(input);
  if (calc_tmp == floor(sqrt(input))){
    return true;
  } else {
    return false;
  }
}

bool check_palindrom(int input) {
  string converted_input;

  if (input < 10) {
    return true;
  } else {
    ostringstream converter;
    converter << input;
    converted_input = converter.str();
    int end = converted_input.size()-1;

    for (int start = 0; start <= end; start++) {
      if (converted_input[start] != converted_input[end]){
        return false;
      } else {
        end--;
      }
    }
  }
  input = sqrt(input);
  if( check_square(input) == false){
    if (check_palindrom(input) == true){
      return true;
    } else {
      return false;
    }
  } else {
    return true;
  }
}

void test_it(){
  string str_tmp;
  string tmp;
  int test_cases;
  int start, end;
  int counter;
  
  ifstream input_file;
  input_file.open("C-small-attempt0.in.txt", ios::in);

  ofstream output_file;
  output_file.open("out", ios::out);

  getline(input_file, str_tmp);
  test_cases = convert_str_to_int(str_tmp);

  for(int i=1; i<=test_cases; i++){
    counter = 0;

    getline(input_file, str_tmp);

    int cursor = 0;
    int pos = 0;

    for (int cursor=0; cursor < str_tmp.size(); cursor++){
      if (int(str_tmp[cursor]) == 32)
        pos = cursor;      
    }

    tmp.erase();
    tmp.append(str_tmp, pos, str_tmp.size());
    str_tmp.erase(pos);

    start = convert_str_to_int(str_tmp);

    end = convert_str_to_int(tmp);

    for (int a=start; a <=end; a++){
        if(check_square(a)){
          if (check_palindrom(a))
            counter++;
        }
      }
    output_file << "Case #" << i << ": " << counter << endl;
  }

  input_file.close();
  output_file.close();
}

int main(){
  test_it();
  return 0;
}