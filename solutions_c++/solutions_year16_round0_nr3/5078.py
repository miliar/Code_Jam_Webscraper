//
//  main.cpp
//  CountingSheep
//
//  Created by TT on 09/04/2016.
//  Copyright © 2016 TT. All rights reserved.
//

#include <iostream>
#include <string>
#include <queue>
#include <unordered_set>

using namespace std;

typedef long long ull;

int *a;
int N, J;
unordered_set<string> seen;

bool isPrime(ull n) {
    if(n < 2) return false;
    if(n == 2 || n == 3) return true;
    if(n%2 == 0 || n%3 == 0) return false;
    ull sqrtN = (ull)sqrt(n)+1;
    for(long i = 6L; i <= sqrtN; i += 6) {
        if(n%(i-1) == 0 || n%(i+1) == 0) return false;
    }
    return true;
}

long interpret(int base){
    ull factor = base;
    ull total = 0;
    
    for (int i = N - 2 - 1; i>=0; --i)
    {
        total += (a[i] * factor);
        factor *= base;
    }
    
    return total + factor + 1;
    
}

ull trivial(ull n){
    if (n % 2 == 0){
        return 2;
    }
    for (int i=3; i<n; i+= 2){
        if (n % i == 0){
            return i;
        }
    }
    return 0;
}

void process(){
    vector<ull> vec;
    for (int i=2; i<=10; ++i){
        ull s = interpret(i);
        if (isPrime(s)){
            return;
        }
        vec.push_back(s);
    }
    
    string s = "";
    for (int i=0; i<N - 2; ++i){
        s += ('0' + a[i]);
    }
    
    if (seen.find(s) != seen.end()){
        return;
    }
    
    seen.insert(s);
    J--;
    cout << "1";
    for (int i=0; i< N - 2; ++i){
        cout << a[i];
    }
    cout << "1";
    
    for (int i=0; i<vec.size(); ++i){
        cout << " " << trivial(vec[i]);
    }
    cout << endl;
}

void enumerate(int n)
{
    if (J == 0){
        return;
    }
    
    if (n == N)
    {
        process();
        return;
    }
    enumerate(n+1);
    a[n] = 1;
    enumerate(n+1);
    a[n] = 0;
}




void fMain(int t){
    cin >> N >> J;
    a = new int[N - 2];
    memset(a, 0, N - 2);
    
    cout << "Case #" << t << ": 1" << endl;
    
    enumerate(0);
}




int main(int argc, const char * argv[]) {
    int T;
    cin >> T;
    for (int t = 1; t <=T; ++t){
        fMain(t);
    }
    return 0;
}
