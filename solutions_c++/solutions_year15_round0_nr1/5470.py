#include<iostream>
#include<fstream>
#include<string>
using namespace std;

int main(){

	ofstream out;
	ifstream in;
	
	in.open("C:\\Users\\Mohammad\\Desktop\\CodeJam\\A-small-attempt8.in");
	out.open("C:\\Users\\Mohammad\\Desktop\\CodeJam\\output.txt");

	string str;
	long a, b, sum;
	in >> a;
	for (int t = 1; t <= a; t++){
		in >> b;
		in >> str;
		long sum = 0;
		long count = 0;
		for (int i = 0; i <= b; i++)
			if (((int)str[i] - 48) != 0)
			{
			if (i <= sum)
				sum += (int)str[i] - 48;
			else
			{
				count += i - sum;
				sum += count;
				sum += (int)str[i] - 48;

				
			}
			}
		
		out << "Case #" << t << ": " << count << endl;
	}
	out.close();
	in.close();

	//system("pause");
}