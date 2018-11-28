#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

bool won(vector<vector<char> > tic, char car, bool& tie);

int main(int argc, char* argv[])
{
	ifstream in("in.txt");
	ofstream out("out.txt");
	int t;
	in >> t;
	for (int c=1; c<=t; c++) {
		int a, b;
		in >> a >> b;
		out << "Case #" << c << ": ";
		int arr[5] = {1,4,9,121,484};
		int count(0);
		for (int i=0; i <5; i++) {
			if (arr[i] >= a && arr[i] <= b) count++;
		}
		out << count << endl;

	}

}//main