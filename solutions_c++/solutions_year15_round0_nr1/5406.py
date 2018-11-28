#include<iostream>
#include<fstream>
#include<string>
using namespace std;

int main(){

	ofstream out;
	ifstream in;
	
	in.open("C:\\Users\\Mohammad\\Desktop\\CodeJam\\A-small-attempt2.in");
	out.open("C:\\Users\\Mohammad\\Desktop\\CodeJam\\output.txt");

	string ABBC;
	long long a, num;
	in >> a;
	unsigned int te = 1;
	while(te <= a){
		in >> num;
		in >> ABBC;
		long long s = 0;
		long long count = 0;
		unsigned int i = 0;
		while (i <= num){
			if (((int)ABBC[i] - 48) != 0)
				if (i <= s)
					s += (int)ABBC[i] - 48;
			else{
				count += i - s;
				s += count;
				s += (int)ABBC[i] - 48;
			}
			i++;
			}
		
		out << "Case #" << te << ": " << count << endl;
		te++;
	}
	out.close();
	in.close();

	//system("pause");
}