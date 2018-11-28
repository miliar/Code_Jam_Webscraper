#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
using namespace std;


int main(){

	int T; cin >> T;
	string in;
	ofstream out;
	out.open("outputA.txt");
	for (int i = 1; i <= T; i++)
	{
		int count = 0;
		cin >> in;
		for (int k = 1; k < in.length(); k++)
		{
			if (in[k] != in[k - 1])count++;
		}
		if (in[in.length() - 1] == '-') { count++; }
		 out << "Case #" << i << ": "<<count<<"\n";
	}


	out.close();

	return 0;
}