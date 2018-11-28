#include <iostream>
#include <vector>
#include <unordered_set>
#include <unordered_map>
#include <stack>
#include <queue>
#include <string>
#include <fstream>
#include <sstream>
#include <algorithm>
using namespace std;

vector<int> primes;
void find_primes(int max_p){
    primes.push_back(2);
    int j;
    for(int i=3;i<max_p;i+=2){
        j=0;
        while(primes[j]*primes[j]<=i && i%primes[j]!=0)j++;
        if (primes[j]*primes[j]>i) primes.push_back(i);
    }
}

int main(){
    find_primes(1000000);
    printf("Case 1: \n");
	int T; cin>>T;
    int N, J; cin>>N>>J;
    int d[N] = {};
    int count=0;
    d[0] = 1; d[N-1]=1;
    while(count<J){
        bool flag = 1;
        int base = 2;
        int factors[9];
        long long num;
        while(base<=10){
            num = 0;
            long long b = 1;
            for(int i=0;i<N;i++) {num+= b*d[N-1-i]; b*=base;}
            int j = 0;
            while(j<primes.size() && num%primes[j]!=0 && primes[j]*primes[j]<=num) j++;
            if (j==primes.size() || num%primes[j]!=0) break;
            factors[base-2] = primes[j];
            base++;
        }
        if (base>10){
            for(int i=0;i<N;i++) cout<<d[i]; cout<<' ';
            for(int i=0;i<base-2;i++) cout<<factors[i]<<' '; cout<<endl;
            count++;
        }
        int i=N-2;
        while(d[i]==1) {d[i] = 0; i--;}
        d[i] = 1;
    }
	
}