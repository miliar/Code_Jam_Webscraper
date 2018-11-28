//
//  main.cpp
//  Coin Jam
//
//  Created by VIVEK GANGWAR on 09/04/16.
//  Copyright © 2016 VIVEK GANGWAR. All rights reserved.
//
#include <iostream>
#include <cstdio>
#include <climits>
#include <cstdlib>
#include <algorithm>
#include <queue>
#include <cstring>
#include <cmath>
#include <vector>
#include <list>
#include <stack>
#include <bitset>
#include <string>
#include <stack>
#include <set>
#include <map>
#include <assert.h>
#include <deque>
#include <ctime>

#define ALL(i,n)    for(i = 0; i < (n); i++)
#define FOR(i,a,b)  for(i = (a); i < (b); i++)
#define SET(p)      memset(p,-1,sizeof(p))
#define CLR(p)      memset(p,0,sizeof(p))
#define S(n)	    scanf("%d",&n)
#define P(n)	    printf("%d\n",n)
#define Sl(n)	    scanf("%lld",&n)
#define Pl(n)	    printf("%lld\n",n)
#define Sf(n)       scanf("%lf",&n)
#define Ss(n)       scanf("%s",n)
#define LL long long
#define ULL unsigned long long
#define pb push_back
using namespace std;
string arr[40000];
bool prime[100000009];
//primality check miller_rabin
ULL mulmod(ULL a, ULL b, ULL c){
    ULL x = 0,y = a%c;
    
    while(b>0){
        if(b&1) x = (x+y)%c;
        y = (y<<1)%c;
        b >>= 1;
    }
    return x;
}
ULL pow(ULL a, ULL b, ULL c){
    ULL x = 1, y = a;
    
    while(b>0){
        if(b&1) x = mulmod(x,y,c);
        y = mulmod(y,y,c);
        b >>= 1;
    }
    
    return x;
}

bool miller_rabin(ULL p, int it){
    if(p<2) return false;
    if(p==2) return true;
    if((p&1)==0) return false;
    
    ULL s = p-1;
    while(s%2==0) s >>= 1;
    
    while(it--){
        ULL a = rand()%(p-1)+1,temp = s;
        ULL mod = pow(a,temp,p);
        
        if(mod==-1 || mod==1)
            continue;
        
        while(temp!=p-1 && mod!=p-1){
            mod = mulmod(mod,mod,p);
            temp <<= 1;
        }
        
        if(mod!=p-1) return false;
    }
    
    return true;
}
LL convertbase(string s,int base)
{
    LL num = 0;
    for (ULL i = 0 ; i <= s.size() - 1; i++) {
        num += int(s[i]-'0')*pow(base, s.size()-1-i);
    }
    return num;
}
LL convertstrtoint(string s)
{
    LL sum = 0,i=0;
    while(s[i]!='\0'){
        sum = sum*10 + (s[i] - 48);
        i++;
    }
    return sum;
}
LL find_divisor(LL n)
{
    for (LL i = 2; i < n; i++) {
        if(n%i == 0)
            return i;
    }
    return -1;
}
void binarynumbers(int n ,int n1 ,int k)
{
    queue<string> numbers;
    numbers.push("1");
    while (n--)
    {
        string s1 = numbers.front();
        numbers.pop();
        string s2 = s1;
        numbers.push(s1.append("0"));
        numbers.push(s2.append("1"));
        //cout << s2 << " "<< convertstrtoint(s2) << "\n";
        if(s2.size() == n1 && miller_rabin(convertstrtoint(s2),18) != 1 && miller_rabin(convertbase(s2, 2),18)!=1  && miller_rabin(convertbase(s2, 3),18)!=1  && miller_rabin(convertbase(s2, 4),18)!=1  && miller_rabin(convertbase(s2, 5),18)!=1  && miller_rabin(convertbase(s2, 6),18)!=1  && miller_rabin(convertbase(s2, 7),18)!=1  && miller_rabin(convertbase(s2, 8),18)!=1  && miller_rabin(convertbase(s2, 9),18)!=1)// && k != 0)
        {   cout << s2 << " " << find_divisor(convertbase(s2, 2))  << " " << find_divisor(convertbase(s2, 3))  << " " << find_divisor(convertbase(s2, 4))  << " " << find_divisor(convertbase(s2, 5))  << " " << find_divisor(convertbase(s2, 6))  << " " << find_divisor(convertbase(s2, 7))  << " " << find_divisor(convertbase(s2, 8))  << " " << find_divisor(convertbase(s2, 9))  << " " << find_divisor(convertbase(s2, 10)) << endl;
            k--;
        }
        if (k == 0) {
            break;
        }
    }
}

int main(int argc, const char * argv[]) {
    int test;
    cin >> test;
    for (int i = 1; i <= test; i++) {
        int n,j;
        cin >> n >> j;
        cout <<"Case #" << test <<":\n";
        binarynumbers(100000,n ,j);
    }
    return 0;
}
