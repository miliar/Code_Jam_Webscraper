#include <iostream>
#include <string>
#include <fstream>
#include <stdlib.h>
#include <sstream>
#include <math.h>
using namespace std;

string int_to_str(long long int number)
{
    stringstream ss;
    ss << number;
    return ss.str();
}

bool palindrome(string input) {
    return input == string(input.rbegin(), input.rend());
}

int main() {
    ifstream fin("/Users/usamaelnily/Desktop/in.txt");
    ofstream fout("/Users/usamaelnily/Desktop/out.txt");
    
    long long int t, c = 1, a, b;
    string x;
    fin >> t;
    while(t--) {
        int ans = 0;
        fin >> a >> b;
        
        for(long long int i = a; i <= b; i++) {
            if(palindrome(int_to_str(i)) && palindrome(int_to_str(sqrt(i))) && (((sqrt(i) - (int)sqrt(i)) == 0)))
                ans++;
        }
        
        fout <<"Case #" << c << ": " << ans << endl;
        c++;
    }
    return 0;
}