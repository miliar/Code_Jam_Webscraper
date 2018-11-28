#include <iostream>
#include <vector>
#include <string>
#include <utility>
#include <algorithm>
#include <cstdio>

using namespace std;

bool ss(string str){
    int size = str.size();
    for(int i=0;i<size/2;i++){
        if(str[i] != str[size-1-i])return false;
    }
    return true;
}

bool s(int i){
    char c[128];
    sprintf(c,"%d",i);
    return ss(string() + c);
}

bool d[1001];

int solve(int l,int h){
    int ans = 0;
    for(int i=l;i<=h;i++){
        if(d[i]){
            //cout << i << endl;
            ans++;
        }
    }
    return ans;
}


void setup(){
    int i=0;
    while(++i*i <= 1000){
        d[i*i] = s(i*i) && s(i);
    }
}

int main(){
    setup();
    int T;
    cin >> T;
    int a;
    int l,h;
    for(int i=1;i<=T;i++){
        cin >> l >> h;
        int s = solve(l,h);
        cout << "Case #" << i << ": " << s << endl;
    }
}
