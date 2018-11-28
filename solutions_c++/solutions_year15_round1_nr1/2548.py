#include <fstream>
#include <iostream>
#include <vector>
using namespace std;

int main(int argc, char* argv[]){

	string fin = argv[1];
	ifstream istr(fin.c_str());

	ofstream ostr(argv[2]);

	int t,num;
	float max=0.0;
	float first,second,total1,total2;
	float diff = 0.0;
	istr >> t;

	for (int i=0;i<t;i++){

		istr >> num;
		istr >> first;
		vector<float> values;
		values.push_back(first);

		for (int j=0;j<num-1;j++){

			istr >> second;
			values.push_back(second);
			if (first > second) total1 += (first-second);
			if (max < (first-second)) max = (first-second);
			if (diff < (first-second)) diff = (first-second);

			first = second;

		}

		first = values[0];
		for (unsigned int j=1;j<values.size();j++){

			second = values[j];
			if (diff >= first) total2 += first;
			else total2 += diff;
			first = second;
		}


		ostr << "Case #" << i+1 << ": " << int(total1) << ' ' << int(total2) << endl;
		total1 = 0.0;
		total2 = 0.0;
		diff = 0.0;

	}

}