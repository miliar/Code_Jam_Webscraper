#include <iostream>
#include <fstream>
#include <string>
using namespace std;

bool check_line(int x1 , int y1 , int i , int j , int** Arr){
	bool result,result_column,result_row;
	result_row = true;result_column = true; 
	// row
	for(int z1=0;z1<j;z1++)
		//if( Arr[x1][z1] < Arr[x1][z1-1] )
		if( !(Arr[x1][y1] >= Arr[x1][z1]) )
			result_row = false;
	// column
	for(int z2=0;z2<i;z2++)
		//if( Arr[z2][y1] < Arr[z2-1][y1] )
		if( !(Arr[x1][y1] >= Arr[z2][y1]) )
			result_column = false;

	if(result_column||result_row)
		result = true;
	else
		result = false;
	return result;
}	

int main(){
	
	ifstream input("B-large.in");
	ofstream output("output");
	string s,out;
	int tours,i,j;
	input>>tours;
	for(int z=1;z<=tours;z++) {
		input>>i>>j;
		int** Array = new int*[i];
		for(int i1 = 0; i1 < i; i1++)
		    Array[i1] = new int[j];
		for(int z1=0;z1<i;z1++)
			for(int z2=0;z2<j;z2++)
				input>>Array[z1][z2];
		bool out = true;
		for(int q1=0;q1<i;q1++){
			for(int q2=0;q2<j;q2++){
				if(!check_line(q1,q2,i,j,Array)){
					out = false; break;}}
			if(!out){
				break;}}
		if(out)
		{ output<<"Case #"<<z<<": "<<"YES"<<endl; }
		else
		{ output<<"Case #"<<z<<": "<<"NO"<<endl; }
		delete[] Array;
	}
	return 0;
	
}
