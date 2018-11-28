#include <fstream>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;


vector<int> process(istream& ip){
	size_t N;
	ip >> N;
	vector<int> input(N*(2*N-1));
	for (size_t i = 0; i < N*(2*N-1);++i)
		ip >> input[i];
	for (size_t i = 0; i < N*(2*N-1)-1; ++i)
		for (size_t j = i+1; j < N*(2*N-1); ++j)
			if (input[i]>input[j]) swap(input[i],input[j]);
	vector<int> sortindexlist;
	sortindexlist.push_back(0);
	for (size_t i = 0; i < N*(2*N-1); ++i){ //guaranteed that there is solution
		if (input[i] == input[sortindexlist.back()]) continue;
		sortindexlist.push_back(i);
	}
	sortindexlist.push_back(N*(2*N-1));
	vector<int> countlist;
	for(size_t i = 0; i < sortindexlist.size()-1; ++i)
		countlist.push_back(sortindexlist[i+1]-sortindexlist[i]);
	vector<int> result;
	for(size_t i = 0; i < countlist.size(); ++i)
		if (countlist[i]%2==1) result.push_back(input[sortindexlist[i]]);
	return result;
}

int main(int argc, char **argv){
	ifstream ip(argv[1]);
	ofstream op("output.txt");
	size_t T;
	ip >> T;
	for (size_t i = 1; i <= T; ++i){
		op << "Case #" << i << ": ";
		vector<int> result = process(ip);
		for (size_t j = 0; j < result.size(); ++j)
			op << result[j] << ' ';
		op << endl;
	}
	op.close();
	ip.close();
	return 0;
}