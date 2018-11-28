#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <math.h>
#include <gmpxx.h>
#include <algorithm>
#include <assert.h>

std::string find_min(const std::string& val) {

	std::string t;
	t.append(1, val[0]);
	char c = val[0];
	for(int i =1; i < val.size();++i) {
		if(c != val[i]) {
			t.append(1, val[i]);
			c =val[i];
		}
	}
	return t;
}

void solve(std::ifstream& in)
{
	std::string s[100];
	
	int n;
	in >> n;

	for(int i =0; i < n;++i) {
		in >> s[i];
	}
	std::string m= find_min(s[0]);
	for(int i =1;i < n;++i) {
		std::string t = find_min(s[i]);
		if(m.size() != t.size() || m !=t) {
			printf("Fegla Won\n");
			return;
		}
	}
	int pos[100];
	int result =0;
	memset(pos, 0, sizeof(pos));
	for(int i =0; i < m.size();++i) {
		int d[100];
		int t =0;
		for(int j =0; j < n;++j) {
			d[j] =0;
			while (s[j][pos[j]] == m[i]) {
				t++;
				d[j]++;
				pos[j]++;
			}
		}
		int ave =t/n;
		if(t%n >=n/2) {
			ave++;
		}
		for(int j =0; j <n;++j) {
			result += abs(d[j] - ave);
		}
	}

	printf("%d\n", result);
}
int main(int argc, char* argv[]) 
{
	if(argc < 2) {
		std::cerr << "missing input file\n" ;
		return 1;
	}

	std::ifstream in(argv[1]);
	int c ;
	in  >> c;
	for(int i =1; i <=c;++i) {
		printf("Case #%d: ", i);
		solve(in);
	}
	return 0;
}
