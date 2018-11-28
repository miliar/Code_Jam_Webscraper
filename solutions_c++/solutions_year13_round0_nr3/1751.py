#include<iostream>
#include<fstream>
#include<sstream>
#include<string>
#include<vector>
#include<cmath>
using namespace std;

bool palindrome(long long n) {
    stringstream ss;
    string s;
    ss<<n;
    ss>>s;

    for(int i = 0, j = s.length() - 1; i < j;) {
        if(s[i++] != s[j--]) return false;
    }

    return true;
}

void calc_palindrome(vector<long long> &p, long long a, long long b) {
	long long r_a = sqrt(double(a));
    long long r_b = sqrt(double(b));

    long long i = (r_a * r_a == a ? r_a : r_a + 1);
    for(; i <= r_b; ++i) {
        if(palindrome(i) && palindrome(i*i)) p.push_back(i*i);
    }
}

int fairsquare(vector<long long> &p, long long a, long long b) {
    int count = 0;

    vector<long long>::iterator it = p.begin();
    for(; it != p.end(); ++it) {
        if(*it >= a && *it <= b) ++count;
    }
        
    return count;
}

int main(int argc, char **argv) {
    ifstream input(argv[1], ios::in);
    ofstream output("output.txt", ios::out);

    int T;
    input>>T;
    
	vector<long long> p;
    calc_palindrome(p, 1, 100000000000000);
    for(int t = 1; t <= T; ++t) {
        long long a, b;
        input>>a>>b;
        output<<"Case #"<<t<<": ";
        output<<fairsquare(p, a, b)<<endl;
    }
 
    return 0;
}
