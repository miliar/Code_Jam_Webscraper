#include<iostream>
#include<bitset>
#include<cmath>
#include<cstring>
#define MAX 1000000
#define NPRIME 78498
using namespace std;

unsigned long long primes[NPRIME];
unsigned long long numLine[MAX];

void sieve() {
    long long i, j=0, k;
    int step=0;
    primes[j++]=2; primes[j++]=3;

    for(i=5; i<MAX;) {
        if(numLine[i]==0) {
            primes[j++]=i;
            for(k=2; i*k<MAX; k++)
                numLine[i*k]=1;
        }
        // little quicker jumps
        if(step%2) {i+=4; step=0;}
        else {i+=2; step++;}
    }
    //printf("%lld %lld\n", j, primes[NPRIME-1]);
}

int isPrime(unsigned long long n) {
    long long i;
    for(i=0; primes[i]*primes[i] < n &&  i<NPRIME; i++) {
        //printf("checking for %lld\n", primes[i]);
        if(n%primes[i] == 0) return primes[i];
    }
    return 1;
}

int main() {
    sieve();
/*  cout<<isPrime(337)<<"\n";
    string bin = bitset<4>(13).to_string();
    cout<<bin<<'\n';
    cout<<stol("110111", nullptr, 3); 
    string bin2 = bitset<14>(0).to_string();
    cout<<bin2<<'\n'; */

    int t, j, n, i;
    int count;
    unsigned int loopn;
    long long candidate, flag; 
    const int maxN = 65535; //maxN = pow(2, n) - 1;
    const int maxDigits = 14;
    string bin , newn;
    //cin>>t;
    //cin>>n>>j;
    n=16; j=50;
    //maxDigits = n-2;
    //cout<<maxN;
    count=0;
    loopn = 0;
    
//   /*
 while(count < j) {
//        cout<<"checking for "<<loopn<<"\n";
        bin = bitset<14>(loopn).to_string();
        newn = '1' + bin + '1';
//        cout<<"checking if prime in all bases for "<< newn <<'\n';
        flag=0;
        for(i=2; i<11; i++) {
            candidate = stoll(newn, nullptr, i);
            if(isPrime(candidate) == 1) { flag=1; break; }
        }
        if(flag == 0) { // got a number
            count++;

            // now print all its non trivial divisor in base 2 to k
            cout<<newn<<" ";
            for(i=2; i<11; i++) {
                candidate = stoll(newn, nullptr, i);
                cout<< isPrime(candidate) << " ";

            }

            cout<<'\n';

        }
        

        loopn++;
    }
//*/

    return 0;
}
