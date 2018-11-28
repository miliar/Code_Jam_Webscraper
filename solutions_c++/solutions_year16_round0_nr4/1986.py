#include <iostream>
#include <vector>
#include <string>
#include <bitset>
using namespace std;
void exe();

int main(void)
{	
	int T;
	cin >> T;
	for(int caseNum=1; caseNum<=T ; ++caseNum){
		cout << "Case #" << caseNum << ": ";
		exe();
		cout << endl;	
	}
	return 0;
}

void exe()
{
	uint64_t K, C, S;
	cin >> K >> C >> S;
	if(C*S<K) cout << "IMPOSSIBLE";
	else{
		//uint64_t KC = 1; for(auto i=C ; i>0 ; --i) KC*=K;
		for(uint64_t i=0 ; i<K ; i+=C){
			uint64_t num = 0;
			for(uint64_t j=0 ; j<C && i+j<K ; ++j) num = num*K + i+j;
			cout << num + 1;
			if(i+C<K) cout << ' ';
		}
	}
}

