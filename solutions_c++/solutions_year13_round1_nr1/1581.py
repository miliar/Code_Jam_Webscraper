#include <iostream>
#include <string>
#include <algorithm>
#include <fstream>


using namespace std;


bool checkXWon(string a, string b, string c, string d){


	replace(a.begin(), a.end(), 'T','X');
	replace(b.begin(), b.end(), 'T','X');
	replace(c.begin(), c.end(), 'T','X');
	replace(d.begin(), d.end(), 'T','X');
	
	

	if(a[0]=='X' && b[0]=='X' && c[0]=='X' && d[0]=='X')
		return true;
	else if(a[1]=='X' && b[1]=='X' && c[1]=='X' && d[1]=='X'){
		return true;
	}
	else if(a[2]=='X' && b[2]=='X' && c[2]=='X' && d[2]=='X'){
		return true;
	}
	else if(a[3]=='X' && b[3]=='X' && c[3]=='X' && d[3]=='X'){
		return true;
	}
	else if(a == "XXXX")
		return true;
	else if(b == "XXXX"){
		return true;
	}
	else if(c == "XXXX"){
		return true;
	}
	else if(d == "XXXX"){
		return true;
	}
	else if(a[0]=='X' && b[1]=='X' && c[2]=='X' && d[3]=='X'){
		return true;
	}
	else if(a[3]=='X' && b[2]=='X' && c[1]=='X' && d[0]=='X'){
		return true;
	}


	return false;

}

bool checkYWon(string a, string b, string c, string d){
	
	
	
	replace(a.begin(), a.end(), 'T','O');
	replace(b.begin(), b.end(), 'T','O');
	replace(c.begin(), c.end(), 'T','O');
	replace(d.begin(), d.end(), 'T','O');
	
	

	if(a[0]=='O' && b[0]=='O' && c[0]=='O' && d[0]=='O')
		return true;
	else if(a[1]=='O' && b[1]=='O' && c[1]=='O' && d[1]=='O'){
		return true;
	}
	else if(a[2]=='O' && b[2]=='O' && c[2]=='O' && d[2]=='O'){
		return true;
	}
	else if(a[3]=='O' && b[3]=='O' && c[3]=='O' && d[3]=='O'){
		return true;
	}
	else if(a == "OOOO")
		return true;
	else if(b == "OOOO"){
		return true;
	}
	else if(c == "OOOO"){
		return true;
	}
	else if(d == "OOOO"){
		return true;
	}
	else if(a[0]=='O' && b[1]=='O' && c[2]=='O' && d[3]=='O'){
		return true;
	}
	else if(a[3]=='O' && b[2]=='O' && c[1]=='O' && d[0]=='O'){
		return true;
	}

	return false;


}

bool checkNotFinished(string a, string b, string c, string d){

	if(a.find('.')!=string::npos)
		return true;
	
	if(b.find('.')!=string::npos)
		return true;
	
	if(c.find('.')!=string::npos)
		return true;
	
	if(d.find('.')!=string::npos)
		return true;
	

	return false;

}





int main(){

	

	ifstream file("input.in");

	ofstream outfile("output.txt");

	
	long long total;

	file >> total;


	for(int i=0;i<total;i++){


		long long r;
		file >> r;

		long long t;
		file >> t;


		long long total = 0;
		long long count = 0;
		long long a=1;

		while(total<=t){
						

			total += ((r<<1) +a);

			a+=4;

			count++;
			
		}


		outfile << "Case #" << i+1 <<": "<< count-1 << endl;


		/*


		string a;
		file >> a;
		string b;
		file >> b;
		string c;
		file >> c;
		string d;
		file >> d;
			

		string temp;
		getline(file, temp);


		if(checkXWon(a, b, c, d)){
			outfile << "Case #"<< i+1 << ": X won" << endl;
		}
		else if(checkYWon(a, b, c, d)){
			outfile << "Case #"<< i+1 << ": O won" << endl;
		}
		else if(checkNotFinished(a, b, c, d)){
			outfile << "Case #"<< i+1 << ": Game has not completed" << endl;
		}
		else {
			outfile << "Case #"<< i+1 << ": Draw" << endl;
		}
		

		*/


	}
	
	



}