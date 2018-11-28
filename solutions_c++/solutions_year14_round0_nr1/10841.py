#include <fstream>
#include <iostream>
#include <vector>
#include <map>
using namespace std;
int main(int * argc, char * argv[])
{
	int numberOfTC;
	int firstRowIndex, secondRowIndex;
	string badMag = "Bad magician!";
	string cheater = "Volunteer cheated!";
	map<int,bool> firstRow;
	map<int,bool> secondRow;
	ifstream in("A-small-attempt0.in");
	ofstream out("output.in");
	in>> numberOfTC;
	int temp;
	for ( int i =0 ; i < numberOfTC ; i++){
		in >> firstRowIndex;
		for(int j =0 ; j < 4 ; j++){
			for(int k=0; k<4; k++){
				if(j == firstRowIndex-1){
					in >> temp;
					firstRow.insert(pair<int,bool>(temp,true));
				}
				else{
					in>>temp;
				}
			}
		}
		in >> secondRowIndex;
		for(int j =0 ; j < 4 ; j++){
			for(int k=0; k<4; k++){
				if(j == secondRowIndex-1){
					in >> temp;
					secondRow.insert(pair<int,bool>(temp,true));
				}
				else{
					in>>temp;
				}
			}
		}
		int j =0;
		int value;
		map<int,bool>::iterator it ;
		for( it = firstRow.begin(); it!=firstRow.end(); it++){
			if(secondRow.find(it->first)  != secondRow.end()){
				j++;
				value = it->first;
			}
		}
		if(j==1){
			out<<"Case #"<<i+1<<": "<<value<<endl;
		}
		else if(j==0){
			out<<"Case #"<<i+1<<": " << cheater.c_str()<<endl;
		}
		else
		{
			out<<"Case #"<<i+1<<": " << badMag.c_str()<<endl;
		}
		firstRow.clear();
		secondRow.clear();
	}
	return 0;
}