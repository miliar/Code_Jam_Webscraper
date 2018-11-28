#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;


vector<long long> numbers;

bool ifPolindrome(long long number) {
    string a = "";

    do {
        a += (number % 10l) + '0';
        number/=10l;
    } while(number);

    string b = a;
    reverse(a.begin(), a.end());

    return (a == b);
}

void generate(const long long from, const long long to) {
    for(long long i = sqrt(from); i <= sqrt(to); ++i)
        if(ifPolindrome(i) && ifPolindrome(i*i)){
            numbers.push_back(i*i);
            //cout << i*i << endl;
        }
}

int t;

int main() {
    freopen("C-large-1.in", "r", stdin);
   freopen("output.txt", "w", stdout);

    generate(0ll, 100000000000000ll);

    cin >> t;

    for(int i = 0; i < t; ++i) {
        long long a, b;
        int c = 0;

        cin >> a >> b;

        for(vector<long long>::iterator it = numbers.begin(); it != numbers.end(); ++it)
            if(*it >= a && *it <= b)
                ++c;

        printf("Case #%d: %d\n", i+1, c);
    }
}
