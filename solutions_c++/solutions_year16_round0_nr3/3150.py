#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

#define NN 100005LL

using namespace std;

int8_t *bs;
vector<int> primes;

void sieve() {
    bs[0] = bs[1] = 0;
    for(long long int i = 2LL; i <= NN; i++) if(bs[i]) {
        for(long long int j = i*i; j <= NN; j += i) bs[j] = 0;
        primes.push_back((int)i);
    }
}

bool isPrime(long long int N) {
    if(N <= NN) return bs[N];
    for(int i = 0; i < (int)primes.size(); i++)
        if(N % primes[i] == 0) return false;
    return true;
}

long long int pow(int base, int exp) {
    long long int ans = 1LL;
    for(int i = 0; i < exp; ++i)
        ans *= base;
    return ans;
}

long long int toBase(string S, int base) {
    long long int ans = 0;
    int sz = (int)S.size();
    string uno = "1";
    for(int i = sz-1; i >= 0; i--)
        if(string(1,S[i]) == uno)
            ans += pow(base,sz-i-1);
    return ans;
}

int findDivisor(long long int num) {
    // num is guaranteed to not be prime :)
    for(int i = 0; i < (int)primes.size(); ++i)
        if(num%primes[i] == 0) return primes[i];
    return 2;
}

int main() {
cout << "Case #1:\n";

bs = (int8_t *)malloc(sizeof(int8_t)*NN);
for(int i = 0; i < NN; ++i) bs[i] = 1;
sieve();

int T;
cin >> T;
int N,J;
for(int kase = 1; kase <= T; ++kase) {
    int found = 0;
    vector<string> process;
    cin >> N >> J;
    for(int ones = 0; ones < N-1; ++ones) {
        string S = "";
        for(int i = 0; i < ones; ++i)
            S += "1";
        while((int)S.size() < N-2)
            S += "0";
        sort(S.begin(),S.end());
        //cout << S << endl;
        do {
            if(found>=J) break;
            bool flag = true;
            for(int base = 2; base <= 10; ++base) {
                if(isPrime(toBase("1"+S+"1",base))) {
                    flag = false;
                    //cout << "1" + S + "1" << endl;
                    //cout << "S: " << toBase("1"+S+"1",base) << " base: " << base << endl;
                }
            }
            //cout << "1"+S+"1" << endl;;
            if(flag) {
                found+=1;
                process.push_back("1"+S+"1");
            }
        } while(next_permutation(S.begin(),S.end()));
        //cout << "~~~~~" << endl;
    }
    for(int i = 0; i < (int)process.size(); ++i) {
        cout << process[i];
        for(int base = 2; base <= 10; ++base)
            cout << " " << findDivisor(toBase(process[i],base));
        cout << endl;
    }
}
/*
    cout << ":o " << endl;
    for(int base = 2; base <= 10; ++base) {
        cout << toBase("110011", base) << " base: " << base << endl;
        if(isPrime(toBase("110011",base))) cout << base << endl;
    }
*/
    return 0;
}
