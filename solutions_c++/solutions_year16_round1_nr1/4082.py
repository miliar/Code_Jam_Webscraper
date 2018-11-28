/**
@author A B M Ruman
*/
#include<stack>
#include<queue>
#include<cmath>
#include<ctime>
#include<cstdio>
#include<cstring>
#include<string>
#include<sstream>
#include<cstdlib>
#include<climits>
#include<algorithm>
#include<vector>
#include<iostream>
using namespace std;

#define REG register
#define PI 2*acos(0.0)
#define ABS(a) (a<0)?-a:a
#define MAX(a,b) (a>b)?a:b
#define MIN(a,b) (a<b)?a:b

typedef int I;
typedef long L;
typedef float F;
typedef double D;
typedef long long LL;
typedef long double LD;
typedef unsigned int UI;
typedef unsigned long UL;
typedef unsigned long long ULL;

class runtime{
    int start_s;
public:
    runtime(){ start_s=clock();}
    ~runtime(){
        fprintf(stderr,"<time: %f>", double ((clock()-start_s)/double(CLOCKS_PER_SEC)));
    }
};

///factorial genarator
/*
#define FACT_MAX 1001
//#define MOD 100009
long long fact[FACT_MAX];
inline void factGen(){
    //fact = new X[FACT_MAX];
    fact[0]=fact[1]=1;
    int c, f;
    for(c = 2; c < FACT_MAX; c++)
        fact[c] = (fact[c-1] * c); //%MOD;
}
*/
///First 29 fibbonacii numbers
/*
#define FIB_MAX 29
const int fib[] = { 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811 };
*/

//template <class X>
//inline void swap(X *a,X *b){ X c; c=*a; *a=*b; *b=c; }
template <class X>
inline X sqr(X a){ return a*a; }

int main(){
    ///runtime rt; //Uncomment to calculate runtime.
    int T;
    string S, O;
    cin >> T;
    for(int i=1; i<=T; i++){
        cin >> S;
        O = S[0];
        //cout << O << endl;
        for(int j=1; j<S.size(); j++){
            if(O[0]>S[j])
                O = O + S[j];
            else
                O = S[j] + O;

        }
        cout << "Case #"<< i <<": ";
        cout << O << endl;
    }
    return 0;
}
