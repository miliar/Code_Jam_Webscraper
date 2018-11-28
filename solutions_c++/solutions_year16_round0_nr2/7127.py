#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <set>
#include <cmath>
#include <string>

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
    int testcase;
    cin>>testcase;
    for(int t = 1; t<=testcase; t++) {
        string s;
        cin>>s;
        int len = (int) s.size();
        ll count = 0;
        for(int i = len - 1;i>=0;i--) {
            if(s[i]=='-') {
                while(s[i]=='-' && i>=0)
                    i--;
                count+=2;
            }
        }
        if(s[0]=='-')
            count--;
        cout<<"Case #"<<t<<": "<<count<<"\n";
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
