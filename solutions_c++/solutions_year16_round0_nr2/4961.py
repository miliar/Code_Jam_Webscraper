// reading a text file
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
using namespace std;

void flip(string *str, int end){
  for(int i = 0; i<= end; i++){
    if ((*str)[i] == '-')
      (*str)[i] = '+';
    else
      (*str)[i] = '-';
  }
}

int solution(string *str){
	int size = (*str).size();
  //cout << "size = " << size <<endl;
  if(size == 0)
		return 0;
  int i = 0;
  int flip_count = 0;
	while((*str).find('-') != std::string::npos){
    i = (*str).find('-');
    while(i+1<size && (*str)[i+1] != '+'){
      i++;
    }
    flip(str,i);
    flip_count++;

	}

  return flip_count;

}

int main() {
  string line;
  ifstream myfile ("B-large.in");
  ofstream outfile ("B_large_out.txt");
  if (myfile.is_open() && outfile.is_open())
  {
  	getline(myfile,line);
  	istringstream buffer(line);
  	int size;
  	int answer;
  	buffer >> size;
  	for(int i=1; i<=size; i++){
  		getline(myfile,line);
      outfile << "Case #" << i <<": ";
      //cout << "Case #" << i <<": " << line <<endl;
  		answer = solution(&line);
  		outfile << answer << endl;
  	}
    myfile.close();
    outfile.close();
  }

  else cout << "Unable to open file"; 

  return 0;
}
