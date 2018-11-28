#include <iostream>
#include <string>
#include <vector>
#include <unordered_set>
#include <cstdio>
#include <cmath>

using namespace std;

void str_to_double(unsigned long num, int base, unsigned long long & high, unsigned long long & low, unsigned long long & factor){
    unsigned long long res_tmp=0;
    factor=1;
    for(int i=0; i<16; ++i){
        res_tmp+=num%2*factor;
        factor*=base;
        num>>=1;
    }
    low=res_tmp;

    factor=1;
    res_tmp=0;
    for(int i=0; i<16; ++i){
        res_tmp+=num%2*factor;
        factor*=base;
        num>>=1;
    }
    high=res_tmp;
}

string num2str(int N, unsigned long num){
    string s(N,'0');
    for(int i=N-1; i>=0; --i){
        s[i]='0'+num%2;
        num>>=1;
    }
    return s;
}

bool isprime(const unsigned long long & high, const unsigned long long & low,
             const unsigned long long & f, int & factor, const vector<int>& primes){
    unsigned long long upper=sqrt(high+1)*1.0E8;
    for(int i=0; i<primes.size(); ++i){
        if((low%primes[i]+(high%primes[i])*(f%primes[i])%primes[i])%primes[i]==0){
            factor=primes[i];
            return false;
        }
    }
    return true;
}

void get_primes(vector<int>& res, int upper){
    vector<bool> primes(upper+1,true);
    double upper_s=sqrt(upper);
    for(int i=2; i<=upper_s; ++i){
        if(primes[i]){
            for(int j=i; j*i<=upper; ++j) primes[j*i]=false;
        }
    }
    for(int i=2; i<=upper; ++i){
        if(primes[i]) res.push_back(i);
    }
}

int main()
{
    //freopen("D://B-large.in", "r", stdin);
    freopen("D://C-small-attempt0.out", "w", stdout);
    int N, J;
    N=32;
    J=500;
    //cin>>N>>J;

    unsigned long num=(1<<(N-1))-1;
    int counter=0;
    cout << "Case #1:"<<endl;
    vector<int> primes;
    get_primes(primes,1.0E6);


	while(counter<J){
	    num+=2;
        //cout << num2str(N,num)<<endl;
        vector<int> factors(9,0);
        int j=2;
        for(; j<=10; ++j){
            unsigned long long high, low, f;
            str_to_double(num, j, high, low, f);
            if(isprime(high,low,f,factors[j-2],primes)) break;
        }
        if(j>10){
            counter++;
            cout << num2str(N,num);
            for(int j=2; j<=10; ++j){
                cout<<' '<<factors[j-2];
            }
            cout << endl;
        }
	}
    return 0;
}
