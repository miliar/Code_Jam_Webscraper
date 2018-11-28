#include<iostream>
#include<fstream>

using namespace std;

int main(int argc, char** argv){

	ifstream in(argv[1]);
	ofstream out(argv[2]);
	int num_cases=0;

	in >> num_cases;

	for (int c = 1 ; c <= num_cases ; ++c){
		int max_shyness = 0;
		int peopleup = 0;
		int friends = 0;
		string a;
		in >> max_shyness;
		in >> a;
		peopleup = a[0]-'0';
		for (int i = 1 ; i <= max_shyness ; ++i){
			if ( i <= peopleup ) {
				peopleup+=(a[i]-'0');
			} else {
				int f = i - peopleup;
				peopleup += f + (a[i]-'0');
				friends += f;
			}
		}
		out << "Case #" << c << ": " << friends << endl; 
	}
return 0;
}
