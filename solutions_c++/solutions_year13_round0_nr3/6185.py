#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <functional>
#include <numeric>
#include <cmath>

using namespace std;

#define vi vector<int>
#define vvi vector<vector<int> >
#define all(e) e.begin(),e.end()
#define pb push_back

long long isPalindrome(long long a) {
    int digits = log10(a)+1;
    string d;
    for(int c=0; c<digits; c++) {
        d += (char)(a%10);
        a /= 10;
    }
    string rd(d);
    reverse(all(d));
    return d == rd;
}

bool isRootPalindrome(long long i) {
    return isPalindrome(i) && isPalindrome(i*i);
}

#define EXPECT_TRUE(x) if(!(x)) { cout << "failed " << #x << endl; }
#define EXPECT_FALSE(x) if(x) { cout << "failed " << #x << endl; }

void test() {
    EXPECT_TRUE( isPalindrome(1) );
    EXPECT_TRUE( isPalindrome(11) );
    EXPECT_TRUE( isPalindrome(66) );
    EXPECT_TRUE( isPalindrome(101) );
    EXPECT_TRUE( isPalindrome(10101) );
    EXPECT_TRUE( isPalindrome(12321) );
    EXPECT_FALSE( isPalindrome(10) );
    EXPECT_FALSE( isPalindrome(122) );
    EXPECT_FALSE( isPalindrome(12323) );
    cout << "tests done" << endl;
}

int main(int argc, const char *argv[]) {
    //test();
    int N;
    cin >> N;
    for(int ca=0; ca<N; ca++) {
        long long A, B, count=0;
        cin >> A >> B;

        for(long long i=ceil(sqrt(A)); i<=sqrt(B); i++) {
            if(isRootPalindrome(i))
                count++;
        }

        cout << "Case #" << (ca+1) << ": " << count << endl;
    }
    return 0;
}

