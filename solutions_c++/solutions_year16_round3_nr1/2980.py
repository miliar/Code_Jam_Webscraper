#include <iostream>
#include <fstream>
#include <string>
#include <stack>
#include <algorithm>

using namespace std;

#define F(i, n) for(int i=0; i<n; i++)

int main(){
	ofstream myfile;
	myfile.open("output.txt");

	ifstream myReadFile;
	myReadFile.open("A-small-attempt1.in");

	int t;

	myReadFile >> t;

	F(i,t){
		int m;

		myfile << "Case #" << i+1 << ": ";
		myReadFile >> m;

		string s;
		string ss;

		F(j,m){
			myReadFile >> ss;
			s += ss;
		}

		while(1){
			int mm = 0;
			int ind = -1;

			//find max
			F(k, m){
				int ii = stoi(s.substr(k, 1));
				if(ii>mm){
					mm = ii;
					ind = k;
				}
			}

			//reject 1st
			F(k, m){
				int ii = stoi(s.substr(k, 1));
				if(ii==mm){
					s.replace(k,1,to_string(ii-1));
					char o = static_cast<char>(k+65);
					myfile << o;
					break;
				}
			}

			mm=0;
			ind=-1;
			int sum = 0;

			//find max
			F(k, m){

				int ii = stoi(s.substr(k, 1));

				sum+=ii;

				if(ii>mm){
					mm = ii;
					ind = k;
				}
			}

			if(mm == 0){
				break;
			}

			if(sum == 2){
				myfile << " ";
				continue;
			}

			//reject 2nd
			F(k, m){
				int ii = stoi(s.substr(k, 1));
				if(ii==mm){
					s.replace(k,1,to_string(ii-1));
					char o = static_cast<char>(k+65);
					myfile << o << " ";
					break;
				}
			}

			bool end = false;

			F(k, s.length()){
				int ii = stoi(s.substr(k, 1));
				if(ii!=0){
					break;
				}
				if(k+1==s.length()){
					end = true;
					break;
				}
			}


			if(end){
				break;
			}		

		}
		myfile << endl;
	}
	
}
