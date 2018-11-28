#include <iostream>
#include <vector>
#include <sstream>
#include <fstream>

using namespace std;

int foo(vector<int> a) {
	int curr = 0;
	int len = a.size();
	int ret = 0;
	for (int i = 0; i < len; i++) {
		if (curr < i) {
			ret += (i - curr);
			curr += (i - curr + a[i]);
		}
		else {
			curr += a[i];
		}
	}
	return ret;
}

int main() {
	string line;
  	ifstream myfile ("A-large.in");
  	int count = 1;
  	int num, size, invite;
  	ofstream ofile;
  	ofile.open("output_large.txt");
  	if (myfile.is_open()) {
		getline(myfile, line);
		num = atoi(line.c_str());
  		while (getline(myfile,line)) {
  			istringstream ss(line);
  			string max, shy;
  			ss>>max>>shy; 
  			size = atoi(max.c_str());

			vector<int> test(size+1, 0);
			for (int i = 0; i < size+1; i++) {
				test[i] = shy[i] - 48;
			}
			invite = foo(test);
			ofile<<"Case #"<<count<<": "<<invite<<endl;
			test.erase(test.begin(), test.begin()+size);
			count++;
  		}
  	}
  	//ofile.close();
}