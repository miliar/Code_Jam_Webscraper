#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <cstdlib>
#include <algorithm>
using namespace std;
int memo[26];
bool getnum(string str){
    bool ok=1;
    for (int i=0;i<str.size();++i){
        if (memo[str[i]-'A']<=0) ok=0;
    }
    return ok;
}
void solve(){
    printf(" ");
    memset(memo,0,sizeof(memo));
    string str;
    cin >> str;
    for (int i=0;i<str.size();++i) memo[str[i]-'A']++;
    
    string ret,num;
    
    num="ZERO";
    while (memo['Z'-'A']>0){
        ret+='0';
        for (int i=0;i<num.size();++i) memo[num[i]-'A']--;
    }
    num="TWO";
    while (memo['W'-'A']>0){
        ret+='2';
        for (int i=0;i<num.size();++i) memo[num[i]-'A']--;
    }
    num="FOUR";
    while (memo['U'-'A']>0){
        ret+='4';
        for (int i=0;i<num.size();++i) memo[num[i]-'A']--;
    }
    num="SIX";
    while (memo['X'-'A']>0){
        ret+='6';
        for (int i=0;i<num.size();++i) memo[num[i]-'A']--;
    }
    num="EIGHT";
    while (memo['G'-'A']>0){
        ret+='8';
        for (int i=0;i<num.size();++i) memo[num[i]-'A']--;
    }    
    num="ONE";
    while (memo['O'-'A']>0){
        ret+='1';
        for (int i=0;i<num.size();++i) memo[num[i]-'A']--;
    }
    num="THREE";
    while (memo['T'-'A']>0){
        ret+='3';
        for (int i=0;i<num.size();++i) memo[num[i]-'A']--;
    }
    num="FIVE";
    while (memo['F'-'A']>0){
        ret+='5';
        for (int i=0;i<num.size();++i) memo[num[i]-'A']--;
    }
    num="SEVEN";
    while (memo['S'-'A']>0){
        ret+='7';
        for (int i=0;i<num.size();++i) memo[num[i]-'A']--;
    }
    num="NINE";
    while (memo['I'-'A']>0){
        ret+='9';
        for (int i=0;i<num.size();++i) memo[num[i]-'A']--;
    }
    sort(ret.begin(),ret.end());
    cout << ret << endl;
}

int main(){
    int ntest;
    scanf("%d",&ntest);
    for (int test=1;test<=ntest;++test){
        printf("Case #%d:",test);
        solve();
    }
    return 0;
}
