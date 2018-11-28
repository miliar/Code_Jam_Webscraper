#include <iostream>
#include <string>
#include <fstream>
#include <stdlib.h>

using namespace std;

class algorithm {
private:
	ifstream in;
	ofstream out;
	int process_case(){
		unsigned long long r , T, count, counter;
		int i= 0;		
		//max--;
		in >> r >> T;
		//cout << r <<"   " << T  << endl;
		//cout << row <<"  " << col << " "<<r_2<<" " << check << endl;
		counter = 2 * r + 1;
		count = counter;
		while(count <= T){
			i++;
			counter += 4;
			count += counter;
		}
		return i;
	}

public:
	void solution(char *input, char *output) {
		string strInput;
		int count;
		int num=1;

		in.open(input, ios::in);
		out.open(output, ios::out);

		getline(in, strInput);
		count = atoi(strInput.c_str());
		while(count) {
			int ret = process_case();
			out << "Case #" << num << ": "<< ret << endl;
			//out << ret << endl;
			num++;
			count--;
		}
		in.close();
		out.close();
	}
};

int main() {
	algorithm a;
	a.solution("./src/input", "./src/output");
	return 0;
}
