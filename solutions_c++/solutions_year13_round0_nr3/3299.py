#include<iostream>
#include<vector>
#include <gmp.h>	
#include <gmpxx.h>
using namespace std;
typedef long long LL;


void solve(int testcase){
    mpz_t one; mpz_init_set_ui(one,1);
    string As,Bs; cin >> As >> Bs;
    mpz_t A,B;
    mpz_init_set_str(A,As.c_str(),10);
    mpz_init_set_str(B,Bs.c_str(),10);
    mpz_t sqA, sqB, rem;
    mpz_init(sqA);
    mpz_init(sqB);
    mpz_init(rem);
    mpz_sqrtrem(sqA,rem,A);
    if(mpz_cmp_si(rem,0)>0){
        mpz_add(sqA,sqA,one);
    }
    mpz_sqrtrem(sqB,rem,B);
    mpz_t i; mpz_init_set(i,sqA);
    mpz_t counter; mpz_init(counter);
    while(mpz_cmp(i,sqB)<=0){
        mpz_class foo(i);
        string checkpal = foo.get_str();
        bool ispal = true;
        for(int ii=0, j=checkpal.size()-1; ii<j; ii++, j--){
            if(checkpal[ii]!=checkpal[j]){
                ispal = false;
                break;
            }
        }
        if(ispal){
            mpz_t prod; mpz_init(prod);
            mpz_mul(prod,i,i);
            mpz_class bar(prod);
            checkpal = bar.get_str();
            bool ispal = true;
            for(int ii=0, j=checkpal.size()-1; ii<j; ii++, j--){
                if(checkpal[ii]!=checkpal[j]){
                    ispal = false;
                    break;
                }
            }
            if(ispal){
                mpz_add(counter,counter,one);
            }
        }
        mpz_add(i,i,one);
    }
    mpz_class wat(counter);
    string result = wat.get_str();
    cout << "Case #" << testcase << ": " << result << "\n";
}

int main(){
    int T; cin >> T;
    for(int i=0; i<T; ++i){
        solve(i+1);
    }
    return 0;
}
