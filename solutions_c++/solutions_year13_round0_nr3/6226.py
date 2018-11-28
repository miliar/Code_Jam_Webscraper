#include <iostream>
#include <string>
#include <fstream>
#include <vector>
using namespace std;

const int MAX_DIGIT = 1000;
vector<unsigned long long> result; 
int A, B;
int T;

bool is_fair(long long value)
{
	int i = 0;
	int digit[MAX_DIGIT];
	while (value > 0){
		digit[i++] = value % 10;
		value /= 10;  
	}
	for (int j = 0 ; j < i ; ++j){
		if (digit[j] != digit[i-j-1])
			return false;
	}
	return true;		
}

int main()
{
	ifstream input("in.txt");
	if (!input)
		return -1;
	for (unsigned long long i = 1 ; i <= 10000000; ++i){
		if (is_fair(i) && is_fair(i*i)){
			result.push_back(i*i);
		}
	}
	input >> T;
	for (unsigned long long i = 0; i < T ; ++i){
		input >> A >> B;
		int ans = 0;
		vector<unsigned long long>::iterator iter;
		for (iter = result.begin() ; iter != result.end() ; ++iter){
			if ((A<=*iter) && (*iter<=B))
				++ans;
		}
		cout << "Case #" << i+1 << ": " << ans << endl;
	}		
	return 0; 
}
