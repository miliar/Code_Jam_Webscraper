#include <iostream>
#include <vector>
#include <math.h>
#include <set>
using namespace std;
set<int> smallPrimes={2,3,5,7,11};
long long transform(long long num, int from, int to){
    long long res = 0;
    int digit = 0;
    while(num>0){
        res += (num%from) * pow(to, digit);
        num = num/from;
        digit ++;
    }
    return res;
}
bool isPrime(long long num, vector<int>& divisors){
    if(num<65536){
        if(smallPrimes.find((int)num)!=smallPrimes.end()){
            return true;
        }else{
            long long sqrti = sqrt(num);
            for(auto sprime:smallPrimes){
                if(sprime>sqrti)break;
                if(num%sprime==0){
                    divisors.push_back(sprime);
                    break;
                }
            }
            return false;
        }
    }else{
        long long sqrti = sqrt(num);
        for(auto sprime:smallPrimes){
            if(sprime>sqrti)break;
            if(num%sprime==0){
                divisors.push_back(sprime);
                return false;
            }
        }
        return true;
    }
}
int main(int argc, const char * argv[]) {
    int t;
    cin >> t;
    int upbound = 1<<16;
    for(int i=13; i<upbound; i+=2){
        int sqrti = sqrt(i);
        bool isPrime = true;
        for(auto num:smallPrimes){
            if(num>sqrti)break;
            if(i%num==0){
                isPrime = false;
                break;
            }
        }
        if(isPrime)smallPrimes.insert(i);
    }
    for(int i=0;i<t;i++){
        int n,j;
        cin >> n >> j;
        cout << "Case #" << i+1 << ":" << endl;
        long long upbound = 1;
        upbound = (upbound<<n)-1;
        for(long long num = upbound/2+2; num<=upbound; num+=2){
            vector<int> divisors;
            if(isPrime(num, divisors))continue;
            bool jam=true;
            for(int k=3;k<=10;k++){
                long long res = transform(num, 2, k);
                if(isPrime(res, divisors)){
                    jam=false;
                    break;
                }
            }
            if(jam){
                long long div = 1;
                div = div<<(n-1);
                long long num2 = num;
                while(div>0){
                    cout << num2/div;
                    
                    num2=num2%div;
                    div/=2;
                }
                for(int divisor:divisors){
                    cout << ' ' << divisor;
                }
                cout << endl;
                j--;
                if(j==0)break;
            }
        }
    }
    return 0;
}
