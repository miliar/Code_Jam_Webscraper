#include <iostream>
#include <fstream>
#include <math.h>
#include <algorithm>    // std::sort
#include <vector>       // std::vector
#include <string>
#include <random>
#include <cassert>

// Run as ./CoinJam < input.txt

using namespace std;

bool is_prime(long long n, int &k) {
    int temp = floor( sqrt( n ) );
    for(int i = 2; i <= temp; i++) {
        if(n % i == 0) {
            k = i;
            return false;
        }
    }
    return true;
}

bool is_coin(int *n, int *divs, int N) {
    // Check whether n is a coin
    if (n[0] == 0 || n[N-1] == 0) { return false; }
    
    for(long long d = 2; d <= 10; d++) {

        // Construct the number in decimal system d
        long long num = 0;
        long long fact = 1;
        for(int i = N-1; i >= 0; i--) {
            num += n[i]*fact;
            fact *= d;
        }
        
        // Check if it is a prime
        int k;
        if (!is_prime(num, k)) {
            // Sanity check that k is really a divisor of num
            assert(num % k == 0);
            divs[d-2] = k;
        }
        else {
            return false;
        }
    }
    
    return true;
}

string print_me(int *num, int *divs, int N) {
    string str = "";
    for(int i = 0; i < N; i++) {
        str += std::to_string(num[i]);
    }
    for(int j = 0; j < 9; j++) {
        str += " ";
        str += std::to_string(divs[j]);
    }
    return str;
}

string num_to_string(int *num, int N) {
    string str = "";
    for(int i = 0; i < N; i++) {
        str += std::to_string(num[i]);
    }
    return str;
}

bool not_used(std::vector<string> &used, int* num, int N) {
    string nnum = num_to_string(num, N);
    for(int i = 0; i < used.size(); i++) {
        if (nnum.compare(used[i]) == 0) {
            return false;
        }
    }
    used.push_back(nnum);
    return true;
}

int main(int argc, const char *argv[]) {
    
    const int N = 16;
    const int J = 50;
    int nfound = 0;
    
    random_device rd;
    default_random_engine e(rd());
    uniform_int_distribution<int> randi(0, 1);
    
    // Print outcome
    ofstream myfile;
    myfile.open ("output.txt");
    myfile << "Case #1:" << endl;
    
    // Represent each number by a vector
    int num[N];
    num[0] = 1;
    num[N-1] = 1;
    int divs[9];
    
    // Store the numbers found using a vector of strings
    std::vector<std::string> used;
    
    // Randomized algorithm
    while (nfound < J) {
        
        // Generate a  random coin
        for(int i = 1; i < N-1; i++) {
            num[i] = randi(rd);
        }
        
        // Check if the satisfies the assumptions and that it is new
        if ( is_coin(num, divs, N)) {
            if (not_used(used, num, N)) {
                myfile << print_me(num, divs, N) << endl;
                nfound++;
            }
        }
    }
}