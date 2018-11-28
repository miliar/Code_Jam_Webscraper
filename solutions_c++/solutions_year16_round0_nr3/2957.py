#include<iostream>
#include<set>
#include<queue>
#include<bitset>
#include<assert.h>
using namespace std;


#define LEN 16
#define LEN2 32
string getNext(int len, int index) {
    string ans;
    ans += to_string(1);
    if (len == 16)
        ans += bitset<LEN-2>(index).to_string();
    else
        ans += bitset<LEN2-2>(index).to_string();
    
    ans += to_string(1);
    return ans;
}

long long unsigned getValue(string input, int base) {
    long long unsigned ans = 0;
    long long unsigned mul = 1;
    for (int i = 0; i < input.length(); i++) {
        if(input[input.length()-1-i] == '1')
            ans += mul;
        mul *= base;
    }
    return ans;
}

bool isPrime(long long unsigned number, long long unsigned & f) {
    if(number < 2) return false;
    if(number == 2) return true; 
    if(number % 2 == 0) {f = 2; return false;}
    for(long long unsigned i=3; (i*i * i)<=number; i+=2){
        if(number % i == 0 ) { f = i; return false;}
    }
    return true;
}

bool isChoice(string input, vector<int>& factors) {
    for (int i = 2; i <= 10; i++) {
        long long unsigned val = getValue(input, i);
        //cout << "D" <<val <<endl;
        long long unsigned f = 0;
        if (isPrime(val, f)) 
            return false;
        else
            factors.push_back(f);
    }
    return true;
}

void getResults(int n, int j) {
    int count = 0;    
    for (int i = 0; i < 50000; i+=1) {
        string candidate = getNext(n, i);
        vector<int> factors;
        int x = 2;
        if (isChoice(candidate, factors)) {
            cout << candidate; 
            for (int v : factors) {
                cout << " " << v;
                assert(getValue(candidate,x++) % v == 0);
            }
            cout<< endl;
            count++;
        }    
        if (count == j)
            return;
    } 
    cout << "Error" << endl;
}
int main() {

   int numCase = 1000000;
    cin >> numCase; 
    for (int i = 0; i < numCase; i++) {
        int N, J;
        cin >> N;
        cin >> J;
        cout <<"Case #"<<(i+1)<<":"<<endl;
        getResults(N, J);
    }
}
