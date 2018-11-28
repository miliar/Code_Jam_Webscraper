#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;
typedef __int64 ll;

inline void shrinkPancake(vector<int>& pancake)
{
	int length = pancake.size();
	for (int i = 1; i < length; i++){
		if (pancake[i - 1] == pancake[i]){
			pancake[i - 1] = -1;
		}
	}
	if (pancake[length - 1] == 1){
		pancake[length - 1] = -1;
	}
	pancake.erase(remove(pancake.begin(), pancake.end(), -1), pancake.end());

}


void calc(int t, vector<int> pancake)
{
	ll minFlipCount = -1;
	shrinkPancake(pancake);
	cout << "Case #" << t << ": " << pancake.size() << endl;
}
inline vector<int> str2vector(string pancake){
	vector<int> ret;
	unsigned int length = pancake.size();
	for (int i = 0; i < length; i++){
		int p = -1;
		if (pancake[i] == '+') p = 1;
		if (pancake[i] == '-') p = 0;
		if (p == -1){
			cerr << "err";
			exit(-1);
		}
		ret.push_back(p);
	}
	return ret;
}

int main(int argc, char** argv)
{
	if (argc < 2){
		std::cerr << "input file" << std::endl;
		return -1;
	}
	string outfile(argv[1]);
	outfile = outfile.substr(0, outfile.find_last_of(".")) + "_out.txt";
	FILE *file = new FILE;
	if (freopen_s(&file, outfile.c_str(), "w", stdout)){
		fprintf(stderr, "error redirecting stdout\n");
		exit(1);
	}


	std::ifstream ifs(argv[1]);
	std::string str;
	if (ifs.fail()){
		std::cerr << "fail" << std::endl;
		fclose(file);
		return -1;
	}

	getline(ifs, str);
	int T = stoi(str);
	int idx = 1;
	while (getline(ifs, str))	{
		auto pancake = str2vector(str);
		calc(idx++, pancake);
	}

	fclose(file);
	return 0;
}