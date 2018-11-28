#include <iostream>
#include <cstring>
#include <cmath>
#include <cstdio>
#include <cctype>
#include <algorithm>
#include <map>
#include <set>
#include <stack>
#include <queue>


using namespace std;

#define all(x) x.begin(),x.end()
// sort(all(vec))
#define present(container, element) (container.find(element) != container.end())
#define cpresent(container, element) (find(all(container),element) != container.end())
#define tr(container, it) for(typeof(container.begin()) it=container.begin();it!=container.end();it++)
// tr(set,it)
// total+=it->second;

string totwo(long long x){
    string s;
    while(x>0){
        s+='0'+x%2;
        x/=2;
    }
    reverse(s.begin(),s.end());
    return s;
}

long long change(string s,int k){
    long long x=0;
    for(int i=0;i<s.length();i++){
        x=x*k+(s[i]-'0');
    }
    return x;
}

int main(){
    int t;
    cin >> t;
    int hhh=1;
    while(t--){
        
        int k,c,s;
        cin >> k >> c >> s;
        cout << "Case #" << hhh++ << ":";
        for(int i=1;i<=k;i++)
            cout << " " << i ;
        cout << endl;
    }
}