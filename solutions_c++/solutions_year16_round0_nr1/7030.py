#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <set>
#include <cmath>
#include <stack>

#define ll long long int
#define pll pair<long long, long long>
#define pii pair<int, ll>
#define pb push_back
#define mp make_pair
#define getchar_unlocked getchar
#define F first
#define S second

using namespace std;

int getint();
long long getlint();

int main() {
    set<int> digits;
    int t;
    cin>>t;
    set<int>::iterator it;
    for(int i=1;i<=t;i++) {
        ll n;
        ll j=1;
        cin>>n;
        if(n==0) {
            cout<<"Case #"<<i<<": INSOMNIA\n";
            continue;
        }
        for(int k=0;k<=9;k++) {
            digits.insert(k);
        }
        while(!digits.empty()) {
            ll temp = n*j;
            while(temp) {
                int dig = temp%10;
                temp/=10;
                if((it=digits.find(dig))!=digits.end()) {
                    digits.erase(it);
                }
            }
            if(!digits.empty())
                j++;
        }
        cout<<"Case #"<<i<<": "<<n*j<<"\n";
    }
	return 0;
}

int getint()
{
    int c,num=0;
    while((c=getchar_unlocked())==' ' || c=='\n')
    ;
    int sign;
    if(c=='-'){
        sign=-1;
    }
    else{
        sign=+1;
    }
    if(c=='-' || c=='+'){
        c=getchar_unlocked();
    }
    while(c!=' ' && c!='\n' && c!=EOF){
        num=(num<<1)+(num<<3)+(c-'0');
        c=getchar_unlocked();
    }
    return num*sign;
}

long long int getlint()
{
    int c;
    long long num=0;
    while((c=getchar_unlocked())==' ' || c=='\n')
    ;
    long long int sign;
    if(c=='-'){
        sign=-1;
    }
    else{
        sign=+1;
    }
    if(c=='-' || c=='+'){
        c=getchar_unlocked();
    }
    while(c!=' ' && c!='\n' && c!=EOF){
        num=(num<<1)+(num<<3)+(c-'0');
        c=getchar_unlocked();
    }
    return num*sign;
}
