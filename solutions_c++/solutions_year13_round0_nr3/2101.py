#include<iostream>
#include<cstdio>
#include<cstring>
#include<map>
#include<vector>
#include<algorithm>
#include<sstream>
#include<cmath>
using namespace std;
int ntest;
int g[12000000];
bool good(int x){
    long long t = 1LL*x*x;
    stringstream ss;
    ss << x;
    string str = ss.str();
    for(int i=0; i<str.length()/2+1; i++){
        if(str[i]!= str[str.length()-1-i]) return false;
    }
    stringstream ss2;
    ss2 << t;
    str = ss2.str();
    for(int i=0; i<str.length()/2+1; i++){
        if(str[i]!= str[str.length()-1-i]) return false;
    }
    //cout << x << " " << str << endl;
    return true;
}
void pre(){
    for(int i=1; i<10000011; i++){
        if(good(i)){
            g[i]=g[i-1]+1;
        }else g[i] = g[i-1];

    }
}
long long a,b;
void solve(int test){
    printf("Case #%d: ",test+1);
    int l = (int) sqrt(a);
    if(1LL*l*l>=a) l--;
    int h = (int) sqrt(b);
    if(1LL*h*h >b) h--;
    cout << g[h]-g[l] << endl;
}
int main(){
    freopen("C-large-1.in","r",stdin);
    freopen("test.out","w",stdout);
    pre();
    scanf("%d\n",&ntest);
    for(int t=0; t<ntest; t++){
        cin>>a>>b;
        solve(t);
    }
    return 0;
}
