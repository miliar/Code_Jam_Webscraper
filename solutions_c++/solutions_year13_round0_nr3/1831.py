#include <iostream>
#include <cstdio>
#include <map>
#include <algorithm>
#include <cstring>  //for C++
#include <vector>
#include <cmath>
#include <queue>
#include <set>
#include <map>
#include <sstream>
//#include <string> for C

#define REP(i,n) for(i=0;i<(n);++i)
#define FOR(i,l,h) for(i=(l);i<=(h);++i)
#define FORD(i,h,l) for(i=(h);i>=(l);--i)
#define foreach(itr, cont) for (typeof(cont.begin()) itr = cont.begin(); itr != cont.end(); itr++)

using namespace std;

bool checkpalindrome(long long int num){
    int bits[15];
    int count=0;
    while(num!=0){
        bits[count] = num%10;
        num = num/10;
        count++;
    }
    
    for(int i=0; i<count/2; i++)
        if(bits[i] != bits[count-1-i])
            return false;
    
    return true;
}

bool checksquare(long long int num){
    long double root = sqrt((long double)num);
    if(root - (long long int)root == 0.0)
        return true;
    else
        return false;
}

bool checkAnswer(long long int num, long long int A, long long int B){
    if(checkpalindrome(num)){
        long long int sqrtNum = num*num;
        if(sqrtNum >= A && sqrtNum<=B && checkpalindrome(sqrtNum))
            return true;
    }
    
    return false;
}

int main()
{
    int T, k;
    long long int A, B, i;
    cin>>T;
    REP(k,T){
        cin>>A>>B;
        cout<<"Case #"<<k+1<<": ";
        long long int count = 0;
        long long int start = (long long int)sqrt((long double)A);
        long long int end = (long long int)sqrt((long double)B);
        for(i=start; i<=end; i++){
            if(checkAnswer(i, A, B)){
                count++;
            }
        }
        
        cout<<count<<endl;
    }
}
