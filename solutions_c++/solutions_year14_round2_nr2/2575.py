#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <string>
#include <bitset>
#include <unordered_set>

using namespace std;

int main(int argc, char* argv[]) 
{
	ifstream input(argv[1]);
    int T, A, B, K, cc=0;
	string s;

	if(input >> T)
	{
		while(cc++ < T && input >> A >> B >> K) 
		{
			long long res = 0; 
			for(int i=0; i<A; i++) {
				for(int j=0; j<B; j++) {
					if((i & j) < K) {
						//cout << i << " " << j << endl;
						res++;
					}
					
				}
			}

			cout << "Case #" << cc << ": ";
			cout << res << endl;
			
		}		
	}

	return 0;
}
