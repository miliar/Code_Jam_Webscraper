#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>

using namespace std;

int main(){
	ifstream input("B-small-attempt0.in");
	ofstream output("B-small-attempt0.out");
	
	int t, cs = 1;
	input >> t;
	
	int A, B, K;

	while(t--){
		input >> A >> B >> K;
		
		int ans = 0;
		
		for(int i=0; i<A; i++){
			for(int j=0; j<B; j++){
				if((i&j) < K)
					ans++;
				//output << (i&j) << endl;
			}
		}
		output << "Case #" << cs << ": " << ans << endl;
	
		cs++;
	}
	
	return 0;
}
