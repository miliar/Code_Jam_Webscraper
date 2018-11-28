#include<iostream>
#include<fstream>
using namespace std;


int retsimilarity(int *first,int *second){
	int error = -1;
	int index = 0;
	for(int i = 0;i<4;i++){
		for(int j = 0;j<4;j++){
			if(first[i]==second[j]){
				error++;
				index = j;
				break;
			}
		}
	}
	if(error>0) return -2;
	else if(error == -1) return -1;
	return index;	
}

int main(){
	int t = 0;
	int j = 1;
	ifstream ifile("A-small-attempt0.in");
	ofstream ofile("output.txt");
	ifile>>t;
	while(t--){
		int first,second;
		ifile>>first;
		int firstArr[4];
		for(int i = 0 ;i<4;i++){
			for(int j = 0;j<4;j++){
				if(i == (first-1)) ifile>>firstArr[j];
				else{
					int temp;
					ifile>>temp;
				}
			}
		}
		
		
		ifile>>second;
		int secondArr[4];
		for(int i = 0 ;i<4;i++){
			for(int j = 0;j<4;j++){
				if(i == (second-1)) ifile>>secondArr[j];
				else{
					int temp;
					ifile>>temp;
				}
			}
		}
	    int result = retsimilarity(firstArr,secondArr);
	    if(result == -2)
	    	ofile<<"case #"<<j++<<": Bad magician!"<<endl;
	    else if(result == -1)
	    	ofile<<"case #"<<j++<<": Volunteer cheated!"<<endl;
	    else
	        ofile<<"case #"<<j++<<": "<<secondArr[result]<<endl;
	}
}
