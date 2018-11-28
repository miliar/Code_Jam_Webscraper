#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

long long int isPrime(long long int n){

    for(long long int i = 3; i*i < n; i += 2){
        if(n % i == 0)
            return i;
    }
    return -1;
}
bool checkJamcoin(string s){
    vector<long long int> dividers;
    for(int i = 2; i <= 10; ++i){
        long long int  num = 0;
        long long int multiplyer = 1;
        for(int j = s.size() - 1; j >= 0; --j){
            if(s[j] == '1'){
                num += multiplyer;
            }
            multiplyer *= i;
        }
        long long int divider = isPrime(num);
        if(divider < 0)
            return false;
        dividers.push_back(divider);
    }

    cout<<s;
    for(auto &i : dividers){
        cout<<" "<<i;
    }
    cout<<endl;
    return true;
}

string toString(int n, int N){

    string s;
    while(n != 0){
        N--;
        if(n & 1)
            s.insert(0,"1");
        else
            s.insert(0,"0");
        n = n>>1;
    }

    for(int i = 0; i < N; ++i)
        s.insert(0,"0");

    return s;
}

void generateNum(int N, int J){

int num = 1;

for(int i = 0 ; i < N - 3; ++i){
        num *= 2;
        num += 1;
    }

    for(int i = 0; i <= num; ++i){
        string s("1");
        s.append(toString(i, N - 2));
        s.append("1");
        if(checkJamcoin(s))
            J--;
        if(J <= 0)
            return;
    }
}



int main(){

int num = 0;

cin>>num;
printf("Case #1:\n");
for(int i = 0 ; i < num ;++i){
    int N,J;
    cin>>N>>J;
    generateNum(N,J);
}

return 0;
}
