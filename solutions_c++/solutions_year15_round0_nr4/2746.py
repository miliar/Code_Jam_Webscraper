#include<iostream>
#include<fstream>
#include<string>

using namespace std;

int main(int argc, char * argv[]){

fstream in_file;
in_file.open(argv[1], ios::in);

fstream out_file;
out_file.open("newXomino.out", ios::out);


int i;  // case number

in_file >> i;

int x, r, c;
string winner;

for (int k=0; k<i; k++){
	
	in_file >> x >> r >> c;
	if( (r*c)%x != 0 ) winner = "RICHARD";
	else if(x < 3) winner = "GABRIEL";
	else { 		 
		if(r<x-1 || c <x-1) winner = "RICHARD";
		else winner = "GABRIEL";
	}

//	cout     << "Case #" << k+1 << ": " << winner << endl;
	out_file << "Case #" << k+1 << ": " << winner << endl;
}

in_file.close();
out_file.close();

return 0;
}
