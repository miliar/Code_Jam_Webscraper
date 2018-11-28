#include <iostream>
#include <vector>
#include <fstream> 
#include <stdlib.h>
#include <string>
using namespace std;

int getOutput(int smax, string line){
	int count = 0, need=0,i;
	vector<string> all;
	string result;
	int SIZE = smax+1;
	int input_size = line.length();
	int buffer[SIZE];

	for(int i = 0; i < SIZE; i++){
		buffer[i] = line[i]-48;
        for(int k=0;;k++){
            if(count<i && buffer[i]>0){
                need++;
                count++;
            }
            else
                break;
        }
		count+=buffer[i];
	}
	return need;	
}
 
int main()
{
/*  int caseCount, a;
  string b = "";
  cin >> caseCount;
*/

  ifstream in ("A-large.in");
  ofstream out("A-large.out");

  if (!in.is_open() || in.eof())               
  {
    cerr << "ERROR: invalid input file" << endl;
    return (-1);
  }
  if(!out.is_open()) {
    cerr << "ERROR: couldn't create ouput file" << endl;
    return (-1);
  }
 
  int numCases;                       
  int a;              
  string  b = "";                
  string line;                        
  getline(in, line, '\n');            
  numCases = atoi(line.c_str());    

  for (int i=1; i<=numCases; i++) {
    if(in.eof())  { return (-1); }              
    in >> a;                             
    in >> b;
    out << "Case #" << i <<": "<<getOutput(a, b)<<"\n";
  }
  return 0;
}
