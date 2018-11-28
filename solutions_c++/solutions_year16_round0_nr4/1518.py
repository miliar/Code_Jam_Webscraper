#include <bits/stdc++.h>
using namespace std;
long long power(int a, int b){
    long long res = 1;
    for(int i = 1; i <= b; i++)
        res = res*a;
    return res;
}
int main()
{
    long long t, k, c, s;
    cin>>t;
    for(int test = 1; test <= t; test++){
        cin>>k>>c>>s;
        cout<<"Case #"<<test<<": "; 
        for(int i = 0; i < k; i++){
            long long ans = power(k, c-1)*i + 1;
            cout<<ans<<" ";
        }
        cout<<endl;
    }
}