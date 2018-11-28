#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <cctype>
#include <algorithm>
#include <string>

using namespace std;

vector<int> convert(string seq){
	vector<int> output;
	output.resize(seq.size());
	for(int i =0; i< seq.size(); i++){
		switch (seq[i]){
			case 'i': 
				output[i] = 2; 
			break;
			case 'j':
				output[i] = 3;
			break;
			case 'k':
				output[i] = 4;
			break;
		}
	}
	return output;
}

int mult(int x, int y){
	/*
	if(x == 1){
		return y;
	}
	else if( y == 1){
		return x;
	}
	else if( x < 0 ){
		return -1*mult(-1*x, y);
	}
	else if( y < 0){
		return -1*mult(x, -1*y);
	}
	else if(x == y){
		return -1;
	}
	//i = 2
	else if( x == 2){
		if(y == 3){
			return 4;
		}
		else if(y == 4){
			return -3;
		}
	}
	//j = 3
	else if( x == 3){
		if( y == 2){
			return -4;
		}
		else if( y == 4){
			return 2;
		}
	}
	//k = 4
	else if (x == 4){
		if( y == 2){
			return 3;
		}
		else if( y == 3){
//cout << "hai" << endl;
			return -2;
		}
	}
	cerr << "Error encountered " << x << " " << y << endl;
	return 0;		
	*/

	if(x < 0){
		return -1*(mult (-1*x, y));
	}
	if(y < 0){
		return -1*(mult (x, -1*y));
	}

	vector< vector<int> > table;
	vector<int> temp_row;

	temp_row.resize(4);
	temp_row[0] = 1;
	temp_row[1] = 2;
	temp_row[2] = 3;
	temp_row[3] = 4;
	table.push_back(temp_row);	
	
	temp_row[0] = 2;
	temp_row[1] = -1;
	temp_row[2] = 4;
	temp_row[3] = -3;
	table.push_back(temp_row);


	temp_row[0] = 3;
	temp_row[1] = -4;
	temp_row[2] = -1;
	temp_row[3] = 2;
	table.push_back(temp_row);


	temp_row[0] = 4;
	temp_row[1] = 3;
	temp_row[2] = -2;
	temp_row[3] = -1;
	table.push_back(temp_row);
	
	return(table[x-1][y-1]);
}

int seq_mult( vector<int> seq){
	int start = 1;
	for(int i =0; i< seq.size(); i++){
		start = mult(start, seq[i]);
		//cout << start << " ";
	}
	//cout << endl;
	return start;
}

string solution(long long int repeats, vector<int> seq){
	int seq_prod = seq_mult(seq);
	int chk_prod = 1;
	for(int i = 0; i < repeats; i++){
		//cout << chk_prod << " ";
		chk_prod = mult(chk_prod, seq_prod);
	}
	//cout << endl;
	//cout << chk_prod << endl;
	if(chk_prod != -1){
		return "NO";
	}
	//cout << "Passed the first check" << endl;
	chk_prod = 1;
	int index = 0;
	//find an i
	while(index <= (repeats)*seq.size()){
		if(chk_prod == 2){
			break;
		}
		else{
			chk_prod = mult(chk_prod, seq[index%seq.size()]);
			index++;
		}
	}
	//cout << "Found an i" << endl;
	//find a j
	chk_prod = 1;
	while(index <= (repeats)*seq.size()){
		if(chk_prod == 3){
			break;
		}
		else{
			chk_prod = mult(chk_prod, seq[index%seq.size()]);
			index++;
		}

	}
	//cout << "Found a j" << endl;

	//find a k
	chk_prod = 1;
	while(index <= (repeats)*seq.size()){
		if(chk_prod == 4){
			return "YES";
		}
		else{
			chk_prod = mult(chk_prod, seq[index%seq.size()]);
			index++;
		}
	}
	return "NO";

}

int main(){
	/*
	for(int i =1; i<=4 ; i++){
		for(int j =1; j<=4; j++){
			cout << mult(i,j) << " ";
		} 
		cout << endl;
	}
	*/
	int num_case;
	cin >> num_case;

	for(int n =0; n< num_case; n++){
		long long int string_length;
		long long int repeats;

		string seq;

		cin >> string_length;
		cin >> repeats; 
		cin >> seq;
		
		//for(int i = 0; i < seq.size(); i++){
			//cout << seq[i];
		//}
		cout << "Case #" << n+1 << ": " << solution(repeats, convert(seq) ) << endl;

				
	}

}
