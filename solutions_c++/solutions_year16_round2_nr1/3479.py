#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector> 
using namespace std;

string name[10] = {"ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"};
string name2[10]={"0","1","2","3","4","5","6","7","8","9"};
string findphone(string s){

	if(s.length() == 0) return "";
	for(int i=0; i< 10; i++){
		string temp = s;
		string numName = name[i];
		bool valid = true;
		for(int j =0; j< numName.length(); j++ ){
			int ind = temp.find(numName.at(j)) ;
			if(ind < 0 ){
				valid = false;
				break;
			}
			else{
				temp.erase(ind,1);
			}
		}
		if(valid){
			if(findphone(temp) != "error" ){
				return  name2[i] + findphone(temp);	
			}
			
		}		
	}
	return "error";
	
}
int main()
{
    ifstream myfile;
    ofstream output;
    myfile.open("input.txt");
    output.open("output.txt");
    
    int numCase;

    myfile >> numCase;

    for(int i=0; i< numCase ; i++){
    	string code ;
		myfile >> code;
		string number = findphone(code);
		output << "Case #" << i+1 << ": " ;

		output << number << endl;
		
    }
    myfile.close();
    output.close();
    return 0;
}


