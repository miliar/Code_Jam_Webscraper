#include <fstream>
#include <vector>
#include <string>

using namespace std;

int main(){
	ifstream fin("a.in");
	ofstream fout("a.out");
	vector<long long> res;
	vector<long long> who;
	char* buf = new char[100];
	for(long long i = 1; i <= 10000001; i++){
		long long sq = i * i;
		itoa(sq, buf, 10);
		string s(buf);
		itoa(i, buf, 10);
		string s3(buf);
		string s4 = "";
		string s2 = "";
		for(int j = s.size() - 1; j >= 0; j--){
			s2 += s[j];
		}
		for(int j = s3.size() - 1; j >= 0; j--){
			s4 += s3[j];
		}
		if(s == s2 && s3 == s4){
			res.push_back(i * i);
			who.push_back(i);
		}
	}
	int t;
	fin >> t;
	for(int k = 0; k < t; k++){
		int l, r;
		fin >> l >> r;
		int cnt = 0;
		for(int i = 0; i < res.size(); i++){
			if(res[i] >= l && res[i] <= r){
				cnt++;
			}
		}
		fout << "Case #" << k + 1 << ": " << cnt << "\n";
	}
	return 0;
}