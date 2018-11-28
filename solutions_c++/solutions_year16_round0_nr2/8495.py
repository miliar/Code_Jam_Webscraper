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

int T, first, last, i, sz, counter;
string S;

inline int findFirst(){
    int i=0;
    first = S.find_first_of('-');
}

inline int findLast(){
    int i=0,lt;
    if(last>sz) last=sz-1;
    last = S.find_last_of('-', last);
}

inline void flip(int c){
    for(int i=0;i<=c;i++){
        switch(S[i]){
        case '+':
            S[i]='-';
            break;
        case '-':
            S[i]='+';
            break;
        }
    }
    for(int i=0,j=c;i<j;i++,j--){
        swap(S[i],S[j]);
    }
    counter++;
}

int main(){
    ///runtime rt; //Uncomment to calculate runtime.

    cin >> T;
    for(i=0; i<T; i++){
        cin >> S;
        sz = S.size();
        first=INT_MAX;
        last=INT_MAX;
        counter = 0;
        first = findFirst();
        last = findLast();

//        cout<<first<<endl;
//        cout<<last<<endl;
        while(last>-1){
            int tmp = first-1;
            if(tmp>-1)
                flip(tmp);

//            cout << S<<endl;

            if(tmp != last)
                flip(last);

//            cout << S<<endl;
//            cout << counter<<endl;

            first = findFirst();
            last = findLast();

//            cout<<first<<endl;
//            cout<<last<<endl;

        }
        cout << "Case #"<< i+1 <<": "<<counter<<endl;

    }

    return 0;
}
