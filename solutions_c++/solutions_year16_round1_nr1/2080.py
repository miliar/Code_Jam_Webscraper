#include <bits/stdc++.h>
#include <fstream>
using namespace std;
int main() {
	int i,j, k;
	ifstream input;
 	ofstream output;
 	input.open("A-large (1).in");
 	output.open("Ans.txt");
 	string string1="";
 	string string2="";
 	input >> i;
 	for (j=0; j<i;j++){
   	 	input >> string1;
    	string2 = string1[0];
 	for(k=1; k<string1.size(); k++){
  		if (string1[k]>=string2[0]) {
   			string2.insert(0, 1, string1[k]);
  		} else {
   			string2.push_back(string1[k]);
  		}
 	}
 	output << "Case #";
 	output << j+1;
 	output << ": ";
 	output << string2;
 	output << "\n";
 	}
}
