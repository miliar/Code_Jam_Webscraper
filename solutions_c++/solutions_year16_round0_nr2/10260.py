//revenge.cpp

#include <iostream>
#include <string>
#include <fstream>
#include <cmath>


using namespace std;

void read();


string *input;
int numOfCase = 0;


int findFlip(int num, int power){
  if (power == 1){
    return num;
  }
  if (num < pow(2,power-1)){//first half
    if (num < pow(2, power-2)){//first quarter
      return findFlip(num, power-1);
    }
    else {//second quarter
      return findFlip(num, power-1)+1;
    }
  }
  else {//second half
    num = num - pow(2,power-1);
    if (num < pow(2, power-2)){//first quarter
      return findFlip(num, power-1)+1;
    }
    else {//second quarter
      return findFlip(num, power-1);
    }
  }
}

int binary_decimal(int n) /* Function to convert binary to decimal.*/
{
    int decimal=0, i=0, rem;
    while (n!=0)
    {
        rem = n%10;
        n/=10;
        decimal += rem*pow(2,i);
        ++i;
    }
    return decimal;
}


int main(){
  read();
  int answers[numOfCase];

  for (int i = 0; i < numOfCase; i++){
    string binary = "";
    for (char c : input[i]){//change to binary
      if (c == '+'){//zero
        binary += '0';
      }else if (c == '-'){//one
        binary += '1';
      }
    }
    int power = binary.length();
    int num = binary_decimal(stoi(binary));
    int temp = findFlip(num,power);
    answers[i] = temp;
    //cout << findFlip(num, power) << '\n';
  }


  
  //write answers
  ofstream myfile("answers.txt");
  if (myfile.is_open())
  {
    for (int i = 0; i < numOfCase; i++){
      myfile << "Case #" << i+1 << ": " << answers[i] << '\n';
    }
    myfile.close();
  }
  else cout << "Unable to open file1";

  delete[] input;
}


void read(){
 	string line;
 	ifstream myfile("B-small-attempt0.in");
 	if (myfile.is_open())
 	{
    getline(myfile,line);

    numOfCase = stoi(line);
    input = new (nothrow) string[numOfCase];
    if (input == nullptr){
    cout << "Error: memory could not be allocated";
    }else{
      for (int i = 0; i < numOfCase; i++){
        getline(myfile,line);
        input[i] = line;
      }
    }
    myfile.close();
 	}	
  else cout << "Unable to open file2"; 
}

