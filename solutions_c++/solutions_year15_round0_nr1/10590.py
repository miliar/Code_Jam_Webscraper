#include<iostream>
#include<fstream>
#include<cstring>
#include<string>
#include<cmath>
using namespace std;

int main()
{
	ifstream in;
	ofstream out;
	int Count =0;
	int Extras = 0;
	in.open("input.txt");
	out.open("output.txt", ios::out);
	char dump;
	string s;
	int No;
	int Val;
	int NoOfPeople;
	int * List = NULL;
	getline(in, s);
	No = stoi(s);
	for( int i = 0; i < No; i++) {
		Count = 0;
		Extras = 0;
		in >> NoOfPeople;
		getline(in, s);
		Val = stoi(s);
		List = new int[NoOfPeople+1];

		for( int j = NoOfPeople; j >=0 ; j--) {
			List[NoOfPeople-j] = Val/pow(10,j);
			Val = Val-(List[NoOfPeople-j]*pow(10,j));
		}

		for(int a =0 ; a < NoOfPeople+1; a++) {
			if(List[a] != 0) {
				if(Count < a) {
					Extras = Extras - Count + a;
					Count = a;
				}
				Count = Count + List[a];
			}
		}
		out << "Case #" << i +1 << ": " << Extras << '\n';
	}
	
}