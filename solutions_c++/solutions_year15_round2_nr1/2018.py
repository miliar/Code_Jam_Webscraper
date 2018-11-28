#include <iostream>
#include <cstdio>
#include <stack>
#include <vector>
#include <math.h>

using namespace std;

typedef unsigned long long ull;
ull T,N,ans;

ull power(ull base, int exp){
    if (exp == 0) return 1;
    if (exp%2 == 0) return power(base*base,exp/2);
    else return base*power(base*base,exp/2);
}

ull reduce(ull num){
    vector<ull> dig;
    while(num > 0){
        dig.push_back(num%10);
        num/=10;
    }
    int lim = dig.size()/2;
    ull r = 1;
    if (dig.size()%2 == 1) lim++;
    for (int i = 0; i < lim; i++){
        if (i == 0){
            ans += dig[i]-1;
        }
        else ans += dig[i]*power(10LL,i);
    }
    for (int i = lim; i < dig.size(); i++){
        r += dig[i]*power(10LL,i);
    }
    return r;
}

ull flip(ull num){
    stack<ull> dig;
    while(num > 0){
        dig.push(num%10);
        num/=10;
    }
    int len = 0;
    ull f = 0;
    while(!dig.empty()){
        f += dig.top()*power(10LL,len);
        dig.pop();
        len++;
    }
    return f;
}

int main()
{
    freopen("cj15r1bp1small.in","r",stdin);
    freopen("cj15r1bp1small.out","w",stdout);
    cin >> T;
    for (int z = 1; z <= T; z++){
        ans = 0;
        cin >> N;
        for (ull i = N; i > 0;i--){
            if (i <= 10){
                ans += i; break;
            }
            if (i % 10 != 0){
                i = reduce(i);
                int f = flip(i);
                if (i != f){
                    ans++;
                    i = reduce(f);
                }
            }
            ans++;
        }
        cout << "Case #" << z << ": " << ans << endl;
    }
    return 0;
}

