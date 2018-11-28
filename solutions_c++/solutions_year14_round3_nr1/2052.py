#include <iostream>
#include <vector>
#include <utility>
#include <fstream>
#include <climits>
#include <iomanip>
#include <algorithm>
#include <set>
#include <list>
#include <cmath>
#include <map>
#include <string>
#include <sstream>

using namespace std;

ofstream output;

bool IsPowerOfTwo(int x)
{
    return (x & (x - 1)) == 0;
}

int main(int argc, char* argv[])
{
    ifstream input;
    
    input.open(argv[1]);
    output.open("output.out");
    
    int T;
    input >> T;
    
    for (int i = 1; i <= T; i++) {
        string str, str_P, str_Q;
        input >> str;
        istringstream iss(str);
        getline(iss, str_P, '/');
        getline(iss, str_Q, '/');
		int P, Q;
		P = atoi(str_P.c_str());
		Q = atoi(str_Q.c_str());

		if (Q%P == 0 && Q/P != 1) {
			Q = Q/P;
			P = 1;
		}
        
		output << "Case #" << i << ": ";
        
		if (IsPowerOfTwo(Q) == false) {
			//output << Q << "is not power of 2" << endl;
			output << "impossible";
		} else {
			int ans = 1;
			int tmp = Q/2;
			while (P < tmp) {
				tmp /= 2;
				ans++;
			}
			
			//if (ans > 40)
			//	output << "impossible";
			//else 
				output << ans;
		}
                
        if (i != T)
           output << endl;
    }
}

