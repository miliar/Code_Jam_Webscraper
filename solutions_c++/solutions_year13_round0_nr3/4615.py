#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <utility>
#include <sstream>
#include <iomanip>
#include <list>

using namespace std;
#define deb(a) cout<<#a<<":"<<a<<endl;

long long isSquare(long long n) {
    for(long long i=1; (i*i)<=n; i++) {
        if((i*i) == n) {return i;}
    }
    return 0;
}

bool isPalindrome(long long n) {
    stringstream ss1, ss2;
    
    ss1<<n;
    ss2<<n;
    
    string str1, str2;
    
    ss1>>str1;
    ss2>>str2;
    
    reverse(str2.begin(), str2.end());
    
    if(str1!=str2) {return false;}
    return true;
}

bool check(long long n) {
    if(!isPalindrome(n)) {return false;}

    long long sq = isSquare(n);
    if(!sq) {return false;}
    
    if(!isPalindrome(sq)) {return false;}
    
    return true;
}

int main() {
    string ln;
    int T;
    
    cin>>T;
    getline(cin, ln);
    
    for(int t=1; t<=T; t++) {
        long long a, b;
        cin>>a>>b;
        
        int res = 0;
        
        for(long long k=a; k<=b; k++) {
            if(check(k)) {res++;}
        }
        
        cout<<"Case #"<<t<<": "<<res<<endl;
    }
    
    return 0;
}