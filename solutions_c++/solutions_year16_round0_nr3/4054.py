#include <bits/stdc++.h>
using namespace std;

int T;
int N;

int answers = 0;

vector<long long> primes;
bool sieve[1000005];

void pregen(){
    for(int i = 2; i<1000000; i++){
        if (!sieve[i]){
            primes.push_back(i);
            sieve[i] = true;
            for(int j = i+i; j<1000000; j+=i){
                sieve[j] = true;
            }
        }
    }
}

long long str2base(string s, int n){
    long long val = 0;
    long long run = 1;
    while (s.length() > 0){
        if (s[s.length()-1] == '1') val+=run;
        s = s.substr(0,s.length()-1);
        run = run*n;
    }
    return val;
}

void verify(string s){
    int ans[12] = {0};
    bool works = true;
    for(int k = 2; k<=10; k++){
        long long x = str2base(s, k);
        for(int i = 0; i<primes.size(); i++){
            if (primes[i] >= x) break;
            if (x%primes[i]==0){
                ans[k] = primes[i];
                break;
            }
        }
        if (ans[k] == 0) works = false;
    }

    if (works){
        cout << s;
        for(int i = 2; i<=10; i++) cout << " " << ans[i] ;
        cout << endl;
        answers++;
    }

}

void genStr(string s){
    if (answers == 50) return;
    if (s.length()==16) verify(s);
    else{
        if(s.length()<15) genStr(s+'0');
        if (answers == 50) return;
        genStr(s+'1');
        if (answers == 50) return;
    }
}

int main(){
    freopen("output.txt", "w", stdout);
    pregen();
    string s = "1";
    genStr(s);




}
