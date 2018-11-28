#include <iostream>
#include <sstream>
#include <stdlib.h>
#include <string>
using namespace std;

int main(){
  int num_cases;
  cin >> num_cases;
  for(int i = 0; i < num_cases; i++){
    char n_c[6] = {'\0'};
    unsigned long long int n = 0;
    cin >> n_c;
    stringstream str;
    str << n_c;
    str >> n;
    if(n == 0){
      cout << "Case #" << i+1 << ": INSOMNIA" << endl;
    }
    else{
      bool done = false;
      int digits[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
      int j = 0;
      char temp[6] = {'\0'};
      unsigned long long int n_t = 0;
      while(!done){
        n_t = n*++j;
        string temp;
	ostringstream convert;
	convert << n_t;
	temp = convert.str();
	int k = 0;
	while(temp[k] != '\0'){
	  digits[temp[k]-48] = true;
	  k++;
	}
	if(digits[0] && digits[1] && digits[2] && digits[3] && digits[4] && digits[5] && digits[6] && digits[7] && digits[8] && digits[9]){
	  done = true;
	}
      }
      cout << "Case #" << i+1 << ": " << n_t << endl;
    }
  }
  return 0;
}
