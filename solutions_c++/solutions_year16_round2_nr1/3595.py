#include <cstdio>
#include <cstring>
#include <string>
using namespace std;
char s[2222];
int a[222];
string c[11]={"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
bool ok(string p) {
    int b[222]={};
    for ( int i = 0 ; i < (int)p.length() ; i++ ) 
        b[p[i]-'A']++;
    for ( int i = 0 ; i < 26 ; i++ ) 
        if ( a[i] < b[i] ) return false;
    return true;
}
void rm(string p) {
    for ( int i = 0 ; i < (int)p.length() ; i++ ) 
        a[p[i]-'A']--;
}
void add(string p) {
    for ( int i = 0 ; i < (int)p.length() ; i++ ) 
        a[p[i]-'A']++;
}
bool isEnd() {
    for ( int i = 0 ; i < 26 ; i++ ) 
        if ( a[i] > 0 ) return false;
    return true;
}
string ans;
string np="0123456789";
void go(int pos,string ss) {
    if ( isEnd() ) {
        ans = ss;
        return;
    }
    if ( pos >= 10 ) return;
    if ( ok(c[pos]) ) {
        rm(c[pos]);
        go(pos,ss+np[pos]);
        add(c[pos]);
    } 
        go(pos+1,ss);
}
int main() {
    int tc;
    scanf("%d",&tc);
    for ( int _tc = 1 ; _tc <= tc ; _tc++ ) {
        printf("Case #%d: ",_tc);
        scanf("%s",s);
        memset(a,0,sizeof a);
        ans = "";
        for ( int i = 0 ; s[i] ; i++ ) 
            a[s[i]-'A']++;
        go(0,"");
        printf("%s\n",ans.c_str());
    }
    return 0;
}
