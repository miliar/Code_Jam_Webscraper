#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cassert>
using namespace std;



int ovation(vector<int>& shyness) {
	assert( !shyness.empty() );
	int res = 0, sum = shyness[0];
	
	for (int k=1; k<shyness.size(); k++) {
		if (sum < k) {
			res += (k - sum);
			sum += (k - sum);
		}
		sum += shyness[k];
		
		// if (sum >= k) {
			// sum += shyness[k];
		// } else {
			// res += (k - sum);
			// sum += (k - sum);
			// sum += 
		// }
	}
	
	return res;
}

int main(int argc, char* argv[]) 
{
	if (argc != 2) {
		cout << "Nothing" << endl;
	}
	
	int numTCs, maxLv;
	string shy_str;
	
	fstream fin(argv[1]);
	if ( !fin.is_open() ) cerr << "File open error" << endl;
	
	fin>>numTCs;
	for (int i=0; i<numTCs; i++) {
		fin>>maxLv>>shy_str;
		// cout<<maxLv<<" "<<shy_str<<endl;
		vector<int> shyness(shy_str.size());
		
		for (int j=0; j<shy_str.size(); j++) {
			shyness[j] = shy_str[j]-'0';
		}
		
		int res = ovation(shyness);
		cout<<"Case #"<<(i+1)<<": "<<res<<endl;
	}
	
	
	fin.close(); fin.clear();
	return 0;
}