// reading a text file
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
using namespace std;

int check_arr(int arr[]){
	for(int i=0; i<10; i++){
		if(arr[i] == 0)
			return 0;
	}
	return 1;
}

int solution(int number){
	int check[10]={0,0,0,0,0,0,0,0,0,0};
	if(number == 0)
		return 0;
	int check_value = number;
	int i = 1;
	while(1){
		check_value = number * i;

		while(check_value>=1){
			check[check_value%10] = 1;
			check_value /= 10;
		}
		if (check_arr(check) == 1)
			return number * i;
		i++;
	}


}

int main () {
  string line;
  ifstream myfile ("A-large.in");
  ofstream outfile ("A_large_out.txt");
  if (myfile.is_open() && outfile.is_open())
  {
  	getline(myfile,line);
  	istringstream buffer(line);
  	int size;
  	int answer=0;
  	buffer >> size;
  	for(int i=1; i<=size; i++){
  		getline(myfile,line);

  		outfile << "Case #" << i <<": ";
  		istringstream buf(line);
  		int value;
  		buf >> value;
  		if (value == 0){
  			outfile << "INSOMNIA";
  		} else {
  			
  			answer = solution(value);
  			outfile << answer;
  		}
  		outfile << endl;
  	}
    myfile.close();
    outfile.close();
  }

  else cout << "Unable to open file"; 

  return 0;
}
