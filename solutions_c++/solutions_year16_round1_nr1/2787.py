#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <set>
#include <cmath>
#include <string>

#define ll long long int
#define pll pair<long long, long long>
#define pii pair<int, int>
#define pb push_back
#define mp make_pair
#define getchar_unlocked getchar

using namespace std;

int getint();
long long getlint();

int main() {
    string s;
    int t;
    cin>>t;
    for(int j =1; j<=t;j++) {
        cin>>s;
        string a="";
        int sz = (int) s.size();
        for(int i=0;i<sz;i++) {
            if(a.size()==0) {
                a+=s[0];
            }
            else if(s[i]<a[0]) {
                a+=s[i];
            }
            else {
                a=s[i]+a;
            }
        }
        cout<<"Case #"<<j<<": "<<a<<"\n";
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
