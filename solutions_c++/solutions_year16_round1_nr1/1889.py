#include <fstream>
#include <string>

using namespace std;

string process (const string& input){
	string result = "";
	if (input.size() == 0) return result;
	else result.push_back(input[0]);
	for (size_t i = 1; i < input.size(); ++i){
		if (input[i]>= result[0]) result.insert(result.begin(),input[i]);
		else result.push_back(input[i]);
	}
	return result;
}


int main(int argc, char** argv){
	ifstream ip(argv[1]);
	ofstream op("output.txt");
	size_t T;
	ip >> T;
	string input;
	for (size_t i = 1; i <= T; ++i){
		ip >> input;
		op << "Case #" << i << ": ";
		op << process(input);
		op << endl; 
	}
	op.close();
	ip.close();
	return 0;
}