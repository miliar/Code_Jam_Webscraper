#include <iostream>
#include<string>
#include <fstream>
#include <sstream>
#include <vector>
#include <cmath>

#include "stdio.h"
#include <stdlib.h>

using namespace std;

vector<long long> combine(int in){

	int bits = in - 2;

	int nums = pow ((double)bits, 2);

	vector<long long> result;

	string full = "1";

	for (long long i = 0; i < nums; i++) {
		string inter = "";

		if (i == 0) {
			inter = "0";
		}
		else {
			long long all = i;
			while (all > 0) {
				long long res = all % 2;
				string res_s;
				stringstream ss;
				ss << res;
				ss >> res_s;
				inter = res_s + inter;
				all /= 2; 
			}
		}

		while  (inter.size() < bits) {
			inter = "0" + inter;
		}
		full = "1" + inter + "1";
		
		stringstream ss;

		ss << full;

		long long temp = 0;

		ss >> temp;

		result.push_back ( temp );

	}


	return result;
}


vector<long long> in_dif_bi (long long in) {

	long long input = in;

	vector<long long> value(9,0);
	string tmp;

	int count = 0;

	while (in > 0) {
		long long res = in % 10;
		 
		for (int i =0; i < 9; i++) {
			value[i] = value[i] + res * pow(double((i+2)), count);
		}
		count++;
		in = in / 10;
	
	}

	return value;
}

bool is_prime(long long a)
{
	for(long long i = 2;i <= pow(a, 0.5); i++) {
		if(a%i==0) {
			return false;
		}
	}
	return true;
}

long long find_small (long long a) {

	for (long long i = 2; i <= pow(a, 0.5); i++ ) {
		if ( a%i == 0 ) {
			return i;
		}
	}

	return 0;

}


bool is_ok (vector<long long> in) {


	for (long long i = 0; i < in.size(); i++ ) {
		if ( is_prime(in[i]) ) {
			return false;
		}
	}

	return true;

}



vector<long long> trans_to_small ( vector<long long> in) {
	vector<long long> result(9,0);

	for (long long i = 0; i < in.size(); i++) {
	
		result[i] = find_small (in[i]);
	
	}

	return result;

}


int main() {


	

	long long lines = 0;

	long long bits = 0;

	long long j_lines = 0;


	string tmp;

	ifstream in("C:/Users/Liao/Desktop/2/C-small-attempt1.in");

	ofstream out("C:/Users/Liao/Desktop/2/out.txt");


	getline(in, tmp);

	lines = atoi (tmp.c_str());

	long long count = 1;

	while (count <= lines) {
		
		out << "Case #" << count << ":" << endl;
		
		in >> tmp;
		bits = atoi ( tmp.c_str() );




		in >> tmp;
		
		j_lines = atoi ( tmp.c_str() );


		vector<long long> all_posi = combine(bits);

		long long count_ok = 0;

		for ( long long i = 0; i < all_posi.size(); i++) {
			cout << all_posi[i] << endl;
			
			vector<long long> now = in_dif_bi (all_posi[i]);

			


			if ( is_ok(now)  ) {

				vector<long long> output = trans_to_small (now);
				

				out << all_posi[i];

				for (int i = 0; i < output.size(); i++) {
					out << " " << output[i];
				}

				out << endl;
			
				count_ok++;
				if (count_ok >= j_lines){
					break;
				}
			}

		}

		



		
		count++;
	}



	in.close();
	out.close();



	return 0;
}