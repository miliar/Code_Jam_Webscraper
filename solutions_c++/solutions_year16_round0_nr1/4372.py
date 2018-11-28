#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;
typedef __int64 ll;

void calc(int t, ll N)
{
	vector<char> target = { '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' };
	ll n = N;
	if (n == 0){
		cout << "Case #" << t << ": " << "INSOMNIA" << endl;
		return;
	}

	ll count = 1;
	while (true){
		string strN = std::to_string(n);
		for (auto& digit : target){
			if (strN.find(digit) != std::string::npos){
				digit = '*';
			}
		}
		target.erase(remove(target.begin(), target.end(), '*'), target.end());

		if (target.empty()){
			cout << "Case #" << t << ": " << n << endl;
			return;
		}
		n += N;
		count++;
	}
}

int main(int argc, char** argv)
{
	if (argc < 2){
		std::cerr << "input file" << std::endl;
		return -1;
	}
	string outfile(argv[1]);
	outfile = outfile.substr(0, outfile.find_last_of(".")) + "_out.txt";
	FILE* fpOut = freopen(outfile.c_str(), "w", stdout);


	std::ifstream ifs(argv[1]);
	std::string str;
	if (ifs.fail()){
		std::cerr << "fail" << std::endl;
		fclose(fpOut);
		return -1;
	}

	getline(ifs, str);
	int T = stoi(str);
	int idx = 1;
	while (getline(ifs, str))	{
		ll n=stoll(str);
		calc(idx++,n);
	}

	fclose(fpOut);
	return 0;
}