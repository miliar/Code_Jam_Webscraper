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

bool checkpalindrome(int num){
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

bool checksquare(int num){
    float root = sqrt(num);
    if(root - (int)root == 0.0)
        return true;
    else
        return false;
}

bool checkAnswer(int num){
    if(checkpalindrome(num) && checksquare(num))
        if(checkpalindrome((int)sqrt(num)))
            return true;
    
    return false;
}

int main()
{
    int T, A, B, i, k;
    cin>>T;
    REP(k,T){
        cin>>A>>B;
        cout<<"Case #"<<k+1<<": ";
        int count=0;
        FOR(i,A,B){
            if(checkAnswer(i)){
                count++;
            }
        }
        
        cout<<count<<endl;
    }
}
