#include<iostream>
#include<string>
#include<fstream>
using namespace std;

int checkNumber(char s){

	int b = 0;

	if (s == '1')
		b = 1;
	else if (s == '2')
		b = 2;
	else if (s == '3')
		b = 3;
	else if (s == '4')
		b = 4;
	else if (s == '5')
		b = 5;
	else if (s == '6')
		b = 6;
	else if (s == '7')
		b = 7;
	else if (s == '8')
		b = 8;
	else if (s == '9')
		b = 9;
	else
		b = 0;

	return b;


}

int peopleInvite(string s, int t){
	int sum = 0;
	int d = 0;
	int a = 0;
	int b = 0;
	for (int i = 0; i < t + 1; i++){

		if (i == 0){

			b = checkNumber(s[i]);
			sum = sum + b;
		}
		else{

			if (s[i] != '0'){



				d = i - sum;
				if (d < 0)
					d = 0;
				a = a + d;
				b = checkNumber(s[i]);
				sum = sum + b+a;

			}


		}


	}

	return a;
}


int main(){

	int n = 0;
	ifstream fin;
	ofstream fout;

	fin.open("input.in");
	fout.open("output.out");

	fin >> n;

	if (n > 100 || n < 1)
		cout << "Test case out of bounds." << endl;
	else {
		for (int i = 0; i < n; i++){

			int t = 0, q = 0;;
			fin >> t;

			string s;
			fin >> s;

			q = peopleInvite(s, t);
			if (q < 0)
				q = 0;

			fout << "Case #" << i + 1 << ": " << q << endl;


		}
	}





	return 0;
}