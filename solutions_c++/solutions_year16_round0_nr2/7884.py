#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;

bool over(string input){
    if(input.find("-") == string::npos){
        return true;
    }
    else{
        return false;
    }
}

long long int plus_(string input){
  long long int count = 0;
  for(long long int i = 0;i < input.length();i++){
    if(input[i] == '+'){
      count++;
    }
  }
  return count;
}

long long int minus_(string input){
  long long int count = 0;
  for(long long int i = 0;i < input.length();i++){
    if(input[i] == '-'){
      count++;
    }
  }
  return count;
}

void reverse_(string &input){
    reverse(input.begin(), input.end());
    for(long long int i = 0;i < input.length();i++){
        if(input[i] == '+'){
            input[i] = '-';
        }
        else{
            input[i] = '+';
        }
    }
}

long long int flip(string input){
    vector<string> push;
    long long int result = 0;
    while(input.length() > 0){
        if(input[input.length() - 1] == '-'){
            if(input[0] == '-'){
              reverse_(input);
              result++;
            }
            else{
              long long int j = 0;
              while(input[j] != '-'){
                input[j] = '-';
                j++;
              }
              result++;
            }
        }
        else if(input[input.length() - 1] == '+'){
            input = input.substr(0, input.length() - 1);
            //cout << input << "here+" << endl;
            //result++;
        }
    }
    return result;
}

int main(){
    long long int t, counter = 1;
    string input;
    cin >> t;
    while(t--){
        cin >> input;
        long long int result = flip(input);
        cout << "Case #" << counter << ": " << result << endl;
        counter++;
    }
    return 0;
}
