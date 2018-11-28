#include<fstream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;
bool com(long long n, long long &d){
	if (n <= 11){
		if (n == 0 || n == 1 || n == 2 || n == 3 || n == 5 || n == 7 || n == 11)
			return false;
		else{
			d = (n == 9) ? 3 : 2;
			return true;
		}
	}
	long long z = sqrt(n);
	if (n % 2 == 0){
		d = 2;
		return true;
	}
	for (long long i = 3; i <= z + 1;){
		if (n%i == 0){
			d = i;
			return true;
		}
		i += 2;
	}
	return false;
}
void generate(string s, int n, int &stop, ofstream &out){
	if (stop == 50)
		return;
	if (n == 0){
		bool ok = true;
		string f = string("1") + s + "1";
		vector<long long> div;
		for (int j = 2; j <= 10; ++j){
			long long n = stoll(f, 0, j), div2;
			if (!com(n, div2)){
				ok = false;
				break;
			}
			else
				div.push_back(div2);
		}
		if (ok){
			out << f << ' ';
			for (auto i : div)
				out << i << ' ';
			out << endl;
			++stop;
		}
	}
	else{
		generate(s + "0", n - 1, stop, out);
		generate(s + "1", n - 1, stop, out);
	}
}
int main(){
	ofstream out("output.txt");
	int stop = 0;
	out << "Case #1:" << endl;
	generate("", 14, stop, out);
}
