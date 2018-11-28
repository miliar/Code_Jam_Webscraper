#include <iostream>
#include <fstream>
using namespace std;


long int T,N;
bool seen[10];


int main(){
	ifstream in("input");
	ofstream out("output");

	in >> T;
	for(int i =1; i <= T; i++){
		out << "Case #" << i << ": ";
		in >> N;
		long int left = 10;
		for(int j =0; j < 10; j++){ seen[j] = false;}

		if( N == 0 ){ out << "INSOMNIA" << endl;}
		else{
			long int multWith= 0;
			while(left > 0){
				multWith++;
				long int num = N*multWith;
				//cout << num << endl;
				//cout<< "broken into : ";
				while(num>0){
					long int rem = num%10;
					//cout << rem << "  ";
					if(!seen[rem]){ left--; seen[rem] = true;}
					num = num/10;
				}
			}
			out << N*multWith << endl;
		}

	}
}