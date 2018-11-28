#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include <vector>
#include <bitset>

using namespace std;

int main() {
        ifstream input;
        ofstream output;
        input.open("./Downloads/C-large.in");
        output.open("result20160103");

        vector<unsigned> prime(1, 2);
        for (unsigned i = 3; i < (1 << 4); i ++) {
                bool is_prime = true;
                for (unsigned j = 0; j < prime.size(); j++) {
                        if (i % prime[j] == 0) {
                                is_prime = false;
                                break;
                        }
                }
                if (is_prime){
                        prime.push_back(i);
                }
        }

        unsigned T;
        input >> T;

	for (unsigned t = 0; t < T; t ++) {
                vector<unsigned long long> empty;
                vector<vector<unsigned long long> > res;
		unsigned N, J;
		input >> N >> J;
                for (unsigned long long i = 0; i < (1 << 14); i ++) {
                        vector<unsigned long long> temp(1, (i << 1) + (1ull << 15) + 1ull);
                        for (unsigned long long j = 2; j <= 10; j ++) {
                               unsigned long long b_num = 1;
                               unsigned long long weight = 1;
                               for (unsigned w = 1; w <= 15; w ++) {
                                       weight = weight * j;
                                       if (((1ull << (w - 1)) & i) != 0) {
                                               b_num += weight;
                                       }
                               }
                               b_num += weight;
                               for (unsigned k = 0; k < prime.size(); k ++) {
                                       if (b_num % prime[k] == 0) {
                                               temp.push_back(prime[k]);
                                               break;
                                       }
                               }
                        }
                        if (temp.size() == 10) {
                                res.push_back(temp);
                                if (res.size() == J) {
                                        break;
                                }
                        }
                }

                output << "Case #" << t + 1 << ":" << endl; 
                for (unsigned i = 0; i < res.size(); i ++) {
                        output << std::bitset<16>(res[i][0]);
                        if (N == 32) {
                                output << std::bitset<16>(res[i][0]);
                        }
                        for (unsigned j = 1; j < 10; j ++) {
                                output << " " << res[i][j];
                        }
                        output << endl;
                }
	}

	return 0;
}
