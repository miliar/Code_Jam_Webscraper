#include<iostream>
#include<set>
#include<string>
#include<cstdio>

using namespace std;

typedef unsigned long long ull;

bool is_palindrome(ull num){
    char buffer[30];
    snprintf(buffer, 30, "%llu", num);
    string s = string(buffer);
    
    int b = 0, e = s.size()-1;
    bool ok = true;
    while (b<e){
        if (s[b++]!=s[e--]){
            ok = false;
            break;
        }
    }
    return ok;
}


int main(void){
    set<ull> pals;
    for(int i=1;i<1e7;++i){
        if (is_palindrome(i)){
            ull x=i*i;
            if (is_palindrome(x)) {
                pals.insert(x);
                //cout<<x<<endl;
            }
        }
    }
    pals.insert(1e15);
    
    int T;
    cin>>T;
    for(int tcase = 1; tcase <= T; ++tcase){
        ull A,B;
        cin>>A>>B;
        auto a = pals.lower_bound(A);
        auto b = pals.lower_bound(B);
        while (*a<A) ++a;
        while (*b<=B) ++b;
        //cout<<*a<<" "<<*b<<endl;
        ull res = distance(a, b);
        cout<<"Case #"<<tcase<<": "<<res<<endl;
    }
}
